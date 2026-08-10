#import python system files
import sys
import os
import shutil
from datetime import date
#import 3rd party files
from fpdf import FPDF
import pandas as pd
import sqlalchemy
import numpy as np
import mysql.connector
from fpdf.enums import XPos, YPos
#import local files
import utils
from ResultsClass import TestResults


def report(conn,PLOT_DIR):
    txId = None
    rxId = None
    bid = None
    rxFlag = False
    txFlag = False
    bidFlag = False
    help = False
    argn = 1

    while argn < len(sys.argv):
        arg = sys.argv[argn]
        argn += 1
        if arg == "-txid":
            txId = sys.argv[argn]
            argn += 1
        elif arg == "-rxid":
            rxId = sys.argv[argn]
            argn += 1
        elif arg == "-bid":
            bid = sys.argv[argn]
            argn += 1
        else:
            print("Unknown option %s" % arg)
            return
    if help:
        print("-txid          transmit test id")
        print("-rxid          receive test id")
        print("-bid          Bounce test id")
        return

    dic    = list()
    rxlist    = list()
    status = list()
    config = utils.ReadIni('testreport.ini')
    data   = TestResults(conn,rxId,txId,bid,PLOT_DIR)
    
    if rxId != None:
        data.getRxData()

        rxPwrCom      = data.rxPwrCom
        xcvrGain      = data.xcvrGain
        nf            = data.nf
        rxFreq        = data.rxFreq
        sn = data.sn
        dic.append(rxPwrCom)
        dic.append(rxFreq)
        dic.append(xcvrGain)
        dic.append(nf)
    else: 
        rxPwrCom      = ('Receive Power Supply Consumption Limits',"NA")
        xcvrGain      = ('Receiver Gain',"NA")
        nf            = ("Receiver Noise Figure","NA")
        rxFreq        = ('Receiver Input Frequency',"NA")
        sn = data.sn
        dic.append(rxPwrCom)
        dic.append(rxFreq)
        dic.append(xcvrGain)
        dic.append(nf)


    if txId != None:
        data.getTxData()
        txPwrCom      = data.txPwrCom
        harm          = data.harm
        temp          = data.txTemp
        flat          = data.flat
        rl            = data.rl
        txFreqOut     = data.txFreqOut
        sn = data.sn
        txPout = data.txPout
        dic.append(txFreqOut)
        dic.append(txPwrCom)
        dic.append(txPout)
        dic.append(harm)
        dic.append(rl)
        dic.append(flat)
        dic.append(temp)
    else: 
        txPwrCom      = ('Transmit Power Supply Consumption Limits', 'NA')
        harm          = ('Harmonics', 'NA')
        temp          = ('Temperature Sensors', 'NA')
        flat          = ('Transmit Power Flatness', 'NA')
        rl            = ('Reference Source Port Return Loss', 'NA')
        txFreqOut     = ('Transmit Output Frequency', 'NA')
        sn = data.sn
        txPout = ("Transmit In-Band Output Peak Power","NA")
        dic.append(txFreqOut)
        dic.append(txPwrCom)
        dic.append(txPout)
        dic.append(harm)
        dic.append(rl)
        dic.append(flat)
        dic.append(temp)

    if bid != None:
        data.getBounceData()
        bounce        = data.bounce
        dic.append(bounce)
        sn = data.sn
    else: 
        bounce        = ('Bounce Test', 'NA')
        dic.append(bounce)
        sn = data.sn
    if len(dic)!=0:

        for i in range(len(dic)): 
            if(dic[i][0]=='Bounce Test'):
                clkStatus = dic[i][2]
                break
                
        results = any(elem[1] == "Fail" for elem in dic if len(elem) > 0)
        if results == False:
            Status = "PASS"
        else:
            Status = "FAIL"
        print(f"rxId:{rxId}")
        print(f"txId:{txId}")
        print(f"bid:{bid}")

        if data.hx_failed == False and clkStatus != True  :
            print("Overall Status: ",Status)
        else:
            if clkStatus == False: 
                print(f"Overall Status: {Status} (This module failed sub harmonics. All other test Passed)")
            else: 
                print(f"Overall Status: FAIL")

        if ([sn[0]]*len(sn)==sn) and ([data.sessionId[0]]*len(data.sessionId)==data.sessionId): 
            print(f'Serial Number: {sn[0]}')
        else: 
            print(f'Serial Number: Not Unique')

        for key in dic:
            if key == None:
                pass
            elif len(key)==0:
                pass
            else:
                print(f"{key[0]} : {key[1]}")
        if(clkStatus == True):
            print("SiTime Clock : Fail")
        else: 
            print("SiTime Clock : Pass")

if __name__ == '__main__':
    PLOT_DIR ="\plots"       
    conn = mysql.connector.connect(user='root', password ='Pr0dRag343Ver!', database='TetraProd', host='192.168.3.66')
    status = report(conn,PLOT_DIR)
    conn.close()
    try:
        shutil.rmtree(PLOT_DIR)
    except FileNotFoundError:
        pass
