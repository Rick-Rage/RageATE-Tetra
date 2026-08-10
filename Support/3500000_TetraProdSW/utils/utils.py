from __future__ import division, print_function, absolute_import, unicode_literals
from playsound import playsound
import sys
import time
import os
import re
import openpyxl
from datetime import datetime
import ctypes
import shutil
import math
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import*
import serial
import prog_e3644a
import prog_Sorensen
import pyvisa
import time
import os
import cv2
import subprocess as sp
from RageComm import RageComm
from git import Repo
import SqlFuncs
import VerifySiTime

def SilentPrint(pdf,printer):
    # acroread = r'C:\Program Files (x86)\Adobe\Reader 11.0\Reader\AcroRd32.exe'
    acrobat = r'C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe'

    # '"%s"'is to wrap double quotes around paths
    # as subprocess will use list2cmdline internally if we pass it a list
    # which escapes double quotes and Adobe Reader doesn't like that

    cmd = '"{}" /N /T "{}" "{}"'.format(acrobat, pdf, printer)

    proc = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc.communicate()
    exit_code = proc.wait()


def gitRevText(gitRepoPath):
    repo = Repo(gitRepoPath)

    tagName = ''
    for tag in repo.tags:
        if tag.commit == repo.head.ref.commit:
            tagName = str(tag)
            if tagName.startswith('Rev'):
                tagName = tagName[3:]
            break

    if not tagName:
        tagName = str(repo.head.ref.commit)
        tagName = tagName[:8]

    if repo.is_dirty():
        tagName += "-dirty!"
    return tagName
    return "bob"

def getCodeRev():
    return("Rev: " + gitRevText('..'))

def OpenPdf(file_name,root):
    v1=None
    v2 = None

    pdfwindow = Toplevel(root)

    pdfwindow.geometry("750x750")

    v1 = pdf.ShowPdf()

    v2 = v1.pdf_view(pdfwindow,
                pdf_location = file_name,
                width = 150, height = 1000)
    v2.pack()
    LOOP_ACTIVE = True

    while LOOP_ACTIVE:
        root.update()
        USER_INPUT = raw_input("Give me your command! Just type \"exit\" to close: ")
        if USER_INPUT == "exit":
            ROOT.quit()
            LOOP_ACTIVE = False
        else:
            LABEL = Label(ROOT, text=USER_INPUT)
            LABEL.pack()


def ReadIni(path):
    ini = {}
    a = {}
    folder = ''
    with open(path, "r") as fp:
        for line in fp:
            if ';' in line:
                fields = line.split(';')
                line = fields[0]
            line = line.strip()
            if len(line) == 0:
                continue
            if line[0] == '[':
                if line[-1] == ']':
                    if len(a) > 0:
                        ini[folder] = a
                        a = {}
                    folder = line[1:-1]
            elif '=' in line:
                fields = line.split('=')
                key = fields[0].strip()
                value = fields[1].strip()
                a[key] = value
    if len(a) > 0:
        ini[folder] = a
        a = {}
    return ini

def ParseDuration(duration):
    fields = duration.split(':')
    hours = 0
    minutes = 0
    seconds = 0
    seconds = int(fields.pop())
    if len(fields) > 0:
        minutes = int(fields.pop())
    if len(fields) > 0:
        hours = int(fields[0])
    return hours*3600+minutes*60+seconds

def RunCancelDialog():
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Do you want to cancel the test and lose your data?")
    msgBox.setWindowTitle("Restart Test")
    msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

    returnValue = msgBox.exec()
    if returnValue == 65536:
        return False
    # TBD
    # Create a dialog which asks "Test is not finished.  Do you want to lose test data?"
    return True


def wait(com):
    com.consoleIo('')


def GetEsn(com):
    resp = com.consoleIo('esn')
    resp = com.consoleIo('esn')

    family = resp.split('\n')[0].split(':')
    ser = resp.split('\n')[1].split(':')
    return {str(family[0]):family[1],str(ser[0]):ser[1]}

def GetRdv(com):

    rdv = {}
    resp =  com.consoleIo('rdv')
    # 0)  isu18p5: 17495 mV
    # 1)  core1p0: 1026 mV
    # 2)   xvr1p0: 1022 mV
    # 3)   dig1p8: 1801 mV
    # 4)   dig3p3: 3270 mV
    # 5)   xvr1p2: 1233 mV
    # 6)   div5p0: 4988 mV
    # 7)   vdd3p3: 3287 mV
    # 8)    rx2p5: 357 mV
    # 9)    tx2p5: 1128 mV
    # 10)   adc1p8: 70 mV

    resp = resp.split('\n')
    for line in resp:
        fields = line.split()
        rdv[str(fields[1][:-1])] = int(fields[2])
    return rdv
 
def GetAdc(com):
    rdv = {}
    resp =  com.consoleIo('adcsync')
    resp = resp.split('\n')
    return resp[0]
    
def getcaladc(com):
    rdv = {}
    resp =  com.consoleIo('caladc -s')
    resp = resp.split('\n')
    return (resp[0])

def selfTest(com):
    st = {}

    ans = com.consoleIo('selftest')
    resp = ans.split('\n')

    #isolate the passfail line
    for line in resp:
        fields = line.split()
        st[str(fields[0])] = str(fields[-1])

    return(st)

def GetRev(com):
    rev = {}
    resp = com.consoleIo('rev')
    # rev
    # SW Version 02001004 Rev 2.1.4
    # SW GitHash CAA762AE
    # SW Date    20220808
    # FW Version 0200030F Rev 2.0.3 HW Rev 15
    # FW GitHash A4CE1135
    # FW Date    20220708
    # PMIC Rev   1.1

    resp = resp.split('\n')
    for line in resp:
        fields = line.split()
        name = str(fields[0])+str(fields[1])
        version = fields[2]
        if len(fields) > 3:
            if name == "SWVersion":
                version = fields[4]
            elif name == "FWVersion":
                version = fields[4]
                rev['HWRev'] = fields[7]
        rev[name] = version
    return rev

def GetRdiv(com):
    rdiv = {}
    resp = com.consoleIo('rdiv')

    resp = resp.split('\n')
    for line in resp:
        fields = line.split()
        rdiv[str(fields[1][:-1])] = {'mA': int(fields[2]), 'mV': int(fields[4])}
    return rdiv
    
def siTime():
    return(VerifySiTime.main( ['RATest','C:\\3500000_TetraProdSW\\utils']))

def UpdateIv(iv, ini, meas):
    ok = True
    report = ''
    for supply in iv.keys():
        lim = ini['rdiv_limits'][supply].split(',')
        lim = [a.strip() for a in lim]
        offset = 0
        for param in ['mA', 'mV']:
            value = meas[supply][param]
            iv[supply][param]['Value'] = value
            lo = int(lim[offset])
            hi = int(lim[offset+1])
            iv[supply][param]['Low'] = lo
            iv[supply][param]['High'] = hi
            okSupply = value >= lo and value <= hi
            iv[supply][param]['Ok'] = okSupply
            offset += 2
            ok = ok and okSupply
            line = (str(supply) + ' ' + str(param) + ' ' + str(iv[supply][param]))
            report = report + line  +'\n'
    return ok,report


def UpdateV(v, ini, meas):
    ok = True
    report = ''
    for supply in v.keys():
        lim = ini['rdv_limits'][supply].split(',')
        lim = [a.strip() for a in lim]
        value = meas[supply]
        v[supply]['Value'] = value
        lo = int(lim[0])
        hi = int(lim[1])
        v[supply]['Low'] = lo
        v[supply]['High'] = hi
        okSupply = value >= lo and value <= hi
        v[supply]['Ok'] = okSupply
        line = (str(supply) + ' ' + str(v[supply]))
        report = report + line  +'\n'
    return ok,report

def GetPcbInfo(port):
     PCBA = []
     window = sg.Window("Enter PCBA INFO",layoutPCBA)
     while True:
         event,values = window.read()
         if event == sg.WIN_CLOSED:
             break
         if event == "OK" or event == "Submit":
            window.close()
            values = list(values.values())
            values = values[0].split(',')
            return values[0],values[1],values[2]

def ErrorMsg(info):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Error")
    msg.setInformativeText(info)
    msg.setWindowTitle("Error")
    msg.exec_()

def WarningMsg(info):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText("Warning")
    msg.setInformativeText(info)
    msg.setWindowTitle("Warning")
    msg.exec_()

def TurnOnPowerSupply(inst,voltage, current):
    # Connect to the power supply, set the voltage and the current max and turn
    # on the supply
    ISupplySet = 2#amps
    configTime = 7
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource(inst)
    prog_e3644a.reset(inst)
    prog_e3644a.SetV(inst,voltage)
    prog_e3644a.SetILim(inst,current)
    prog_e3644a.PowerOn(inst)
    # Read the voltage and current from the supply and check over-current
    ReadDisplay = prog_e3644a.readDisplay(inst)
    meas_voltage = ReadDisplay[0]
    meas_current =  ReadDisplay[1]
    # if (meas_voltage >= vll) or (meas_voltage <= vul):
    #     errMsg = f'Measurement voltage is not within the specify range of {vll} -> {vul}'
    # elif(meas_voltage >= ill) or (meas_voltage <= iul):
    #     errMsg = f'Measurement Current is not within the specify range of {ill} -> {iul}'
    # else:
    errMsg = ''
    # Disconnect from the supply
    pass # TBD
    return errMsg, meas_voltage, meas_current

def TurnOffPowerSupply(inst):
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource(inst)
    # TBD
    # Connect to the power supply and turn it off
    prog_e3644a.PowerOff(inst)
    # Disconnect from the supply
    # time.sleep(0.5)
    ok = True
    errMsg = ''
    return ok, errMsg
    
def incVoltageBurn(inst):
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource(inst)
    prog_Sorensen.SetV(inst,prog_Sorensen.getVolt(inst) + .01)

def TurnOnPowerSupplyBurn(inst,voltage, current,OVolt):
    # Connect to the power supply, set the voltage and the current max and turn
    # on the supply
    ISupplySet = 2#amps
    configTime = 7
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource(inst)
    prog_Sorensen.reset(inst)
    #prog_Sorensen.OVSet(inst,OVolt)
    prog_Sorensen.UnMask(inst)
    prog_Sorensen.SQR(inst)
    prog_Sorensen.SetV(inst,voltage)
    prog_Sorensen.SetILim(inst,current)
    prog_Sorensen.PowerOn(inst)
    print(prog_Sorensen.Fault(inst))
    # Read the voltage and current from the supply and check over-current
    ReadDisplay = prog_Sorensen.readDisplay(inst)

    meas_voltage = ReadDisplay[0]
    meas_current =  ReadDisplay[1]
    # if (meas_voltage >= vll) or (meas_voltage <= vul):
    #     errMsg = f'Measurement voltage is not within the specify range of {vll} -> {vul}'
    # elif(meas_voltage >= ill) or (meas_voltage <= iul):
    #     errMsg = f'Measurement Current is not within the specify range of {ill} -> {iul}'
    # else:
    errMsg = ''
    # Disconnect from the supply
    pass # TBD
    return errMsg, meas_voltage, meas_current
    
def setCurrent(inst,curr):
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource(inst)
    prog_Sorensen.SetILim(inst,curr)


def CheckPowerSupplyBurn(inst):
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource(inst)
    
    volt,curr,pow = prog_Sorensen.readDisplay(inst)
    fault = prog_Sorensen.Fault(inst)
    print(fault)
    ok = True
    errMsg = ''
    return(volt,curr,pow,fault)

def TurnOffPowerSupplyBurn(inst):
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource(inst)
    # TBD
    # Connect to the power supply and turn it off
    prog_Sorensen.PowerOff(inst)
    # Disconnect from the supply
    # time.sleep(0.5)
    ok = True
    errMsg = ''
    return ok, errMsg

def ConvertPcba2AssyNumber(pcba):
    try:
        # Older versions of the PCBA SN had 'SN' or 'TA' before the numer
        # Use re to get the digits at the end of the PCBA SN
        m = re.search('([0-9]+)$', pcba)
        # Convert the PCBA serial number to an assembly serial number
        # Insert 'WAM-000' at the beginning of the number
        pcba = m.group(0).zfill(6)
        assy = 'WAM-' + pcba
        return assy
    except:
        return None

def getDateCode():
     now = datetime.now() # current date and time
     datecode = now.strftime("%y%W")
     return(datecode)

def MakeTestFolder(base, testName):
    dirName = os.path.join(base, testName)
    try:
        os.mkdir(dirName)
    finally:
        return dirName

def GetDateTime():
    now = datetime.now()
    return now.strftime("%Y%m%d_%H%M%S")

def CopyFiles(srcPath, dstPath):
    for filename in os.listdir(srcPath):
        filename = os.path.join(srcPath, filename)
        shutil.copy2(filename, dstPath)


MBOX_STYLE_OK = 0
MBOX_STYLE_OK_CANCEL = 1
MBOX_STYLE_ABORT_RETRY_IGNORE = 2
MBOX_STYLE_YES_NO_CANCEL = 3
MBOX_STYLE_YES_NO = 4
MBOX_STYLE_RETRY_CANCEL = 5
MBOX_STYLE_CANCEL_TRY_AGAIN_CONTINUE = 6
MBOX_OK = 1
MBOX_CANCEL = 2
MBOX_ABORT = 3
MBOX_RETRY = 4
MBOX_IGNORE = 5
MBOX_YES = 6
MBOX_NO = 7
MBOX_TRY_AGAIN = 10
MBOX_CONTINUE = 11

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def testFiles():
    dt = GetDateTime()
    loc = MakeTestFolder('local_files', 'broadway', dt)
    for i in range(0,10):
        with open(os.path.join(loc, f"tmp{i}.txt"), "w"):
            pass
    rem = MakeTestFolder('remote_files', 'broadway', dt)
    CopyFiles(loc, rem)

class PictureWindow(QDialog):
    def __init__(self,parent=None,path = None, name = None):
        super(PictureWindow,self).__init__(parent)
        self.title='Picture Check: ' + name
        self.left=10
        self.top=70
        self.width=640
        self.height=480
        self.path = path
        self.accept_reject = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        label=QLabel(self)

        pixmap=QPixmap(self.path)
        label.setPixmap(pixmap)

        discardButton = QPushButton(self.tr("&Retake"))
        discardButton.setDefault(True)

        self.resize(pixmap.width(),pixmap.height()+30)

        self.button_box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Save,
            QtCore.Qt.Horizontal,
            self
        )
        self.button_box.addButton(discardButton,QDialogButtonBox.RejectRole)
        self.button_box.move(0,pixmap.height())
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.show()


def TakePicture(parent, name, serialNumber, timeStamp):
    while True:
        #Takes a picture then prompts the user to see if the picture is good
        path = parent.imagePath
        ret,frame = parent.cap.read()
        playsound("../utils/shutter.wav",False)
        path = os.path.join(path, serialNumber + '-' + timeStamp + '-' + name + '.png')
        try:
            cv2.imwrite(path, frame)
            #creates a PyQT5 window to show picture
            picture = PictureWindow(parent=parent,path = path, name=name)
            picture.setWindowModality(QtCore.Qt.ApplicationModal)
        except:
            ErrorMsg("Could not take picture")
            parent.cap = cv2.VideoCapture(0)
            continue
        if (picture.exec_() == QtWidgets.QDialog.Accepted):
            break
    return True

def parseTechnicianId(scannerText):
    #005, CHARLIE AUWERDA, LWL
    try:
        fields = [field.strip() for field in scannerText.split(",")]
        location = fields[2].upper()
        if(len(fields) != 3 or (location != "LWL" and location != "NBPT")):
            utils.ErrorMsg("Not a Valid employee ID")
            return None,''
        return int(fields[0]), fields[1]
    except:
        return None,''
        
def roundup(x):
    return int(math.ceil(float(x) / 100.0)) * 100
    
def writeNCRlog(reason,sn,date,comment,path):
    wb = openpyxl.load_workbook("C:\\Users\\CharlieAuwerda\\Rage Systems\\Manufacturing - Documents\\MRB\\test.xlsx")
    sheet = wb.active
    #Case	Case Type	Date	Item_Number	Qty_Affected	Serial Number(s)	RaGE_PO	Vendor	Vendor_RMA	RaGE RMA	Reason for fail     Reason for Return	Comment
    data = ("","",date,"5083561","",sn,"","","","","",reason,path,"",comment)
    sheet.append(data)
    wb.save("C:\\Users\\CharlieAuwerda\\Rage Systems\\Manufacturing - Documents\\MRB\\test.xlsx")
    
def parseModuleLabel(scannerText):
    label = {}
    print(scannerText)
    #TA22280102,0x00003609B5D6,2232,C.05, Wideband Antenna Module,5083561, RaGE Systems, www.ragesystems.com
    if scannerText.find("WAM") == -1:
        if not scannerText.find("RA") == -1:
            label['SerialNumber'] = scannerText
            label['DateCode'] = scannerText[2:6]
            label['Revision'] = SqlFuncs.GetRev(scannerText)
            label['ESN'] = SqlFuncs.getEsn(SqlFuncs.getconfigidfromMod(scannerText))
            return(label)
        else:
            scannerText = SqlFuncs.getModSn(scannerText)
            label['SerialNumber'] = scannerText
            label['DateCode'] = scannerText[2:6]
            label['Revision'] = SqlFuncs.GetRev(scannerText)
            label['ESN'] = SqlFuncs.getEsn(SqlFuncs.getconfigidfromMod(scannerText))
            return label
    else:
        fields = [field.strip() for field in scannerText.split(",")]
        label = {}
        label['SerialNumber'] = fields[0]
        label = SqlFuncs.setWam(label['SerialNumber'])
        print(label)
        return label

if __name__ == '__main__':
    print(siTime())
   