
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
    cnx = mysql.connector.connect(
        user='root', password="Pr0dRag343Ver!", database='TetraProd', host='192.168.3.66')
except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

cursor = cnx.cursor()

cursor.execute(
    f'SELECT MAX(lot_id),Pass_fail from tetra_burn_in_asy where DUTSN = "WAM-000354"')
burnInLot = cursor.fetchone()
print(burnInLot)
cursor.execute(f'SELECT MAX(id) from tetra_assembly where module_serial_number = "WAM-000354" ')
asy_id = cursor.fetchone()
print(asy_id)