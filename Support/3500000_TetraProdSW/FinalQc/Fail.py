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
   
   
cursor.execute('SELECT distinct(MSN) FROM tetra_header')
resp = (list(cursor))
sns = [list(row) for row in resp]
flat = sum(sns,[])
print(flat)

for moduleSerialNumber in flat:
    try:
        FinalTestTime,rx,tx,bounce = SqlFuncs.lookupFinalTest(moduleSerialNumber)
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
                    cursor.execute(f"Insert into Module (Module_SN,PCB_SN,FinalTest_PF) Values ('{moduleSerialNumber}','{moduleSerialNumber[-4:]}','{passfail}')")
                    print(cursor)
        os.remove('Status.txt')
    except:
        continue
        
cnx.commit()