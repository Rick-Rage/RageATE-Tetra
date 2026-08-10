import mysql.connector
from datetime import date, datetime, timedelta
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import csv

def convertTuple(tup):
    st = ','.join(map(str, tup))
    return st
 
    
    
    
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
cursor.execute(f"SELECT count_id,noisefig_dB_,peak_p_dBm_,peak_gain_dB_,bp_rfon_dBm_Hz_ FROM tetra_RX_data WHERE abs_time_stamp_ BETWEEN '2022-08-24 00:00:00' AND '2023-02-8 00:00:00' AND count_id > 1775533 ")
resp = cursor.fetchall()
print(resp[0])


i = 0
with open("NoiseFigureFix02282023.csv", 'a') as file:
  # file.write('ID,OLD,,,,,ALTERATION,,,,,UPDATED\n')
  # file.write(',noisefig_dB_,peak_p_dBm_,peak_gain_dB_,bp_rfon_dBm_Hz_, ,noisefig_dB_,peak_p_dBm_,peak_gain_dB_,bp_rfon_dBm_Hz_, ,noisefig_dB_,peak_p_dBm_,peak_gain_dB_,bp_rfon_dBm_Hz_\n')
  for thing in resp:
    file.write(convertTuple(thing))
    file.write(", ,")
    if thing[1] != -1:
        file.write(f"{str(thing[1])} - 2,")
    else:
        file.write(f"{str(thing[1])},")
    file.write(f" {str(thing[2])} + 2, {str(thing[3])} + 2, {str(thing[4])} + 2, , ")
    thing = list(thing)
    if thing[1] != -1:
        thing[1] = thing[1]-2
    thing[2] = thing[2]+2
    thing[3] = thing[3]+2
    thing[4] = thing[4]+2
    file.write(f"{thing[1]},{thing[2]},{thing[3]},{thing[4]},\n")
    cursor.execute(f"UPDATE tetra_RX_data set noisefig_dB_ = '{thing[1]}', peak_p_dBm_ = '{thing[2]}', peak_gain_dB_ = '{thing[3]}',bp_rfon_dBm_Hz_ = '{thing[4]}' WHERE count_id = '{thing[0]}'")
    cnx.commit()
    print(thing[0])
