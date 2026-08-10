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


cursor.execute('SELECT distinct(Module_SN) FROM Module')
resp = (list(cursor))
sns = [list(row) for row in resp]
flat = sum(sns,[])
print(flat)

for pcba_serial_number in flat:
    try:
        txattn = SqlFuncs.lookupFinalTestattn(pcba_serial_number)
        cursor.execute(f"UPDATE Module SET TXATTN_ID = '{txattn}' WHERE Module_SN = '{pcba_serial_number}'")
    except Exception as exp:
        print(exp)

cnx.commit()
