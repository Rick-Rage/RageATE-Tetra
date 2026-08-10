from os import execl
import mysql.connector
from datetime import date, datetime, timedelta
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


Password = "Pr0dRag343Ver!"

def getPassword():
    global Password
    while(Password == ""):
        text, ok = QInputDialog.getText(None, "Attention", "Password?",
                                        QLineEdit.Password)
        if ok and text:
            Password = text
            try:
                connect()
            except:
                Password = ""

def connect():
    global Password
    try:
        cnx = mysql.connector.connect(user='root', password=Password, database='TetraProd', host='192.168.3.66')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None
    else:
        return cnx

def getCartonNum(amount):
    q=f"SELECT Count(id) FROM tetra_final_inspection where Carton = (Select Max(Carton) from tetra_final_inspection) and Carton not like '%l1%';"
    ans = executeOne(q)
    count = ans[0][0]

    q="SELECT MAX(Carton) from tetra_final_inspection where Carton not like '%l1%';"
    ans = executeOne(q)
    cart = ans[0][0]
    
    if cart == None:
        return 1
    q=f"SELECT Count(id) FROM tetra_final_inspection where Carton = (Select Max(Cast(Carton AS int)) from tetra_final_inspection  where Carton not like '%l1%');"
    ans = executeOne(q)
    count = int(ans[0][0])

    q="SELECT MAX(Cast(Carton AS int)) from tetra_final_inspection where Carton not like '%l1%';"
    ans = executeOne(q)
    cart = ans[0][0]
    print(count)
    if count < amount:
        return(int(cart))
    else:
        return(int(cart)+1)
        
def setCartonNum(SN):
    q=f"UPDATE tetra_final_inspection SET Carton = NULL where module_serial_number = '{SN}'" 
    executeOne(q)

    
def checkCartonContent(amount):
    cart = getCartonNum(amount)
    #print(cart)
    q = f"SELECT module_serial_number FROM tetra_final_inspection where Carton = {cart};"
    resp = executeOne(q)
    sns = [list(row) for row in resp]
    flat = sum(sns,[])
    return(flat)
   
    
def checkBurnIn(sn):
    try:
        q = f"SELECT asy_id FROM tetra_burn_in_asy WHERE DUTSN = '{sn}'"
        asyid = executeOne(q)
        asyid = asyid[0][0]
        if asyid == None:
            return 'false'
        else:
            q = f"SELECT id FROM tetra_burn_in_asy WHERE DUTSN = '{sn}'"
            idnum = executeOne(q)
            idnum = idnum[0][0]
            asyid = getAssyId(sn)
            q = f'UPDATE tetra_burn_in_asy SET asy_id = {asyid} WHERE (id = {idnum})'
            x = executeOne(q)
            return 'true'
    except:
        return('false')

def checkSupe(id):
    cnx = connect()
    if cnx is None:
        return None
    cursor = cnx.cursor()
    try:
        q = f"SELECT name FROM tetra_technicians WHERE emp_id = {id} and position = 'Supe'"
        cursor.execute(q)
        name = cursor.fetchone()
        name = name[0]
    except mysql.connector.Error as err:
        print(err)
        name = None
    # Should be just one, but just in case
    for n in cursor:
        pass
    cursor.close()
    cnx.close()
    return name


def getTechnician(id):
    cnx = connect()
    if cnx is None:
        return None
    cursor = cnx.cursor()
    try:
        q = f"SELECT name FROM tetra_technicians WHERE emp_id = {id}"
        cursor.execute(q)
        name = cursor.fetchone()
        name = name[0]
    except mysql.connector.Error as err:
        print(err)
        name = None
    # Should be just one, but just in case
    for n in cursor:
        pass
    cursor.close()
    cnx.close()
    return name

def executeOne(query):
    cnx = connect()
    if cnx is None:
        return None
    cursor = cnx.cursor()
    data = None
    try:
        cursor.execute(query)
        data = list(cursor)
        cnx.commit()
    except mysql.connector.Error as err:
        print(err)
    cursor.close()
    cnx.close()
    return data

def getEsn(id):
    q=f"SELECT esn FROM tetra_configuration WHERE id = '{id}';"
    ans = executeOne(q)
    esn = ans[0][0]
    return(esn)
    
def getconfigidfromMod(sn):
    q=f"SELECT Config_ID FROM Module WHERE Module_SN = '{sn}';"
    ans = executeOne(q)
    id = ans[0][0]
    return(id)

def getFPGAsw(id):
    q=f"SELECT fpga_sw_revision FROM tetra_configuration WHERE id = '{id}';"
    ans = executeOne(q)
    rev = ans[0][0]
    return(rev)

def getFPGAfw(id):
    q=f"SELECT fpga_fw_revision FROM tetra_configuration WHERE id = '{id}';"
    ans = executeOne(q)
    rev = ans[0][0]
    return(rev)

def getPICsw(id):
    q=f"SELECT pmic_sw_revision FROM tetra_configuration WHERE id = '{id}';"
    ans = executeOne(q)
    rev = ans[0][0]
    return(rev)

def lookupPcbaSn(id):
    q=f"SELECT pcba_serial_number FROM tetra_configuration WHERE id = '{id}';"
    ans = executeOne(q)
    pcba = ans[0][0]
    return(pcba)

def lookupAssemblySn(esn):
    q = ("SELECT Module.Asy_ID, Module.Module_SN FROM Module"
    + " INNER JOIN tetra_configuration ON tetra_configuration.id=Module.Config_ID"
    + f" WHERE tetra_configuration.esn = '{esn}';")
    ans = executeOne(q)
    asyId = ans[0][0]
    asySn = ans[0][1]
    return asyId,asySn

def GetRev(sn):
    q = (f"SELECT Asy_ID from Module where Module_SN = '{sn}'")
    ans = executeOne(q)
    print(ans)
    asyid = ans[0][0]
    
    q = (f"SELECT module_revision from tetra_assembly where id = '{asyid}'")
    ans = executeOne(q)

    rev = ans[0][0]
    return(rev)
    
def getAssyId(sn):
    q= f"SELECT id FROM tetra_assembly where module_serial_number = '{sn}' ORDER BY date_time DESC LIMIT 1;"
    ans = executeOne(q)
    asyid = ans[0][0]

    return(asyid)
    
def getAssyIdFromModule(sn):
    q= f"SELECT asy_id FROM Module where Module_SN = '{sn}';"
    ans = executeOne(q)
    asyid = ans[0][0]

    return(asyid)

def lookupPcbConfigInfo(pcb_id):
    q = f"SELECT pcba_part_number,pcba_serial_number,pcba_revision FROM tetra_configuration WHERE id = '{pcb_id}' ORDER BY date_time DESC LIMIT 1;"
    ans = executeOne(q)
    pn = ans[0][0]
    sn = ans[0][1]
    rev = ans[0][2]
    return pn, sn, rev


def getPCBIdfromAssy(sn):
    q= f"SELECT Config_ID FROM Module WHERE Module_SN = '{sn}';"
    ans = executeOne(q)
    pcbId = ans[0][0]
    return(pcbId)

def lookupConfigTest(sn):
    q= f"SELECT Config_ID FROM Module WHERE Module_SN = '{sn}'"
    ans = executeOne(q)
    pcbid = ans[0][0]

    q=f"SELECT pass_fail,date_time FROM tetra_configuration WHERE id = '{pcbid}' ORDER BY date_time DESC LIMIT 1;"
    ans = executeOne(q)
    passfail = ans[0][0]
    datetime = ans[0][1]

    return(datetime,passfail,pcbid)

def lookupFinalTest(sn):

    q = f"SELECT RXTest_ID FROM Module WHERE Module_SN = '{sn}'"
    ans = executeOne(q)
    rx = ans [0][0]
    
    q = f"SELECT TXTest_ID FROM Module WHERE Module_SN = '{sn}'"
    ans = executeOne(q)
    tx = ans [0][0]

    q = f"SELECT BounceTest_ID FROM Module WHERE Module_SN = '{sn}'"
    ans = executeOne(q)
    try:
        bounce = ans [0][0]
    except:
        bounce = "NULL"
        
    q = f"SELECT MAX(Date_Time) FROM tetra_header WHERE id in ('{rx}','{tx}');"
    ans = executeOne(q)
    datetime = ans[0][0]
    
    return (datetime,rx,tx,bounce)

def lookupFinalTestattn(sn):
    q = f"SELECT id FROM tetra_header WHaERE Date_Time =(Select MAX(Date_Time) from tetra_header where MSN = '{sn}' and Test_Name = 'REV-C_TETRA_TX-ATTEN');"
    ans = executeOne(q)
    print(ans)
    print(q)
    try:
        id = ans [0][0]
    except:
        id = None
    return(id)
    
def lookupFinalTestPassFail(id):
    q = f"SELECT FinalTest_PF FROM tetra_header WHERE id = {id};"
    ans = executeOne(q)
    PassFail = ans[0][0]

    return(PassFail)

def lookupAssemblyTest(sn):
    q = f"SELECT Asy_PF,Asy_ID FROM Module WHERE Module_SN = '{sn}'"
    ans = executeOne(q)
    passfail = ans[0][0]
    pcbid = ans[0][1]
    print(pcbid)
    q = f"SELECT date_time FROM tetra_assembly WHERE id = '{pcbid}';"
    ans = executeOne(q)
    datetime = ans[0][0]

    return (datetime,passfail)

def lookupBurnInTest(sn):
    q = f"SELECT Burnlot_ID,Burnlot_PF FROM Module WHERE Module_SN = '{sn}'"
    ans = executeOne(q)
    lotid = ans[0][0]
    passfail = ans[0][1]

    q = f"SELECT end_date_time FROM tetra_burn_in_lot WHERE id = '{lotid}';"
    ans = executeOne(q)
    datetime = ans[0][0]

    return (datetime,passfail)

def lookupPcba(sn):
    q = f"SELECT id FROM tetra_configuration WHERE pcba_serial_number='{sn}' ORDER BY date_time DESC LIMIT 1;"
    ans = executeOne(q)
    id = ans[0][0]
    return id

def getiniDateTime(sn):
    q=f"SELECT date_time FROM tetra_configuration WHERE pcba_serial_number = '{sn}';"
    ans = executeOne(q)
    return(ans)

def updateTetraConfiguration(data):
    fields = list(data.keys())
    values = list(data.values())
    sfields = ','.join(fields)
    svalues = ','.join(values)
    q = f"INSERT INTO tetra_configuration ({sfields}) VALUES ({svalues});"
    executeOne(q)

def updateTetraAssembly(data):
    fields = list(data.keys())
    values = list(data.values())
    sfields = ','.join(fields)
    svalues = ','.join(values)
    q = f"INSERT INTO tetra_assembly ({sfields}) VALUES ({svalues});"
    executeOne(q)

def updateTetraBurnIn(data):
    fields = list(data.keys())
    values = list(data.values())
    sfields = ','.join(fields)
    svalues = ','.join(values)
    q = f"INSERT INTO tetra_burn_in_lot ({sfields}) VALUES ({svalues});"
    executeOne(q)

def lookupTetraBurnLotId(start_date_time):
    q = f"SELECT id FROM tetra_burn_in_lot WHERE start_date_time='{start_date_time}';"
    ans = executeOne(q)
    return ans[0][0]

def updateTetraBurnInasy(data):
    fields = list(data.keys())
    values = list(data.values())
    sfields = ','.join(fields)
    svalues = ','.join(values)
    q = f"INSERT INTO tetra_burn_in_asy ({sfields}) VALUES ({svalues});"
    executeOne(q)

def updateTetraQC(data):
    fields = list(data.keys())
    values = list(data.values())
    sfields = ','.join(fields)
    svalues = ','.join(values)
    q = f"INSERT INTO tetra_final_inspection ({sfields}) VALUES ({svalues});"
    executeOne(q)

def getLotId():
    q = "SELECT id from tetra_burn_in_lot ORDER BY id DESC LIMIT 1;"
    idnum = executeOne(q)
    try:
        idnum = idnum[0][0]
    except:
        idnum = 0
    idnum = idnum + 1
    return(idnum)

def getConfigId():
    q = "SELECT id from tetra_configuration ORDER BY id DESC LIMIT 1;"
    idnum = executeOne(q)
    try:
        idnum = idnum[0][0]
    except:
        idnum = 0
    idnum = idnum + 1
    return(idnum)

def getdatecode(sn):
    q = f"SELECT DateCode FROM tetra_assembly WHERE module_serial_number = '{sn}' ORDER BY date_time DESC LIMIT 1;"
    ans = executeOne(q)
    id = ans[0][0]
    return id

def nowDateTime():
    #'YYYY-MM-DD hh:mm:ss'
    s = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return s

def datetimeToTimeStamp(dt):
    return dt.replace('-','').replace(':','').replace(' ','_')

def ModulepostConfig(pcbaSN,pass_fail,pcbid):
    try:
        q = f"SELECT id,Module_SN from Module where PCB_SN = '{pcbaSN}'"
        ans = executeOne(q)
        existingid = ans[0][0]
        existingModSN = ans[0][1]
    except Exception as ex:
        existingid = None
        existingModSN = None
        print(ex)
    if not existingid:
        try:
            q = f"SELECT id,Module_SN from Module where Module_SN = '{pcbaSN}'"
            ans = executeOne(q)
            existingid = ans[0][0]
            existingModSN = ans[0][1]
        except Exception as ex:
            existingid = None
            existingModSN = None
            print(ex)
        if not existingid:
            q = f"INSERT INTO Module (PCB_SN,Module_SN,Config_PF,Config_ID) VALUES ('{pcbaSN}','{pcbaSN}','{pass_fail}','{pcbid}')"
            executeOne(q)
            print(q)
        else:
            q = f"UPDATE Module set Config_PF = '{pass_fail}',Config_ID = '{pcbid}' WHERE Module_SN = '{pcbaSN}' "
            executeOne(q)
    else:
        q = f"UPDATE Module set Config_PF = '{pass_fail}',Config_ID = '{pcbid}' WHERE PCB_SN = '{pcbaSN}' "
        executeOne(q)


def wamAss(oldModSN):
    dc = datetime.now().strftime('%y%m')
    prefix = 'RA' + dc
    
    label = {}
    
    q = f"SELECT MAX(date_time) from tetra_assembly WHERE module_serial_number = '{oldModSN}'"
    #print(q)
    ans = executeOne(q)
    curtime = ans[0][0]
    label['DateCode'] = ans[0][0].strftime("%y%W")
        
    prefix = 'RA' + ans[0][0].strftime('%y%m')
    #print('hello')
    #print(oldModSN)
    q = f"SELECT PCB_SN,Config_PF from Module where Module_SN = '{oldModSN}'"
    ans = executeOne(q)
    pcbaSN = ans[0][0]
    configpf = ans[0][1]
    #print('hello1')
    q = f"SELECT MAX(Module_SN) FROM Module Where not Module_SN Like ('%WAM%') and Module_SN like ('%{prefix}%')"
    ans = executeOne(q)
    prevSN = ans[0][0]
    #print('hello2')
    #check if module has already been programmed before
    try:
        q = f"SELECT id,Module_SN from Module where PCB_SN = '{pcbaSN}'"
        ans = executeOne(q)
        existingid = ans[0][0]
        existingModSN = ans[0][1]
    except Exception as ex:
        existingid = -1
        existingModSN = -1
        print(ex)
        
    print(existingid)
    print(existingModSN)
    #we have to update module SN if they are in the old format 
    if (not existingid == -1) or (not str(existingModSN).find("WAM") == -1):
        if (prevSN):
            count = ''.join(c for c in prevSN if c.isdigit())
            count = str(count)[4:]
            count = int(count) + 1 
            
        else:
            count = 1
            
        count = str(count).zfill(4)
        modSN = prefix + str(count)
        
        q= f"SELECT id FROM tetra_configuration WHERE pcba_serial_number = '{pcbaSN}' ORDER BY date_time DESC LIMIT 1;"
        ans = executeOne(q)
        pcbid = ans[0][0]
    
        if str(existingModSN).find("WAM") == -1:
            try:
                q = f"INSERT INTO Module (PCB_SN,Module_SN,Config_PF,Config_ID) VALUES ('{pcbaSN}','{modSN}','{configpf}','{pcbid}')"
                executeOne(q)
                print(q)
            except Exception as exp:
                print(exp)
        else:
            try:
                q = f"UPDATE Module SET Config_ID = '{pcbid}',Config_PF ='{configpf}', Module_SN = '{modSN}' WHERE id = '{existingid}'"
                executeOne(q)
                print(q)
            except Exception as exp:
                print(exp)

    else:
        try:
            q = f"UPDATE Module SET Config_ID = '{pcbid}',Config_PF ='{configpf}' WHERE id = '{existingid}'"
            executeOne(q)
        except Exception as exp:
            print(exp)
    #print(q)
    q = f"SELECT Module_SN from Module where PCB_SN = '{pcbaSN}'"
    ans = executeOne(q)
    label['SerialNumber'] = ans[0][0]
    #print(label['SerialNumber'])

    
    return(label)

def wamProg(sn):
    label = {}
    q = f"SELECT MAX(date_time) from tetra_configuration WHERE pcba_serial_number = '{sn}'"
    #print(q)
    ans = executeOne(q)
    curtime = ans[0][0]
    label['DateCode'] = ans[0][0].strftime("%y%W")
    prefix = 'RA' + ans[0][0].strftime('%y%m')
    
    prevSN = None
    q = f"SELECT MAX(Module_SN) FROM Module Where not Module_SN Like ('%WAM%') and Module_SN like ('%{prefix}%')"
    ans = executeOne(q)
    prevSN = ans[0][0]
    
    if not prevSN:
        count = 1
    else:
        count = ''.join(c for c in prevSN if c.isdigit())
        count = str(count)[4:]
        count = int(count) + 1 
        
    count = str(count).zfill(4)
    modSN = prefix + str(count)

    q = f"UPDATE Module SET Module_SN = '{modSN}' WHERE PCB_SN = '{sn}'"
    executeOne(q)
    
    label['SerialNumber'] = modSN
    return(label)
    
def setWam(SN):
    label = {}
    q = f"SELECT PCB_SN from Module where Module_SN = '{SN}'"
    ans = executeOne(q)
    print(SN)
    print(ans)
    pcbaSN = ans[0][0]
    
    q = f"SELECT MAX(date_time) from tetra_assembly WHERE module_serial_number = '{SN}'"
    #print(q)
    ans = executeOne(q)
    curtime = ans[0][0]
    label['DateCode'] = ans[0][0].strftime("%y%W")
    
    modsn = 'RA2211' + pcbaSN
    print(modsn)
    q = f"UPDATE Module SET Module_SN = '{modsn}' WHERE PCB_SN = '{pcbaSN}'"
    executeOne(q)
    
    label['SerialNumber'] = modsn
    return(label)
    
def getModSn(pcbaSN):
    q = f"SELECT Module_SN from Module where PCB_SN = '{pcbaSN}'"
    ans = executeOne(q)
    return(ans[0][0])
    
def ModulepostAss(modsn,pass_fail):
    id = getAssyId(modsn)
    q = f"UPDATE Module SET Asy_ID = '{id}',Asy_PF ='{pass_fail}' WHERE Module_SN = '{modsn}'"
    executeOne(q)
    
def ModulepostBurn(modsn,lotid,pass_fail):
    q = f"UPDATE Module SET BurnLot_ID = '{lotid}',BurnLot_PF = '{pass_fail}' WHERE Module_SN = '{modsn}'"
    executeOne(q)

def CheckModule(modsn,step):
    if(step == "Assembly"):
        try:
            q = f"SELECT UPPER(Config_PF) from Module where Module_SN = '{modsn}'"
            ans = executeOne(q)[0][0]
            if(ans == "PASS"):
                return(True,1)
            elif(ans == "FAIL"):
                return(False,1)
            else:
                return(False,0)
        except:
            pass
    elif(step == "BurnIn"):
        try:
            q = f"SELECT UPPER(Asy_PF) from Module where Module_SN = '{modsn}'"
            ans = cursor.executeOne()[0][0]
            if (ans == "FAIL" or ans == "NULL" or ans == None):
                check1 = False
            else:
                check1 = True
            q = f"SELECT UPPER(Config_PF) from Module where Module_SN = '{modsn}'"
            ans = cursor.executeOne()[0][0]
            if (ans == "FAIL" or ans == "NULL" or ans == None or check1 == False):
                return(False,1)
            return(True,1)
        except:
            return(False,0)
def checkDatabaseStat():
    cnx = connect()
    stat = cnx.ping(reconnect=False, attempts=1, delay=0)
    cnx.close()
    return(stat)
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    getPassword()
    ModulepostConfig('test','PASS')
    
   
