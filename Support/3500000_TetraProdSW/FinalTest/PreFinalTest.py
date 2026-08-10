import mysql.connector
import sys


try:
    cnx = mysql.connector.connect(user='root', password='Pr0dRag343Ver!', database='TetraProd', host='192.168.3.66')
except mysql.connector.Error as err:
    print(err)

cursor = cnx.cursor(buffered = True)
#TA22240078,0x00003609B620,2224,C.01, Wideband Antenna Module,5083561, RaGE Systems, www.ragesystems.com
arglist = str(sys.argv)

sn = (sys.argv)[1].split(",",1)[0]


cursor.execute(("SELECT id FROM `tetra_header` WHERE MSN = '{}'").format(sn))
idnum = cursor.fetchone()
if idnum != None:
    test = ("This module has been tested before.")
else:
    test = ("This module has not been tested before.")


#loc = (sys.argv)[2]
try:
    q=f"SELECT UPPER(Config_PF) FROM Module WHERE Module_SN = '{sn}';"
    cursor.execute(q)
    ans = list(cursor)
    passfail = ans[0][0]

    if(passfail == "FAIL"):
        print("STOP - FAILED PROGRAMMING")
        print("LAST SEEN: N/A")
        print(test)
        exit()
except:
    print("STOP - NO PROGRAMMING DATA")
    print("LAST SEEN: N/A")
    print(test)
    exit()
try:
    q=f"SELECT UPPER(Asy_PF) FROM Module WHERE Module_SN = '{sn}';"
    cursor.execute(q)
    ans = list(cursor)
    passfail = ans[0][0]

    if(passfail == "FAIL"):
        print("STOP - FAILED ASSEMBLY")
        print("LAST SEEN: ASSEMBLY")
        print(test)
        exit()
except:
    print("STOP - NO ASSEMBLY DATA")
    print("LAST SEEN: PROGRAMMING")
    print(test)
    exit()

try:
    q=f"SELECT UPPER(Burnlot_PF) FROM Module WHERE Module_SN = '{sn}';"
    cursor.execute(q)
    ans = list(cursor)
    passfail = ans[0][0]
    
    if not passfail:
        print("STOP - NO BURN IN DATA")
        print("LAST SEEN: ASSEMBLY")
        print(test)
        exit()
    
    if(passfail == "FAILED"):
        print("STOP - FAILED BURN IN")
        print("LAST SEEN: BURN IN")
        print(test)
        exit()
except:
    print("STOP - NO BURN IN DATA")
    print("LAST SEEN: ASSEMBLY")
    print(test)
    exit()

# q = ("UPDATE tetra_location SET location = '{}' WHERE module_serial_number = '{}';").format(loc,MSN)

print("PASS")
print("LAST SEEN: BURN IN")
print(test)
# try:
#     cursor.execute(q)
# except:
#     print("failed to upload")
# else:
#     print("changed location")
cnx.commit()
#close the cursor
cursor.close()
