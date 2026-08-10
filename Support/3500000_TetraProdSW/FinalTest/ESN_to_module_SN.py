import mysql.connector
import sys


try:
    cnx = mysql.connector.connect(user='root', password='Pr0dRag343Ver!', database='TetraProd', host='192.168.3.66')
except mysql.connector.Error as err:
    print(err)
    
cursor = cnx.cursor(buffered=True)
arglist = str(sys.argv)
esn = (sys.argv)[1]


try:
    cursor.execute(f"SELECT id from tetra_configuration where esn = '{esn}'")
    configid = cursor.fetchone()[0]

    cursor.execute(f"SELECT Module_SN from Module where Config_ID = '{configid}'")
    module_sn = cursor.fetchone()[0]

except:
   print("ERROR - No Module found with that ESN")
else:
    print(module_sn)
