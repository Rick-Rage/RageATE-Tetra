from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import subprocess
import sys
import os
import pandas as pd
import mysql.connector
sys.path.append('../utils')
import SqlFuncs
import utils


try:
    cnx = mysql.connector.connect(user='root', password="Pr0dRag343Ver!", database='TetraProd', host='192.168.3.66')
except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

cursor = cnx.cursor()


cursor.execute('SELECT distinct(pcba_serial_number) FROM tetra_configuration')
resp = (list(cursor))
sns = [list(row) for row in resp]
flat = sum(sns,[])
print(flat)

for pcba_serial_number in flat:
    moduleSerialNumber = None
    configID = None
    asy_id = None
    burnInLot = None
    rx = None
    tx = None
    bounce = None
    configPG = None
    asyPF = None
    BurnInPF = None
    passfail = None
    try:
        cursor.execute(f'SELECT pass_fail from tetra_configuration where date_time = (SELECT MAX(date_time) from tetra_configuration where pcba_serial_number = "{pcba_serial_number}")')
        configPF = cursor.fetchone()[0]
        cursor.execute(f'SELECT id from tetra_configuration where date_time = (SELECT MAX(date_time) from tetra_configuration where pcba_serial_number = "{pcba_serial_number}")')
        configID = cursor.fetchone()[0]
    except Exception as e:
        print(e)
        pass
    try:
        moduleSerialNumber = "WAM-00"+pcba_serial_number
        cursor.execute(f'SELECT MAX(id) from tetra_assembly where module_serial_number = "{moduleSerialNumber}" ')
        asy_id = cursor.fetchone()[0]
        cursor.execute(f'SELECT module_serial_number,pass_fail  from tetra_assembly where id = "{asy_id}"')
        moduleSerialNumber = cursor.fetchone()
        asyPF = moduleSerialNumber[1]
        moduleSerialNumber = moduleSerialNumber[0]
    except Exception as e:
        print(e)
        pass
    try:
        cursor.execute(f'SELECT MAX(lot_id),pass_fail from tetra_burn_in_asy where DUTSN = "{moduleSerialNumber}"')
        burnInLot = cursor.fetchone()
        BurnInPF = burnInLot[1]
        burnInLot = burnInLot[0]
        
    except Exception as e:
        print(e)
        pass
    try:
        FinalTestTime,rx,tx,bounce = SqlFuncs.lookupFinalTest(moduleSerialNumber)
        try:
            os.chdir('C:\\3500004_TetraProductionReportGenerator')
            os.system(f"python finalTestOutcome.py -txid {tx} -rxid {rx} -bid {bounce} >Status.txt")
            outputline = moduleSerialNumber
            with open("Status.txt") as fh:
               for line in fh:
                    print(line)
                    if line.find("Overall Status") != -1:
                        if line.find("PASS") != -1:
                            passfail = "PASS"
                        else:
                            passfail = "Fail"
            
            os.remove('Status.txt')
        except Exception as e:
            print(e)
            pass
    except:
        pass
        
    if moduleSerialNumber == None: moduleSerialNumber = 'NULL'
    if configID == None: configID = 'NULL'
    if asy_id == None: asy_id = 'NULL'
    if burnInLot == None: burnInLot = 'NULL'
    if rx == None: rx = 'NULL'
    if tx == None: tx = 'NULL'
    if bounce == None: bounce = 'NULL'
    if configPF == None: configPF = 'NULL'
    if asyPF == None: asyPF = 'NULL'
    if BurnInPF == None: BurnInPF = 'NULL'
    if passfail == None: passfail = 'NULL'
    if moduleSerialNumber != "NULL":
        cursor.execute(f"Insert into Module (Module_SN,PCB_SN,Config_ID,Asy_ID,Burnlot_ID,RXTest_ID,TXTest_ID,BounceTest_ID,Config_PF,Asy_PF,Burnlot_PF,FinalTest_PF) Values ('{moduleSerialNumber}','{moduleSerialNumber[-4:]}','{configID}','{asy_id}','{burnInLot}','{rx}','{tx}','{bounce}','{configPF}','{asyPF}','{BurnInPF}','{passfail}')")


cnx.commit()
