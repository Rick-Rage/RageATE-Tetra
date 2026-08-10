#import 3rd party files
import pandas as pd
import numpy as np
from datetime import date
#import local files
import utils

class DataGatherer:
    """
    A class for gathering data from the test results database.
    ...
    Attributes
    ----------
    conn : mysql db connector
    rxID : Test Id for the receive table data
    txId : Test Id for the transmit table data

    Methods
    --------
    getModuleInfo():
        Returns WAM's sn (serial number), pmIC (power manage IC fw Verision),
        revision, partNum, and the data the module was tested (dateTested)

    createRxDf(rxId):
        Selects rx data based a test id (rxId) and create a Dataframe
    createTxDf(txId):
        Selects tx data based a test id (txId) and create a Dataframe


    """
    def __init__(self,conn,rxId,txId,bid):
        """
        Constructs all the necessary Attributes for the DataGatherer object.

        Parameters
        ----------
        conn : mysql db connector
            test result database
        rxId : int
            test id for recieve test entry
        txId : int
            test id for transmit test entry
        sn   : str
            Serial number  for module being tested.
        rxDf : None
            space holder for return database
        txDf : None
            space holder for return database
        dateTested : str
            date when the module was tested
        revision : str
            Modules top level revision
        partNum : str
            RaGE Part number 508XXXX
        fwVer : str
            Firmware rev and hardware for module
        pmicFwVer : str
            Power management IC firmware revision
        conn : db connector object
        """
        self.rxId = rxId
        self.txId = txId
        self.bid = bid
        self.sn = []
        self.rxDf = None
        self.txDf = None
        self.dateTested = 0
        self.revision = 0
        self.partNum =  0
        self.fwVer =  0
        self.pmicFwVer =  0
        self.conn = conn
        self.err = ""
        self.validRx = False
        self.validTx = False
        self.bounceDf = None
        self.bounceTestFlag = False
        self.bounceSn = 0
        self.txidFlag = None
        self.rxidFlag = None
        self.test_type = ""
        self.test_250M = False 

    def get_all_rev_c_id_ser_num(self):
        """Returns all entries for rev C released modules"""
        query = pd.read_sql_query (f" SELECT  id from tetra_header;", self.conn)
        df = pd.DataFrame(query)
        idList = list(df["id"])
        self.txidFlag = any(elem == self.txId for elem in idList )
        self.rxidFlag = any(elem == self.rxId for elem in idList )
  
        #     results = any(elem == "FAIL" for elem in status)
        
        for i in idList:
            if self.rxId != None and int(i) == int(self.rxId):
                self.validRx = True
            if self.txId != None and int(i) == int(self.txId):
                self.validTx = True
        return self.validTx,self.validRx

    def getBounceData(self): 
        
        query = pd.read_sql_query (f'''SELECT * FROM TetraProd.Bounce_data where id = '{self.bid}';''', self.conn)
        self.bounceDf = pd.DataFrame(query)
        try: 
            self.bounceSn = self.bounceDf.msn_dut_sn_[0]
            self.sn.append(self.bounceSn )
            
        except IndexError:
            self.bounceTestFlag = False
            
        return self.bounceDf


    def getModuleInfo(self,test):
        """
        Creates a dataframe that holds unique identifier for each test,
        such as test Id, module serial number for the module being tested,
        module part number, firmware version, power management IC firmare rev,
        and module revision.

        Parameters
        ----------
        None

        Returns
        ----------
        infoDf
            A datafrane with a single row which can be indexed to obtain Module/Test info
        """
        if test == "bounce":
            table = "BounceHeader"
            id = self.bid
        else: 
            table = "tetra_header"
            if test == 'rx': 
                id = self.rxId
            else: 
                id = self.txId

        if id != None: 
            try:
                query1 = pd.read_sql_query (
                    f" SELECT * from {table} where id = {id};",
                    self.conn)
                df = pd.DataFrame(query1)
            except:
                self.err = self.err + "Failed to read tx data table from database. check  txid"
                return self.err
        else: 
            pass 
            
        return df
    
    def createRxDf(self,rxId):
        """
        Creates a dataframe of Rx Data table.
        Parameters
        ----------
        rxID : int, required
            A unique test id for the receice test database entry to be selected
        Returns
        ----------
        rxDf
            A dataframe with all the entries for RX Test for the provided test id
        """
        try:
            sqlQuery = pd.read_sql_query (
                f' SELECT * FROM {"tetra_RX_data"} where id = {rxId}',
                 self.conn)
            self.rxDf = pd.DataFrame(sqlQuery)
            return self.rxDf
        except:
            self.err = self.err + "Failed to read rx data table from database. check  rxid"
            return self.err

    def createTxDf(self,txId):
        """
        Creates a dataframe of Tx Data table.
        Parameters
        ----------
        txID : int, required
            A unique test id for the transmit test database entry to be selected
        Returns
        ----------
        txDf
            A dataframe with all the entries for TX Test for the provided test id
        """
        err = ""
        try:
            sqlQuery = pd.read_sql_query (
                f' SELECT * FROM {"tetra_TX_data"} where id = {txId}',
                 self.conn)
            self.txDf = pd.DataFrame(sqlQuery)
            return self.txDf
        except:
            self.err = self.err + "Failed to read tx data table from database.Check  txid "
            return self.err
