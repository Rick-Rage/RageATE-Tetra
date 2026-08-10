#desciption
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import csv
import sys
import os
import time
import cv2
import glob
import datetime
import pathlib
import win32com.client as win32
from pdf2image import convert_from_path

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

sys.path.append('../utils')
import utils
import SqlFuncs
from RageComm import RageComm

# minute in miliseconds for timer
MINUTE = 60000


app = None

#Worker class runs on a different thread connected to the main window using pyqt5 slots and signals
class Worker(QObject):
    finished = pyqtSignal()
    updateText = pyqtSignal(str)
    updateProgressBar = pyqtSignal(int)
    updatePASSFAIL = pyqtSignal(str)
    esnRead = pyqtSignal(str)
    voltcurr = pyqtSignal(float,float,int)
    readmodule = pyqtSignal(dict,dict,dict,dict,str,str,str)
    failtext = pyqtSignal(str)

    def __init__(self,ini,reportfile):
        super(Worker, self).__init__()
        self.ini = ini
        #keeps track of where we are in terms of powersupply cycles
        self.voltStage = 0
        self.log = reportfile

    def runTest(self):

        self.passFail = "PASS"
        self.testid = SqlFuncs.getConfigId()

        #I mean don't run the functions if one fails thats what we call in the buiz a waste of time
        dutData = []
        for st in range(0,6):
            if st == 0:
                self.updateText.emit("Turning On Supply...")
                try:
                    self.turnOnSupply()
                    self.updateProgressBar.emit(10)
                except:
                    self.passFail = "FAIL"
                    
            elif st == 1:
                self.updateText.emit("Programing Pic...")
                try:
                    self.passFail = self.programPic()
                    self.updateProgressBar.emit(23)
                except:
                    self.failtext.emit("PIC failed to program")
                    self.passFail = "FAIL"
                

            elif st == 2:
                self.updateText.emit("Cycling Power Supply...")
                try:
                    ok = self.cycleSupply()
                    self.updateProgressBar.emit(25)
                except:
                    utils.ErrorMsg("Could not turn on power Supply")
                    self.passFail = "FAIL"
                

            elif st == 3:
                self.updateText.emit("Programming FPGA...")
                try:
                    self.passfail,ok = self.programFpga()
                    self.updateProgressBar.emit(29)
                except:
                    self.failtext.emit("FPGA failed to program")
                    self.passFail = "FAIL"

            elif st == 4:
                self.updateText.emit("Cycling Power Supply...")
                try:
                    ok = self.cycleSupply()
                    self.updateProgressBar.emit(11)
                except:
                    utils.ErrorMsg("Could not turn on power Supply")
                    self.passFail = "FAIL"

            elif st == 5:
                self.updateText.emit("Reading DUT Data...")
                try:
                    self.passFail,ok,dutData,failmsg = self.readDutData()
                except:
                    self.failtext.emit(failmsg)
                    self.passFail = "FAIL"
                if not ok:
                    self.failtext.emit(failmsg)
                    self.passFail = "FAIL"
                    
            if self.passFail == "PASS":
                self.updateText.emit("Done\n")
            else:
                self.updateText.emit("Failed\n")
                
                break
        
        self.updatePASSFAIL.emit(self.passFail)
        self.updateText.emit("Turning Off Supply...")
        self.turnOffSupply()
        self.updateProgressBar.emit(100)
        self.updateText.emit("Done\n")
        
        if self.passFail == "PASS":
            self.esnRead.emit(dutData)
        self.finished.emit()

    """Turns on the power supply"""
    def turnOnSupply(self):
        #port, voltage and current settings are in the ini
        ps_port = self.ini['config_power_supply']['port']
        ps_volt = float(self.ini['config_power_supply']['voltage'])
        ps_curr = float(self.ini['config_power_supply']['current'])

        errMsg,measVolt,measCurr = utils.TurnOnPowerSupply(ps_port, ps_volt, ps_curr)
        #sends the voltage and current readings to the main thread
        self.voltcurr.emit(measVolt,measCurr,self.voltStage)

        if errMsg:
            passFail = "FAIL"
        else:
            if (self.voltStage == 0):
                minCurr = float(self.ini['config_power_supply']['min_current_prePic'])
                maxCurr = float(self.ini['config_power_supply']['max_current_prePic'])

            elif (self.voltStage == 1):
                minCurr = float(self.ini['config_power_supply']['min_current_preFPGA'])
                maxCurr = float(self.ini['config_power_supply']['max_current_preFPGA'])

            elif (self.voltStage == 2):
                minCurr = float(self.ini['config_power_supply']['min_current_Final'])
                maxCurr = float(self.ini['config_power_supply']['max_current_Final'])

            # Verify limits
            
            minVolt = float(self.ini['config_power_supply']['min_voltage'])
            maxVolt = float(self.ini['config_power_supply']['max_voltage'])

            if measCurr > maxCurr:
                passFail = "FAIL"
            elif measCurr < minCurr:
                passFail = "FAIL"
            elif measVolt > maxVolt:
                passFail = "FAIL"
            elif measVolt < minVolt:
                passFail = "FAIL"
            else:
                passFail = "PASS"
        self.voltStage = self.voltStage+1
        # Display the status
        if(passFail == "FAIL"):
            self.updateText.emit("Current/Voltage readings not within range")
        return passFail

    """Programs the Pic"""
    def programPic(self):
            ok = False
            path = self.ini['pic']['path']
            tool = self.ini['pic']['tool']
            part = self.ini['pic']['part']
            errMsg,status = prog_pic(tool=tool, part=part, path=path,log = self.log)
            if status:
                ok = True
            else:
                utils.ErrorMsg(errMsg)
            # Display the final status
            if ok:
                passFail = "PASS"
            else:
                passFail = "FAIL"
            return passFail

    """turns the power supply off then on"""
    def cycleSupply(self):
            ok = self.turnOffSupply()
            time.sleep(1)
            if ok:
                ok = self.turnOnSupply()
            return ok

    """turns the power supply off"""
    def turnOffSupply(self):
            # Turn off the supply
            psPort = self.ini['config_power_supply']['port']
            ok = utils.TurnOffPowerSupply(psPort)
            if ok:
                passFail = "PASS"
            else:
                passFail = "FAIL"
            return passFail,ok

    """programs the FPGA

    Creates a log file in order to verify the FPGA was programmed sucsessfully
    """
    def programFpga(self):
        path = self.ini['fpga']['path']
        file = self.ini['fpga']['file']
        imagepath = os.path.join(os.getcwd(), 'pictures')

        flashlog = f'{imagepath}\\flashlog_{self.testid}.txt'

        flash_cmd = f"xsct {path} {file} >> {flashlog}"
        os.system(flash_cmd)
        ok = False
        with open(self.log,'a') as f:
            f.write("Log of FPGA Flashing: \n")
            with open(flashlog, 'r') as log:
                line = log.read()
                f.write(line)
                if 'Program/Verify Operation successful.' in line:
                    f.write('FPGA flashed Succesfully')
                    ok = True
                else:
                    err = "FPGA Failed to flash"
                    f.write(err)
               
                f.write("\n")
        # Display the final status
        if not ok:
            passFail = "FAIL"
        else:
            passFail = "PASS"
        return passFail,ok

    """conects to the board via serial

    reads all necessary data from the board
    emits data to the main thread
    """
    def readDutData(self):
        ok = True
        app.processEvents()
        # Open the serialport to the DUT and read the data back from the "esn",
        # "rev", "rdv" and "rdiv" commands
        com = RageComm(self.ini['Config']['port'])
        failmsg = com.boot()
        if failmsg == "Error: Neither '>' nor 'ADCSYNC FAILED' found in 30 seconds.":
            ok = False
            return "FAIL",ok,"FAIL",failmsg
        elif failmsg == "Error: '>' not found in 2 minutes after 'ADCSYNC FAILED'.":
            ok = False
            return "FAIL",ok,"FAIL",failmsg
            
        #let the board wake up while checking selftest
        time.sleep(5)
        st = None
        iv = None
        esn = None
        rev = None
        rdv = None
        adc = None
        caladc = None
        siTime = None
        res = "FAIL"
        try:
            st = utils.selfTest(com)
            if('FAILED' in st.values()):
                failmsg = "Failed self test"
                ok = False
                return "FAIL",ok,res,failmsg
        except:
            ok = False
            failmsg = "Could not read self test due to timeout"
            return "FAIL",ok,res,failmsg
            
        try:
            iv = utils.GetRdiv(com)
        except:
            ok = False
            failmsg = "Could not read Rdiv results due to timeout"
            return "FAIL",ok,res,failmsg
            
        try:
            esn = utils.GetEsn(com)
        except:
            ok = False
            failmsg = "Could not read esn due to timeout"
            return "FAIL",ok,res,failmsg
            
        try:
            rev = utils.GetRev(com)
        except:
            ok = False
            failmsg = "Could not read Rev due to timeout"
            return "FAIL",ok,res,failmsg
            
        try:
            rdv = utils.GetRdv(com)
        except:
            ok = False
            failmsg = "Could not read Rdv results due to timeout"
            return "FAIL",ok,res,failmsg
            
        try:
            adc = utils.GetAdc(com)
        except:
            ok = False
            failmsg = "Could not read adcsync test due to timeout"
            return "FAIL",ok,res,failmsg
            
        try:
            caladc = utils.getcaladc(com)
        except:
            ok = False
            failmsg = "Could not read caladc due to timeout"
            return "FAIL",ok,res,failmsg
        
           
        try:
            siTime = utils.siTime()
            print(siTime)
        except:
            ok = False
            failmsg = "Could not read SiTimeTest"
            return "FAIL",ok,res,failmsg    
            
        self.readmodule.emit(st,rdv,iv,rev,adc,caladc,siTime)
              
        esn = esn['Serial']
        fpgaFwRevision = rev['FWVersion']
        fpgaSwRevision = rev['SWVersion']
        HwRevision = rev['HWRev']
        pmicSwRevision = rev['PMICRev']
        errMsg = ''

        res = esn + " " + fpgaFwRevision + " " + fpgaSwRevision + " " + pmicSwRevision + " " + HwRevision
        #configure AM Module for rxdata transmission

        #end  AM config
        

        # Display the final status
        if not ok:
            passFail = "FAIL"
        else:
            passFail = "PASS"
        return passFail,ok,res,failmsg

"""MAIN WINDOW

Controls every aspect of the GUI
most variables are stored as class variables
creates a new thread when activley programming
"""
class MainWindow(QMainWindow):
    def __init__(self):
        SqlFuncs.getPassword()
        # Call the inherited classes __init__ method
        #os.chdir("InitialTestAndConfig")
        super(MainWindow, self).__init__()
        # Load the .ui file
        uic.loadUi(os.getcwd() +'\\InitialTestAndConfig.ui', self)
        self.centralwidget.setContentsMargins(20, 20, 20, 20)
        self.checkBoxCable.stateChanged.connect(self.checkBoxChangedAction)
        self.ini = utils.ReadIni('../utils/tetra.ini')
        self.scannerPort = self.ini['scanner']['port']
        
        self.techId = None

        self.editCompletionStatus.setText("")
        # Initialize the widget
        self.init()

        self.progressBar.setRange(0, 100)
        self.cap = cv2.VideoCapture(0)
        self.imagePath = os.path.join(os.getcwd(), 'pictures')
        if not os.path.isdir(self.imagePath):
            os.mkdir(self.imagePath)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timerEvent)
        
        
    def timerEvent(self):
        self.timer.stop()
        self.techId = None
        self.init()
        
    def init(self):
    
        if(self.techId):
            self.timer.start((2)*(MINUTE))
        else:
            self.editTechnician.setText("")
            
        self.failreason = None
        self.testid= SqlFuncs.getConfigId()
        self.passFailLabel.text()
        self.buttonBeginNewPcb.setEnabled(True)
        self.buttonProgram.setEnabled(False)
        self.buttonTakePcbaTopPicture.setEnabled(False)
        self.buttonTakePcbaBottomPicture.setEnabled(False)
        self.buttonDone.setEnabled(False)
        self.checkBoxCable.setEnabled(False)
        self.radioPass.setEnabled(False)
        self.radioFail.setEnabled(False)
        self.station_sw_revision = utils.gitRevText('..')
        self.Rev.setText("Rev: " + self.station_sw_revision)
        self.editPartNumber.setText("")
        self.editSerialNumber.setText("")
        self.editRevision.setText("")
        self.editProgramStatus.setText("")
        self.editNotes.setText("")
        self.log = None
        self.state = 'Ready'
        self.passFail = "PASS"
        self.passFailLabel.setText("")
        self.checkBoxCable.setChecked(False)
        self.radioFail.setChecked(False)
        self.radioPass.setChecked(False)
        self.checkReprogramAssembly.setChecked(False)
        color_effect = QGraphicsColorizeEffect()
        color_effect.setColor(Qt.black)
        self.passFailLabel.setGraphicsEffect(color_effect)
        self.progressBar.setValue(0)
        self.progressComplete = False
        self.SupervisorEnabled = False
        self.timestamp = None

        # Initialize the parameters
        self.nowDateTime = "N/A"
        
        self.techName = "N/A"
        self.pcbaPartNumber = "N/A"
        self.pcbaSerialNumber = "N/A"
        self.pcbaRevision = "N/A"
        self.fpgaFwRevision = "N/A"
        self.fpgaSwRevision = "N/A"
        self.HwRevision = "N/A"
        self.pmicSwRevision = "N/A"
        self.moduleSerialNumber = "N/A"
        self.modulePartNumber = "N/A"
        self.iv = "N/A"
        self.caladc = "N/A"
        self.esn = "N/A"
        self.rev = "N/A"
        self.buttonSupeMode.setText("Enter Supervisor Mode")
        self.rdv = "N/A"
        self.U56 = "N/A"
        self.U54 = "N/A"
        self.U55 = "N/A"
        self.U5  = "N/A"
        self.U20 = "N/A"
        self.U21 = "N/A"
        self.U5  = "N/A"
        self.U20 = "N/A"
        self.selftest = "N/A"
        self.adc = "N/A"
        self.siTime = "N/A"
        self.measCurrentPrePic = -1
        self.measCurrentPreFPGA = -1
        self.measCurrentFinal = -1
        self.measVoltagePrePic = -1
        self.measVoltagePreFPGA = -1
        self.measVoltageFinal = -1
        self.passFail = "PASS"
        self.programText = ''
        self.currentWidget = None
        self.Supe = False
        #initialized dict for checking that read values are within parameteres
        self.iv_info = {
            'sw3p6':  {'mA': {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False},
                       'mV': {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False}},
            'sw5p5':  {'mA': {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False},
                       'mV': {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False}},
            'sw2p8a': {'mA': {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False},
                       'mV': {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False}},
            'sw2p8b': {'mA': {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False},
                       'mV': {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False}},
            'sw2p4':  {'mA': {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False},
                       'mV': {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False}},
            'sw1p4':  {'mA': {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False},
                       'mV': {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False}}}
        self.v_info = {
            'isu18p5': {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False},
            'core1p0': {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False},
            'xvr1p0':  {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False},
            'dig1p8':  {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False},
            'dig3p3':  {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False},
            'xvr1p2':  {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False},
            'div5p0':  {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False},
            'vdd3p3':  {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False},
            'rx2p5':   {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False},
            'tx2p5':   {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False},
            'adc1p8':  {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False},
            'tx2p5':   {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False}}

    #enables supervisor mode which allows for the skipping of steps and what not
    @QtCore.pyqtSlot(name="on_buttonSupeMode_clicked")
    def clickSupeMode(self):
        if self.Supe == False:
            name, done1 = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Scan your badge:')
            parsed_name = name.split(",")
            loc = parsed_name[2].upper().strip()
            if (len(parsed_name) != 3 or (loc != "LWL" and loc != "NBPT")):
                utils.ErrorMsg("Not a Valid Technician")
                return
            try:
                name = SqlFuncs.checkSupe(parsed_name[0])
                if name == None:
                    raise
            except Exception as e:
                utils.ErrorMsg("ID not found in database - Please contact floor supervisor to recive permissions to use this GUI")
                return
            self.Supe = True
            self.buttonSupeMode.setText("Edit PASS/FAIL")
            self.buttonBeginNewPcb.setEnabled(True)
            self.buttonProgram.setEnabled(True)
            self.buttonTakePcbaTopPicture.setEnabled(True)
            self.buttonTakePcbaBottomPicture.setEnabled(True)
            self.buttonDone.setEnabled(True)
            self.checkBoxCable.setEnabled(True)
            self.SupervisorEnabled = True
            passfail = ["PASS","FAIL"]
            state, done1 = QtWidgets.QInputDialog.getItem(self, 'Input Dialog', 'PASS or FAIL module:',passfail)
            self.passFail= state
            self.updateLabel()
        else:
            passfail = ["PASS","FAIL"]
            state, done1 = QtWidgets.QInputDialog.getItem(self, 'Input Dialog', 'PASS or FAIL module:',passfail)
            self.passFail= state
            self.updateLabel()

    #takes a picture of the module and presents the picture to the user
    @QtCore.pyqtSlot(name="on_buttonTakePcbaTopPicture_clicked")
    def clickTakePcbaTopPicture(self):
        if(utils.TakePicture(self, f"pcbaTop_{self.testid}", self.pcbaSerialNumber,self.timestamp)):
            self.buttonTakePcbaTopPicture.setEnabled(False)
            if self.checkReprogramAssembly.isChecked():
                self.checkBoxCable.setEnabled(True)
                self.checkBoxCable.setFocus()
                self.currentWidget = "buttonProgram"
            else:
                self.buttonTakePcbaBottomPicture.setEnabled(True)
                self.buttonTakePcbaBottomPicture.setFocus()
                self.currentWidget = "buttonTakePcbaBottomPicture"

    @QtCore.pyqtSlot(name="on_buttonTakePcbaBottomPicture_clicked")
    def clickTakePcbaBottomPicture(self):
        if(utils.TakePicture(self, f"pcbaBottom_{self.testid}", self.pcbaSerialNumber,self.timestamp)):
            self.buttonTakePcbaBottomPicture.setEnabled(False)
            self.checkBoxCable.setEnabled(True)
            self.checkBoxCable.setFocus()
            self.currentWidget = "checkBoxCable"

    #keeps track of the cable check box
    @QtCore.pyqtSlot(name="on_checkBoxCable_stateChanged")
    def checkBoxChangedAction(self):
        if(self.checkBoxCable.isChecked() == True):
            self.checkBoxCable.setEnabled(False)
            self.buttonProgram.setEnabled(True)
            self.buttonProgram.setFocus()
            self.currentWidget = "buttonProgram"
        else:
            return

    #reads keypress events - allowing for user inputs with a check
    def keyPressEvent(self, e):
        #if key = 'enter'
        if e.key() == QtCore.Qt.Key_Enter - 1:
            if(str(self.currentWidget) == "editTechnician"):
                tid = self.editTechnician.text().upper()
                self.techId,self.techName = utils.parseTechnicianId(tid)
                if not self.techId:
                    utils.WarningMsg("Not a Valid Technician")
                    self.editTechnician.setText('')
                    return
                self.editTechnician.setText(self.techName)
                #keep track of widget for now
                self.currentWidget = "editPartNumber"
                #unlock next text box
                self.editTechnician.setReadOnly(True)
                #lock this text box now that data is correct
                self.editSerialNumber.setReadOnly(False)
                self.editSerialNumber.setFocus()

            elif(self.currentWidget == "editPartNumber"):
                self.pcbaSerialNumber = self.editSerialNumber.text()
                
                if self.checkReprogramAssembly.isChecked():
                    label = utils.parseModuleLabel(self.pcbaSerialNumber)
                    #print(label)
                    #checks to make sure The barcode is in the correct format - WAM-00109, C.01, 5083561, 0000f5f5aa55, Wideband Antenna Module, RaGE Systems
                    if(label == None):
                       utils.WarningMsg("Not a Valid Serial Number")
                       #if incorrect empty the text box
                       self.editSerialNumber.setText("")
                       return

                    self.moduleSerialNumber = label['SerialNumber']
                    pcb_id = SqlFuncs.getPCBIdfromAssy(self.moduleSerialNumber)
                    self.pcbaPartNumber, self.pcbaSerialNumber, self.pcbaRevision = SqlFuncs.lookupPcbConfigInfo(pcb_id)
                    
                else:
                    if(self.pcbaSerialNumber == 'test'):
                        print('nice')
                    elif(self.pcbaSerialNumber.find("RA") == -1 or not(len(self.pcbaSerialNumber) == 10)):
                        utils.WarningMsg("Not a Valid Serial Number")
                        self.editSerialNumber.setText('')
                        self.pcbaSerialNumber = None
                        return
                    
                self.pcbaPartNumber = self.ini['board']['pcbaPn']
                self.pcbaRevision = self.ini['board']['pcbaRev']
                
                self.editPartNumber.setText(self.pcbaPartNumber)
                self.editRevision.setText(self.pcbaRevision)
                self.editSerialNumber.setText(self.pcbaSerialNumber)
                
                self.editSerialNumber.setReadOnly(True)
                self.currentWidget = "Somthing Else"

                self.log = f"{self.imagePath}\{self.pcbaSerialNumber}_{self.timestamp}.txt"
                
                with open(self.log,'w') as f:
                    f.write("*************************************\n")
                    f.write(f"Log of {self.pcbaSerialNumber} at {self.timestamp}\n")
                    f.write(f"Tech:     {self.techName}\n")
                    f.write("*************************************\n\n")
                
                self.currentWidget = "Somthing Else"
                if self.checkReprogramAssembly.isChecked():
                    self.checkBoxCable.setEnabled(True)
                    self.checkBoxCable.setFocus()
                else:
                    self.radioFail.setEnabled(True)
                    self.radioPass.setEnabled(True)
                  

            elif(self.currentWidget=="Somthing Else"):
                pass

    @QtCore.pyqtSlot(name="on_radioFail_clicked")
    def clickradioFail(self):
        self.radioPass.setChecked(False)
        buttonReply = QMessageBox.warning(self, 'Confirmation', "Are you sure you want to Fail this unit", QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.radioPass.setEnabled(False)
            self.buttonBeginNewPcb.setEnabled(False)
            self.buttonProgram.setEnabled(False)
            self.buttonTakePcbaTopPicture.setEnabled(False)
            self.buttonTakePcbaBottomPicture.setEnabled(False)
            self.checkBoxCable.setEnabled(False)
            self.radioPass.setEnabled(False)
            self.radioFail.setEnabled(False)
            self.radioPass.setEnabled(False)
            self.buttonDone.setEnabled(True)
            self.passFail = "FAIL"
            self.editNotes.setText("FAILED ON VISUAL INSPECTION\n")
        else:
            self.radioFail.setChecked(False)

    @QtCore.pyqtSlot(name="on_radioPass_clicked")
    def clickradioPass(self):
        self.passFail = "PASS"
        self.buttonTakePcbaTopPicture.setEnabled(True)
  
        
    @QtCore.pyqtSlot(name="on_buttonBeginNewPcb_clicked")
    def clickBeginNewPcb(self):
        self.timer.stop()
        self.timestamp = SqlFuncs.nowDateTime()
        self.timestamp = SqlFuncs.datetimeToTimeStamp(self.timestamp)

        if self.state != 'Ready':
            doCancel = utils.RunCancelDialog()
            if doCancel:
                self.init()
                self.timer.stop()
            else:
                return

        self.state = 'Running'
        self.editCompletionStatus.setText("")
        if not self.cap.isOpened():
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                utils.ErrorMsg("No camera detected - please make sure the camera is connected")
                return

        self.nowDateTime = SqlFuncs.nowDateTime()
        app.processEvents()

        # Delete any files that are in the image directory
        files = glob.glob(self.imagePath + "\\*")
        for file in files:
            os.remove(file)

        if(self.techId):
            self.currentWidget = "editPartNumber"
            self.editSerialNumber.setReadOnly(False)
            self.editSerialNumber.setFocus()
        else:
            self.editTechnician.setReadOnly(False)
            self.currentWidget = "editTechnician"
            self.editTechnician.setFocus()

    def updateString(self, update):
        self.programText += update
        self.editProgramStatus.setText(self.programText)
        app.processEvents()

    def updateProg(self,amount):
        i=self.progressBar.value()
        amount = amount+i
        if amount > 100:
            amount = 100
        while(i<=amount):
            if self.progressComplete:
                self.progressBar.setValue(100)
                break
            self.progressBar.setValue(i)
            app.processEvents()
            time.sleep(0.2)
            i=i+1

    def updatePASSFAIL(self, state):
        if self.passFail == "PASS":
            # Never change from FAIL to PASS
            self.passFail = state

    #a little thread action using pyqt5's slots and signals
    @QtCore.pyqtSlot(name="on_buttonProgram_clicked")
    def clickProgram(self):
        
        self.buttonProgram.setEnabled(False)
        #t1=threading.Thread(target = self.runTest)
        #t1.start(
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker(self.ini,self.log)
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots

        self.thread.started.connect(self.worker.runTest)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(self.programmingDone)
        self.worker.updateText.connect(self.updateString)
        self.worker.updateProgressBar.connect(self.updateProg)
        self.worker.esnRead.connect(self.DUTread)
        self.worker.voltcurr.connect(self.voltcurr)
        self.worker.readmodule.connect(self.readmodule)
        self.worker.updatePASSFAIL.connect(self.updatePASSFAIL)
        self.worker.failtext.connect(self.failtext)
        # Step 6: Start the thread
        self.thread.start()

    def failtext(self,reason):
        utils.ErrorMsg(reason)
        self.failreason = reason
        self.editNotes.setText(f'{reason}\n')
        
        
    def voltcurr(self,volt,cur,i):
        with open(self.log, 'a') as f:
            if(i == 0):
                f.write("Pwer Supply readings at startup:\n")
                self.measCurrentPrePic = cur
                self.measVoltagePrePic = volt
            elif(i==1):
                f.write("Powersupply Readings after programmingPic:\n")
                self.measVoltagePreFPGA = volt
                self.measCurrentPreFPGA = cur
            else:
                f.write("Powersupply Readings after flashing FPGA:\n")
                self.measVoltageFinal = volt
                self.measCurrentFinal = cur
            f.write(f"Current:  {cur}mA\n")
            f.write(f"Voltage:  {volt}V\n")

    #reads and parses data provided by the module - also checks these readings against parameters
    def readmodule(self,st,meas_v,meas_iv,rev,adc,caladc,siTime):
        self.U56 = st['U56']
        self.U54 = st['U54']
        self.U55 = st['U55']
        self.U5  = st['U5']
        self.U20 = st['U20']
        self.U21 = st['U21']
        self.U5  = st['U5']
        self.U20 = st['U20']
        self.selftest = st['Test:']
        self.adc = adc[8:]
        self.caladc = caladc
        self.siTime = siTime
        #creates a log file in the image path becuase the folder as a whole gets moved to the synology srive
        if not self.failreason:
            self.failreason = ""

        #creates the report with a note of which readings are out of parameters if any
        with open(self.log, 'a') as f:
            f.write(SqlFuncs.nowDateTime() + " " + self.pcbaSerialNumber)
            f.write('\n')
            f.write(caladc)
            f.write('\n')
            f.write(adc)
            f.write('\n')
            f.write('selfTest:')
            f.write(str(st))
            f.write('\n')
            ok1,report = utils.UpdateIv(self.iv_info, self.ini, meas_iv)
            if not ok1:
                
                for supply in self.iv_info.keys():
                    for param in ['mA', 'mV']:
                        if not self.iv_info[supply][param]['Ok']:
                            v = self.iv_info[supply][param]['Value']
                            lo = self.iv_info[supply][param]['Low']
                            hi = self.iv_info[supply][param]['High']
                            txt = f"\nSupply {supply}: {v} {param} out of range {lo} to {hi} {param} "
                            self.failreason += txt
                            self.editNotes.setText(f'{self.failreason}\n')
                            self.programText += txt
            f.write(report)
            

            ok2,report = utils.UpdateV(self.v_info, self.ini, meas_v)
            if not ok2:
                for supply in self.v_info.keys():
                    if not self.v_info[supply]['Ok']:
                        v = self.v_info[supply]['Value']
                        lo = self.v_info[supply]['Low']
                        hi = self.v_info[supply]['High']
                        txt = f"Supply {supply}: {v} {param} out of range {lo} to {hi} {param}"
                        self.failreason += txt
                        self.editNotes.setText(f'{reason}\n')
                        self.programText += txt
            f.write(report)

            #checks to make sure all code versions are correct the current version is stored in the ini file
            ok3 = True
            if rev['SWVersion'] != self.ini['fpga']['rev']:
                txt = f"\nFPGA version {rev['SWVersion']} is incorrect,  should be {self.ini['fpga']['rev']} "
                self.programText += txt
                ok3 = False
            if rev['HWRev'] != self.ini['fpga']['hwrev']:
                txt = f"\nHW version {rev['HWRev']} is incorrect,  should be {self.ini['fpga']['hwrev']} "
                self.programText += txt
                ok3 = False
            if rev['PMICRev'] != self.ini['pic']['rev']:
                txt = f"\nPIC version {rev['PMICRev']} is incorrect,  should be {self.ini['pic']['rev']} "
                self.programText += txt
                ok3 = False

            f.write(self.programText)
            f.write("\n")
            
            if self.adc.find("PASSED") != -1:
                ok4 = True
                self.adc = "PASSED"
            else:
                ok4 = False
                self.programText += "ADC failed"
                self.adc = "FAILED"
                
            if self.caladc.find("mag: 2047 2047 2047 2047") == -1:
                ok5 = False
                self.programText += "Caladc failed"
                self.failreason = "Caladc failed"
                self.editNotes.setText(f'{self.failreason}\n')
                self.caladc = "FAIL"
            else:
                ok5 = True
                self.caladc = "PASS"
            
            if not self.siTime == "PASS":
                ok6 = False
                self.programText += "Register Test failed"
                self.failreason = "Register Test failed"
                self.editNotes.setText(f'{self.failreason}\n')
            else:
                ok6 = True

                
        if not ok1 or not ok2 or not ok3 or not ok4 or not ok5 or not ok6:
            self.editProgramStatus.setText(self.programText)
            app.processEvents()
            self.passFail = "FAIL"
            self.updateLabel()

    #stores the data read from the module in class variables
    def DUTread(self,lib):
        lib=lib.split()
        self.esn = lib[0]
        self.fpgaFwRevision = lib[1]
        self.fpgaSwRevision = lib[2]
        self.pmicSwRevision = lib[3]
        self.HwRevision = lib[4]

    #just updates the pass/fail on the GUI
    def updateLabel(self):
        if(self.passFail == "PASS"):
            color_effect = QGraphicsColorizeEffect()
            # setting color to color effect
            color_effect.setColor(Qt.darkGreen)
            self.passFailLabel.setGraphicsEffect(color_effect)
        else:
            color_effect = QGraphicsColorizeEffect()
            # setting color to color effect
            color_effect.setColor(Qt.darkRed)
            self.passFailLabel.setGraphicsEffect(color_effect)

        self.passFailLabel.setText(self.passFail)

    #enable the "done" button when the programming thread finishes executing
    def programmingDone(self):
        self.progressComplete = True
        self.buttonProgram.setEnabled(False)
        self.programText = ''
        # When programming is finished, enable the DONE button
        self.updateLabel()
        self.buttonDone.setEnabled(True)

    #makes the call to upload to database as well as resetting the GUI to get ready for the next module
    @QtCore.pyqtSlot(name="on_buttonDone_clicked")
    def clickDone(self):
        self.buttonDone.setEnabled(False)
        text = "Updating Database ..."
        self.editCompletionStatus.setText(text)
        app.processEvents()
        self.updateDatabase()
        
        text += " Done"
        self.editCompletionStatus.setText(text)
        self.init()

    #creates a dictonary that is passed to SqlFuncs to upload all the data to the database
    def updateDatabase(self):
        datecode = utils.getDateCode()
        data = {}
        data['tech_id'] = str(self.techId)
        data['station_sw_revision'] = "'" + self.station_sw_revision + "'"
        data['date_time'] = "'" + self.nowDateTime + "'"
        data['pcba_part_number'] = "'" + self.pcbaPartNumber + "'"
        data['pcba_serial_number'] = "'" + self.pcbaSerialNumber + "'"
        data['pcba_revision'] = "'" + self.pcbaRevision + "'"
        data['fpga_fw_revision'] = "'" + self.fpgaFwRevision + "'"
        data['fpga_sw_revision'] = "'" + self.fpgaSwRevision + "'"
        data['hw_revision'] = "'" + self.HwRevision + "'"
        data['pmic_sw_revision'] = "'" + self.pmicSwRevision + "'"
        data['esn'] = "'" + self.esn + "'"
        data['pass_fail'] = "'" + self.passFail + "'"
        data['notes'] = "'" + self.editNotes.toPlainText() + "'"
        data['measCurrentPrePic'] = "'" + str(self.measCurrentPrePic) + "'"
        data['measCurrentPreFPGA'] = "'" + str(self.measCurrentPreFPGA) + "'"
        data['measCurrentFinal'] = "'" + str(self.measCurrentFinal) + "'"
        data['measVoltagePrePic'] = "'" + str(self.measVoltagePrePic) + "'"
        data['measVoltagePrePic'] = "'" + str(self.measVoltagePrePic) + "'"
        data['measVoltagePreFPGA'] = "'" + str(self.measVoltagePreFPGA) + "'"
        data['measVoltageFinal'] = "'" + str(self.measVoltageFinal) + "'"
        data['Supervisor'] = "'" + str(self.SupervisorEnabled) + "'"

        data['U56'] = "'" + str(self.U56) + "'"
        data['U54'] = "'" + str(self.U54) + "'"
        data['U55'] = "'" + str(self.U55) + "'"
        data['U5'] = "'" + str(self.U5) + "'"
        data['U20'] = "'" + str(self.U20) + "'"
        data['U21'] = "'" + str(self.U21) + "'"

        data['SelfTest'] = "'" + str(self.selftest) + "'"
        data['ADCsync'] = "'" + str(self.adc) + "'"
        data['caladc'] = "'" + str(self.caladc) + "'"
        data['siTime'] = "'" + self.siTime + "'"

        for supply in self.iv_info.keys():
            for param in ['mA', 'mV']:
                data[f"{supply}_{param}"] = f"'{self.iv_info[supply][param]['Value']}'"
        for supply in self.v_info.keys():
            data[f"{supply}_mV"] = f"'{self.v_info[supply]['Value']}'"
        
        
        foldername = self.pcbaSerialNumber[4:6]

        datetime = SqlFuncs.datetimeToTimeStamp(self.nowDateTime)
        remotepath = self.ini['database']['remote_folder'] + "/" + foldername  
        if not os.path.isdir(remotepath):
            os.makedirs(remotepath)
        try:
            remoteFolder = utils.MakeTestFolder(remotepath, str(self.pcbaSerialNumber) + "_" + str(datetime))
        finally:
            utils.CopyFiles(self.imagePath, remoteFolder)
            
        impath = f"WAM/Programming/{foldername}/{self.pcbaSerialNumber}_{str(datetime)}"
        data['image_path'] = "'" + impath + "'"
        
        if(self.passFail == "FAIL"):
            self.failure(remotepath) 
        try:
            SqlFuncs.updateTetraConfiguration(data)
            SqlFuncs.ModulepostConfig(self.pcbaSerialNumber,self.passFail,self.testid)
        except Exception as e:
            utils.ErrorMsg(("Failed To upload to database due to following error - \n {}").format(e))
            return

    def failure(self, path):
        msg = MIMEMultipart()
        msg['From'] = 'tomw@ragesystems.com'
        msg['To'] = 'CharlieA@ragesystems.com,EddieR@ragesystems.com,ColinM@ragesystems.com,GretaA@ragesystems.com,GlenW@ragesystems.com,Rickq@ragesystems.com'
        msg['Subject'] = f'{self.pcbaSerialNumber} failed at programming'

        # Assuming self.editNotes.toPlainText() and self.log exist
        body = f'Log file copy attached \nNotes: {self.editNotes.toPlainText()}'
        msg.attach(MIMEText(body, 'plain'))

        with open(self.log, 'rb') as f:
            attach_file = MIMEApplication(f.read(), Name='logfile.log')
            attach_file.add_header('Content-Disposition', 'attachment', filename='logfile.log')
            msg.attach(attach_file)

        # List of recipients
        recipients = ['CharlieA@ragesystems.com', 'EddieR@ragesystems.com', 'ColinM@ragesystems.com', 'GretaA@ragesystems.com', 'GlenW@ragesystems.com', 'Rickq@ragesystems.com']

        try:
            with smtplib.SMTP('smtp-mail.outlook.com', 587) as server:
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login('tomw@ragesystems.com', '175CabotSt!')
                server.sendmail('tomw@ragesystems.com', recipients, msg.as_string())
        except Exception as e:
            print(f"An error occurred: {e}")

        # Write to CSV (Assuming self.pcbaSerialNumber, self.editNotes, self.nowDateTime, path exist)
        with open("C:\\SynologyDrive\\MRB\\MRB.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.pcbaSerialNumber, self.editNotes, self.nowDateTime, path])



def prog_pic(tool, part, path,log):
    pic_status = False
    err = ''
    cmd = f'ipecmd.exe -TP{tool} -P{part} -M -F{path} -OL > log.txt'
    os.system(cmd)
    with open(log,'a') as f:
        f.write("Log of pic programming: \n")
        with open("log.txt",'r') as fh:
            content = fh.read()
            f.write(content)
            f.write("\n")
        if 'Program Succeeded.' in content and 'Operation Succeeded' in content:
            pic_status = True
        else:
            err= "Pic Failed to program"
        return err,pic_status


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
