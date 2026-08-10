"""
Company: Rage Systems
Engineer: Colin Martin
Create:
Module Name: ResultClass
Project Name: Tetra Wideband Antenna Module
Description:

"""
#import systems files
from datetime import date
import shutil
import os
#import 3rd party files
import pandas as pd
import numpy as np
import re
#import local files
from data_gatherer_class import DataGatherer
import utils
import warnings

warnings.filterwarnings('ignore')


class TestResults:
    """
    A class test results.
    ...
    Attributes
    ----------
    conn : mysql db connector
    rxID : Test Id for the receive table data
    txId : Test Id for the transmit table data

    Methods
    --------
    getData():
        Creates the dataframe and compares test point to threshold limits.

    gainCheck():
        Checks receiver gain

    nFCheck():
        Checks Noise Figure

    powerCheck():
        Checks power Consumption

    tempCheck():
        Checks Temperature sensors

    txFlatness():
        Checks transmit Flatnes

    txPoutCheck():
        Check transmit power out

    txFreq():
        Checks input frequency range

    rxFreq():
        Checks output frequency range
    """

    def __init__(self,conn,rxId,txId,bid,PLOT_DIR):
        """
        Constructs all the necessary Attributes for the DataGatherer object.

        Parameters
        ----------
        data : DataGatherer object
            creates dataframes from receive and transmit data tables
        conn : mysql db connector
            test result database
        rxId : int
            test id for recieve test entry
        txId : int
            test id for transmit test entry
        pwrCom   : tuple
            ((number,failures),0) for power Consumption test
        xcvrGain : tuple
            ((number,failures),0) for  receicer gain test
        bounceTest : tuple
            ((number, failures),0) for receiver gain test
        nf : tuple
            ((number,failures),0) for receicer noise figure test
        rl : tuple
            ((number,failures),0) for return loss test
        txFreqOut : tuple
            ((number,failures),0) for transmit frequency Out test
        txPout : tuple
            ((number,failures),0) for transmit power Out test
        flat : tuple
            ((number,failures),0) for transmit flatness test
        sn   : str
            Serial number  for module being tested.
        revision : str
            Modules top level revision
        partNum : str
            RaGE Part number 508XXXX
        fwVer : str
            Firmware rev and hardware for module
        pmicFwVer : str
            Power management IC firmware revision
        infoDf : None
            space holder for return database
        config : fileObject
            hold test threshold and other config information
        """
        self.data = DataGatherer(conn,rxId,txId,bid)
        self.conn = conn
        self.rxId = rxId
        self.txId =  txId
        self.bid = bid
        self.txPwrCom = []
        self.rxPwrCom = []
        self.xcvrGain = []
        self.txTemp = []
        self.rxTemp = []
        self.bounceTest = []
        self.bounce = []
        self.nf = []
        self.rl = []
        self.txFreqOut = []
        self.txPout = []
        self.flat = []
        self.sn = []
        self.revision = 0
        self.partNum =  0
        self.fwVer =  0
        self.pmicFwVer =  0
        self.infoDf = None
        self.config = utils.ReadIni('testreport.ini')
        self.err = ""
        self.validRx = False
        self.validTx = False
        self.harm = 0
        self.PLOT_DIR = PLOT_DIR #Create folder to hold images for  test report
        self.bounceTestFlag = False
        self.txTestFlag = False
        self.rxTestFlag = False
        self.hx_failed = False
        self.test_type = ""
        self.sessionId  = []
        self.clkFailure = False

    def getBounceData(self):
        self.bounceTest =  self.data.getBounceData()
        # self.bounceTest.to_csv("bounceTest.csv")
        self.infoDf = self.data.getModuleInfo('bounce')
        self.sn.append(self.infoDf.MSN[0])
       
        self.test_type = self.infoDf['Test_Parameters_File_Name'][0].split()[-1].split('-PROD-')[-1].split('_')[0]
        self.sessionId.append(self.infoDf["Session_ID"][0])
        try:
            self.bounce = self.bounceCheck()
          
        except ZeroDivisionError:
            self.bounceTestFlag = True

    def  getRxData(self):
        """
        Gather pass and fail for all test

        Paramters
        ---------
        None

        Returns
        None
        """
        if self.rxId == None:
            pass
        else:
            self.validTx,self.validRx = self.data.get_all_rev_c_id_ser_num()
            self.infoDf = self.data.getModuleInfo('rx')

            self.sn.append(self.infoDf.MSN[0])

            self.test_type = self.infoDf['Test_Parameters_File_Name'][0].split()[-1].split('-PROD-')[-1].split('_')[0]
            self.sessionId.append(self.infoDf["Session_ID"][0])
            self.rxDf =  self.data.createRxDf(self.rxId)
            try:
                self.xcvrGain = self.gainCheck()
                self.rxPwrCom = self.rxPowerCheck()
                self.nf = self.nFCheck()
                self.rxFreq = self.rxFreq()
            except ZeroDivisionError:
                self.rxTestFlag = True

    def getTxData(self):
        """
        Gather pass and fail for all test

        Paramters
        ---------
        None

        Returns
        None
        """
        if self.txId == None:
            pass
        else:
            self.validTx,self.validRx = self.data.get_all_rev_c_id_ser_num()
            self.infoDf = self.data.getModuleInfo('tx')
            self.sn.append(self.infoDf.MSN[0])
            self.test_type = self.infoDf['Test_Parameters_File_Name'][0].split()[-1].split('-PROD-')[-1].split('_')[0]
            self.sessionId.append(self.infoDf["Session_ID"][0])

            self.txDf  =  self.data.createTxDf(self.txId)
            # self.sn.append(self.infoDf["MSN"][0])
            try:
                self.harm = self.harmonic()
                self.txPout = self.txPoutCheck()
                self.txFreqOut = self.txFreq()
                self.flat = self.txFlatness()
                self.rl = self.returnLossCheck()
                self.txPwrCom = self.txPowerCheck()
                self.txTemp = self.txTempCheck()
            except ZeroDivisionError:
                self.txTestFlag = True
        # self.err = self.data.err

    def bounceCheck(self):
        """
        Checks the Bounce Test

        Paramters
        ---------
        None

        Returns
        tuple with number of pass and total number of entries
        """
        if self.bid !=None:
            if((self.bounceTest["ClkTest_PASS_FAIL_"][0] == "Fail") or (self.bounceTest["ClkTest_PASS_FAIL_"][0] == "FAIL")): 
                self.clkFailure = True 
            freq = []
            ampl = []

            for i in self.bounceTest.columns:
                temp = i.split("_")
                if temp[0] == 'ampl':
                    ampl.append(list(self.bounceTest[i]))
                elif temp[0]=='freq':
                    freq.append(list(self.bounceTest[i]))
            powList = [element for innerList in ampl for element in innerList]
            freqList = [element for innerList in freq for element in innerList]
            passedPow = []
            passedFreq = []
            for i in range(len(powList)):
                if powList[i]<= float(self.config["BouncePowerLimits"]["upper"]) and powList[i] >= float(self.config["BouncePowerLimits"]["lower"]):
                    passedPow.append(True)
                if freqList[i]<= float(self.config["BounceFreqRange"]["upper"])  and freqList[i] >= float(self.config["BounceFreqRange"]["lower"]):
                    passedFreq.append(True)
            if (passedFreq.count(True)==passedPow.count(True)==len(freqList)):
                status = "Pass"
            else:
                status = "Fail" 
            return (("Bounce Test",status,self.clkFailure))
        # return ((passedFreq.count(True),len(freqList)),passedPow.count(True)/len(powList),status,'bounce')


    def gainCheck(self):
        """
        Checks the receiver gain

        Paramters
        ---------
        None

        Returns
        tuple with number of pass and total number of entries
        """
        if self.rxId != None:
            freq_start_rx = float(self.config["TestLimits"]["freq_start_rx"])
            freq_end_rx = float(self.config["TestLimits"]["freq_end_rx"])

            gainHigh = float(self.config["TestLimits"]["gainHigh"])
            gainLow = float(self.config["TestLimits"]["gainLow"])
            gainhigh = float(self.config["TestLimits"]["gainhigh"])
            gainlow = float(self.config["TestLimits"]["gainlow"])
            gainGf = self.rxDf.copy()
            selected_cols = ['RF_FREQ','peak_gain_dB_','RX_PORT','id']
            gainGf = gainGf[selected_cols]
            gainGf = gainGf[(gainGf['RF_FREQ']>=freq_start_rx) & (gainGf['RF_FREQ']<=freq_end_rx)]

            freq = list(gainGf.RF_FREQ)
            cond = [(gainGf["RF_FREQ"] == i) for i in freq]
            flat_up = float(self.config["TestLimits"]["gainHigh"])
            flat_ll = float(self.config["TestLimits"]["gainLow"])
            freq_end_rx = float(self.config["TestLimits"]["freq_end_rx"])

            gainGf['UpperLim'] = 0
            gainGf['LowerLim'] = 0

            gainGf["UpperLim"].mask(gainGf["RF_FREQ"]<=freq_end_rx , flat_up, inplace=True)
            gainGf["LowerLim"].mask(gainGf["RF_FREQ"]<=freq_end_rx , flat_ll, inplace=True)

            gainGf["Results"] = gainGf["peak_gain_dB_"].ge(gainGf['LowerLim']) & gainGf["peak_gain_dB_"].le(gainGf['UpperLim'])
            # print(gainGf.loc[gainGf['Results'] == False])
            # print(((list(gainGf.Results).count(True),len(gainGf)),list(gainGf.Results).count(True)/len(gainGf)))

            if ((list(gainGf.Results).count(True))==len(gainGf)):
                status = "Pass"
            else:
                status = "Fail"
            return (("Receiver Gain",status))
        else:
            pass
        # print((list(gainGf.Results).count(True),len(gainGf)),list(gainGf.Results).count(True)/len(gainGf),'rxGain')

    def nFCheck(self):
        """
        Checks the receiver noise figure

        Paramters
        ---------
        None

        Returns
        tuple with number of pass and total number of entries
        """
        if self.rxId != None:
            freq_start_nf = float(self.config["TestLimits"]["freq_start_nf"])
            freq_end_nf = float(self.config["TestLimits"]["freq_end_nf"])
            lim_band_edge = float(self.config["TestLimits"]["nf_20_40_GHz"])

            nfDf =   self.rxDf.loc[self.rxDf['noisefig_dB_'] != float(self.config["TestLimits"]["noise_figure_filter"])]
            nfDf = nfDf[(nfDf['RF_FREQ']>=freq_start_nf) & (nfDf['RF_FREQ']<=freq_end_nf)]
            freq = [20,25,30,35,40]
            nfDf = nfDf.loc[nfDf.apply(lambda x: x.RF_FREQ in freq, axis=1)]
            nfDf = nfDf[["RF_FREQ","RX_PORT","noisefig_dB_"]]
            nfDf["UpperLim"] = float(self.config["TestLimits"]["noiseFigure_band"])
            nfDf["UpperLim"].mask(nfDf["RF_FREQ"]==freq_start_nf, lim_band_edge, inplace=True)
            nfDf["UpperLim"].mask(nfDf["RF_FREQ"]==freq_end_nf, lim_band_edge, inplace=True)
            nfDf["Results"] =  nfDf["noisefig_dB_"].le(nfDf['UpperLim'])
            # dfp = nfDf.pivot_table(index=['RF_FREQ'], columns=['RX_PORT',"Results"],values ='noisefig_dB_')
            if list(nfDf.Results).count(True)==len(nfDf):
                status = "Pass"
            else:
                status ="Fail"
            return ('Receiver Noise Figure',status)
            # return ((list(nfDf.Results).count(True),len(nfDf)),list(nfDf.Results).count(True)/len(nfDf),'nf')

    def rxPowerCheck(self):
        """
        Checks the total power consumed by the module

        Paramters
        ---------
        None

        Returns
        tuple with number of pass and total number of entries and the actual power consumed
        """
        if self.rxId != None:
            selectedCols = ['power_w_Watt_']
            pwrDf = self.rxDf.copy()[selectedCols]
            pwrDf = pwrDf.loc[pwrDf['power_w_Watt_'] != 1]
            powerPassed = list(pwrDf['power_w_Watt_'] <  float(self.config["TestLimits"]["powerCon"]))
            pwrDf.loc[:,'PowerResults'] = powerPassed
            power = pwrDf['power_w_Watt_']
            if (powerPassed.count(True)==len(pwrDf)):
                status = "Pass"
            else:
                status ="Fail"
            return ('Receive Power Supply Consumption Limits',status)
    # return ((powerPassed.count(True),len(pwrDf)),power[0],'RxPwrCon')
    # return ((powerPassed.count(True),len(pwrDf)),1,'RxPwrCon')
    def txPowerCheck(self):
        """
        Checks the total power consumed by the module

        Paramters
        ---------
        None

        Returns
        tuple with number of pass and total number of entries and the actual power consumed
        """
        if self.txId != None:
            selectedCols = ['power_w_Watt_']
            pwrDf = self.txDf.copy()[selectedCols]
            pwrDf = pwrDf.loc[pwrDf['power_w_Watt_'] != 1]
            powerPassed = list(pwrDf['power_w_Watt_'] <  float(self.config["TestLimits"]["powerCon"]))
            pwrDf.loc[:,'PowerResults'] = powerPassed
            power = pwrDf['power_w_Watt_']
            if (powerPassed.count(True)==len(pwrDf)):
                status = "Pass"
            else:
                status = "Fail"
            return (("Transmit Power Supply Consumption Limits",status))
        # return ((powerPassed.count(True),len(pwrDf)),power[0],'TxPwrCon')

    def harmonic(self):
        if self.txId != None:
            self.hx_failed = False
            df = self.txDf[["RF_FREQ_OUT","TX_PORT","h2_dbc_dbc_",'hx_dbc_dbc_']]

            df_h2  = df.copy().loc[df['h2_dbc_dbc_'] != -1]
            df_hx  = df.loc[df['hx_dbc_dbc_'] != -1]
            val = list(df_hx["hx_dbc_dbc_"])
            df_h2.drop(columns=["hx_dbc_dbc_"])
            df_h2["H2_Limit"] = float(self.config["TestLimits"]["h2_lim"])
            df_h2["Hx_Limit"] = float(self.config["TestLimits"]["hx_lim"])

            df_h2["hx_dbc_dbc_"] = val
            df_h2["hx_dbc_dbc_"] = df_h2["hx_dbc_dbc_"]
            df_h2['h2_dbc_dbc_'] = df_h2['h2_dbc_dbc_']

            df_h2['Results_hx'] =  df_h2["hx_dbc_dbc_"].le(df_h2['Hx_Limit'])
            df_h2['Results_h2'] =  df_h2["h2_dbc_dbc_"].le(df_h2['H2_Limit'])
            hx_passed = list(df_h2['Results_hx']).count(True)
            h2_passed = list(df_h2['Results_h2']).count(True)
            if (hx_passed!=12):
                self.hx_failed = True
            if (h2_passed==12):
                status = "Pass"
            else:
                status = "Fail"
            return (("Harmonics",status))


    def returnLossCheck(self):
        """
        Checks the Return Loss

        Paramters
        ---------
        None

        Returns
        tuple with number of pass and total number of entries
        """
        if self.txId != None:
            df = self.txDf[["RF_FREQ_OUT","s11_db_","TX_PORT"]]
            rlDf = df.loc[df['s11_db_'] != -1]
            rlPassed = list(rlDf['s11_db_'] <  float(self.config["TestLimits"]["returnLoss"]))
            rlDf.loc[:,'RLResults'] = rlPassed
            selectedCols = ['s11_db_','RLResults']
            rlDf = rlDf[selectedCols]
            # print(rl_df.loc[rl_df['RLResults'] == False])
            #         dic.append(flat)

            if ((rlPassed.count(True)==len(rlDf))):
                status = "Pass"
            else:
                status = "Fail"
            return (("Reference Source Port Return Loss",status))

    def txTempCheck(self):
        """
        Checks the on board temperatute sensors are within spec

        Paramters
        ---------
        None

        Returns
        tuple with number of pass and total number of entries and a list of the temp sensor values
        The mean of the each sensor is return
        """
        if self.txId != None:
            selectedCols = ['adar_temp_deg_c_','fpga_temp_deg_c_', 'ext_temp1_deg_c_', 'ext_temp2_deg_c_','ext_temp3_deg_c_', 'ext_temp4_deg_c_']
            tempDf = self.txDf[selectedCols]
            tempDf = tempDf.loc[tempDf["adar_temp_deg_c_"] !=  float(self.config["TestLimits"]["temp_low"])]
            # Take temperature data
            adarTempDegrees = tempDf["adar_temp_deg_c_"].mean()
            fpgaTempDegrees = tempDf["fpga_temp_deg_c_"].mean()
            extTemp1Degrees = tempDf["ext_temp1_deg_c_"].mean()
            extTemp2Degrees = tempDf["ext_temp2_deg_c_"].mean()
            extTemp3Degrees = tempDf["ext_temp3_deg_c_"].mean()
            extTemp4Degrees = tempDf["ext_temp4_deg_c_"].mean()
            temps = ((1,1),[round(fpgaTempDegrees,1),round(extTemp1Degrees,1),round(extTemp2Degrees,1),round(extTemp3Degrees,1),round(extTemp4Degrees,1)],'tempSensor')
            if (temps[1][0] < 55): #
                status = "Pass"
            else:
                status = "Fail"
            return (("Temperature Sensors",status))
            # return temps

    def rxTempCheck(self):
        """
        Checks the on board temperatute sensors are within spec

        Paramters
        ---------
        None

        Returns
        tuple with number of pass and total number of entries and a list of the temp sensor values
        The mean of the each sensor is return
        """
        selectedCols = ['adar_temp_deg_c_','fpga_temp_deg_c_', 'ext_temp1_deg_c_', 'ext_temp2_deg_c_','ext_temp3_deg_c_', 'ext_temp4_deg_c_']
        tempDf = self.rxDf[selectedCols]
        tempDf = tempDf.loc[tempDf["adar_temp_deg_c_"] !=  float(self.config["TestLimits"]["temp_low"])]
        # Take temperature data
        adarTempDegrees = tempDf["adar_temp_deg_c_"].mean()
        fpgaTempDegrees = tempDf["fpga_temp_deg_c_"].mean()
        extTemp1Degrees = tempDf["ext_temp1_deg_c_"].mean()
        extTemp2Degrees = tempDf["ext_temp2_deg_c_"].mean()
        extTemp3Degrees = tempDf["ext_temp3_deg_c_"].mean()
        extTemp4Degrees = tempDf["ext_temp4_deg_c_"].mean()
        temps = ((1,1),[round(fpgaTempDegrees,1),round(extTemp1Degrees,1),round(extTemp2Degrees,1),round(extTemp3Degrees,1),round(extTemp4Degrees,1)],'tempSensor')
        return temps

    def txFlatness(self):
        """
        Checks the transmit power flatness

        Paramters
        ---------
        None

        Returns
        tuple with number of pass and total number of entries
        """
        if self.txId != None:
            freq_start_flat = float(self.config["TestLimits"]["freq_start_flat"])
            freq_end_flat = float(self.config["TestLimits"]["freq_end_flat"])

            selectedCols = ['RF_FREQ_OUT','p_out_fsl_dBm_','TX_PORT']
            df = self.txDf[selectedCols]
            txPoutDf = df.copy()
            txFlat = txPoutDf[["RF_FREQ_OUT","p_out_fsl_dBm_"]]
            txFlat = txFlat.astype({'RF_FREQ_OUT': float,'p_out_fsl_dBm_': float})
            txPouthigh =  float(self.config["TestLimits"]["flatLim"])/2
            txPoutLow = float(self.config["TestLimits"]["flatLim"])/2
            flatLim = float(self.config["TestLimits"]["flatLim"])

            tx_new = txPoutDf.astype({'RF_FREQ_OUT':float,"TX_PORT":float,'p_out_fsl_dBm_':float})
            tx_new = txPoutDf[(txPoutDf['RF_FREQ_OUT']>=freq_start_flat) & (txPoutDf['RF_FREQ_OUT']<=freq_end_flat)]

            test =  tx_new.pivot_table(index=['RF_FREQ_OUT'], columns=['TX_PORT'],values ='p_out_fsl_dBm_')

            band1 = test.loc[20.5:25].describe()
            band2 = test.loc[25.1:32].describe()
            band3 = test.loc[32.1:].describe()
            band1_list = list()
            band2_list = list()
            band3_list = list()

            bandonepass = False
            bandtwopass = False
            bandthreepass = False

            for i in range(1,13,1):
                band1_list.append((band1[i]["max"]-abs(band1[i])["min"],band1[i]["max"]-abs(band1[i])["min"]<= flatLim))
                band2_list.append((band2[i]["max"]-abs(band2[i])["min"],band2[i]["max"]-abs(band2[i])["min"] <= flatLim))
                band3_list.append((band3[i]["max"]-abs(band3[i])["min"],band3[i]["max"]-abs(band3[i])["min"] <= flatLim))

            for i in band1_list:
                if i[1] == True:
                    bandonepass = True
            for i in band3_list:
                if i[1] == True:
                    bandtwopass = True
            for i in band3_list:
                if i[1] == True:
                    bandthreepass = True
            if bandonepass == bandtwopass == bandthreepass:
                result = 3
            if (result == 3):
                status = "Pass"
            else:
                status = "Fail"
            return (("Transmit Power Flatness",status))
        # return ((result,3),0,'TxFlat')


    def txPoutCheck(self):
        """
        Checks peak transmit Power out

        Paramters
        ---------
        None

        Returns
        tuple with number of pass and total number of entries
        """
        if self.txId != None:
            freq_start_tx = float(self.config["TestLimits"]["freq_start_tx"])
            freq_end_tx = float(self.config["TestLimits"]["freq_end_tx"])

            txhigh = float(self.config["TestLimits"]["txhigh"])
            txlow = float(self.config["TestLimits"]["txlow"])

            freq_end_flat = float(self.config["TestLimits"]["freq_end_flat"])
            selectedCols = ['RF_FREQ_OUT','p_out_fsl_dBm_','TX_PORT']
            df = self.txDf[selectedCols]
            txPoutDf = df.copy()

            #import stats file
            txPouthigh = float(self.config["TestLimits"]["txPouthigh"])
            txPoutLow = float(self.config["TestLimits"]["txPoutLow"])

            tx_new = txPoutDf.astype({'RF_FREQ_OUT':float,"TX_PORT":float,'p_out_fsl_dBm_':float})
            tx_new = tx_new.copy()
            tx_new = txPoutDf[(txPoutDf['RF_FREQ_OUT']>=freq_start_tx) & (txPoutDf['RF_FREQ_OUT']<=freq_end_tx)]
            freq = list(tx_new.RF_FREQ_OUT)
            cond = [(tx_new["RF_FREQ_OUT"] == i) for i in freq]

            # freq_lim = list(pout_limits[(pout_limits['RF_FREQ_OUT']>=freq_start_tx) & (pout_limits['RF_FREQ_OUT']<=freq_end_tx)].RF_FREQ_OUT)

            tx_new = tx_new.copy()
            tx_new['UpperLim'] =0
            tx_new['LowerLim'] = 0
            flat_up = float(self.config["TestLimits"]["txPout_u"])
            flat_ll = float(self.config["TestLimits"]["txPout_l"])
            #
            tx_new["UpperLim"].mask(tx_new["RF_FREQ_OUT"]<=freq_end_flat , flat_up, inplace=True)
            tx_new["LowerLim"].mask(tx_new["RF_FREQ_OUT"]<=freq_end_flat , flat_ll, inplace=True)

            tx_new["Results"] = tx_new["p_out_fsl_dBm_"].le(tx_new['UpperLim'])&tx_new["p_out_fsl_dBm_"].ge(tx_new['LowerLim'])
            # print(tx_new.loc[tx_new['Results'] == False])

            # print((list(tx_new.Results).count(True),len(tx_new)),list(tx_new.Results).count(True)/len(tx_new),"TxPout")
            if ((list(tx_new.Results).count(True))==len(tx_new)):
                status = "Pass"
            else:
                status ="Fail"
            return ('Transmit In-Band Output Peak Power',status)
            # return ((list(tx_new.Results).count(True),len(tx_new)),list(tx_new.Results).count(True)/len(tx_new),"TxPout")


    def txFreq(self):
        """
        Checks the range of Transmit frequencies

        Paramters
        ---------
        None

        Returns
        tuple with number of pass and total number of entries
        """
        test_len = len(self.txDf)
        num_ports = len(self.txDf.TX_PORT.unique())
        if self.txId != None:
            freq = self.txDf.RF_FREQ_OUT.unique()
            check = np.linspace(20.0,40.0,test_len)

            if (len(check)/num_ports==len(freq)):
                status = "Pass"
            else:
                status ="Fail"
            return ('Transmit Output Frequency',status)
            # return ((len(check),len(freq)),0,'txFreq')

    def rxFreq(self):
        """
        Checks the range of receive frequencies

        Paramters
        ---------
        None

        Returns
        tuple with number of pass and total number of entries
        """
        test_len = len(self.rxDf)
        num_ports = len(self.rxDf.RX_PORT.unique())

        if self.rxId != None:
            freq = self.rxDf.ref_freq_GHz_.unique()
            check = np.linspace(20.0,40.0,test_len)

            if (len(check)/num_ports==len(freq)):
                status = "Pass"
            else:
                status ="Fail"
            return ('Receiver Input Frequency',status)
            # return ((201,len(freq)),0,'rxFreq')
