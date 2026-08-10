import mysql.connector
import sys


try:
    cnx = mysql.connector.connect(user='root', password='Pr0dRag343Ver!', database='TetraProd', host='192.168.3.66')
except mysql.connector.Error as err:
    print(err)

cursor = cnx.cursor(buffered = True)
#TA22240078,0x00003609B620,2224,C.01, Wideband Antenna Module,5083561, RaGE Systems, www.ragesystems.com
arglist = str(sys.argv)

try:
    sn = (sys.argv)[1].split(",",1)[0]

    cursor.execute(f"SELECT Config_ID FROM `Module` WHERE Module_SN = '{sn}'")
    configid = cursor.fetchone()[0]

    cursor.execute(f"SELECT Asy_ID FROM `Module` WHERE Module_SN = '{sn}'")
    asyid = cursor.fetchone()[0]


    cursor.execute(f"SELECT esn FROM `tetra_configuration` WHERE id = '{configid}'")
    esn = cursor.fetchone()[0]

    cursor.execute(f"SELECT module_revision FROM `tetra_assembly` WHERE id = '{asyid}'")
    rev = cursor.fetchone()[0]

    cursor.execute(f"SELECT DateCode FROM `tetra_assembly` WHERE id = '{asyid}'")
    date = cursor.fetchone()[0]

    print(f"{sn},{esn},{date},{rev}, Wideband Antenna Module,5083561, RaGE Systems, www.ragesystems.com")
except:
    print("ERROR - Failed to find module")