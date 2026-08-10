import os
import sys
import csv
import subprocess
import cv2
import glob
import qrcode

from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from playsound import playsound
import traceback

sys.path.append('../utils')
import SqlFuncs
import utils

# minute in miliseconds for timer
MINUTE = 60000

class MainWindow(QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(MainWindow, self).__init__()
        SqlFuncs.getPassword()
        # Load the .ui file
        uic.loadUi(os.path.join(os.getcwd(), 'Assembly.ui'), self)
        self.centralwidget.setContentsMargins(20, 20, 20, 20)
        # Read INI file
        self.ini = utils.ReadIni('../utils/tetra.ini')
        # Show the widget
        self.techId = None
        self.editCompletionStatus.setText("")
        self.init()
        self.cap = None
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timerEvent)
        
        
    def timerEvent(self):
        self.timer.stop()
        self.techId = None
        self.init()

    def init(self):
    
        if(self.techId):
            self.timer.start(((MINUTE)*2))
        else:
            self.editTechnician.setText("")

        # Disable all but the 'Begin new PCB' button
        self.buttonBeginNewPcb.setEnabled(True)
        self.buttonChassisTopInside.setEnabled(False)
        self.buttonChassisBottomInside.setEnabled(False)
        self.buttonAssemblyBottom1.setEnabled(False)
        self.buttonAssemblyBottom2.setEnabled(False)
        self.buttonPrintLabel.setEnabled(False)
        self.buttonAssemblyTop.setEnabled(False)
        self.Done.setText("")
        # Clear all but the completion status text
        self.station_sw_revision = utils.gitRevText('..')
        self.Rev.setText("Rev: " + self.station_sw_revision)
        
        self.editPartNumber.setText("")
        self.editSerialNumber.setText("")
        self.editRevision.setText("")
        self.editNotes.setText("")
        # Uncheck all checkboxes
        self.checkVisualPcbaInspection.setChecked(False)
        self.checkAbsorberInstalled.setChecked(False)
        self.checkScrewsTorqued.setChecked(False)
        # Set the state to 'ready' to prepare for a new PCB
        self.state = 'Ready'
        self.buttonSupeMode.setText("Enter Supervisor Mode")
        self.datecode = None
        self.pcbId = "N/A"
        self.pcbaSerialNumber = "N/A"
        self.pcbaPartNumber = "N/A"
        self.esn = "N/A"
        self.assyPartNumber = "N/A"
        self.assySerialNumber = "N/A"
        self.assyRevision = "N/A"
        self.passFail = "PASS"
        self.localFolder = "N/A"
        self.currentWidget = "N/A"
        self.SupervisorEnabled = False
        self.imagePath = os.path.join(os.getcwd(), 'pictures')
        if not os.path.isdir(self.imagePath):
            os.mkdir(self.imagePath)
        self.startTime = None
        self.timeStamp = None
        self.imgqr = None
        self.PFlabel.setText("")
        color_effect = QGraphicsColorizeEffect()
        color_effect.setColor(Qt.black)
        self.PFlabel.setGraphicsEffect(color_effect)
        self.scansn = 0
        self.scanrev = 0
        self.scanpn = 0
    #activates when supervisor button is clicked
    #checks that the Id is a cupervisor
    #allows the editing of any field as well as skipping steps
    @QtCore.pyqtSlot(name="on_buttonSupeMode_clicked")
    def clickSupeMode(self):
        if self.SupervisorEnabled == False:
            name, done1 = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Scan your badge:')
            parsed_name = name.split(",")
            loc = parsed_name[2].upper().strip()

            #verify that user is a supe
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

            #unlocks all the steps
            self.SupervisorEnabled = True
            self.buttonSupeMode.setText("Edit PASS/FAIL")
            self.buttonBeginNewPcb.setEnabled(True)
            self.buttonChassisTopInside.setEnabled(True)
            self.buttonChassisBottomInside.setEnabled(True)
            self.buttonAssemblyBottom1.setEnabled(True)
            self.buttonAssemblyBottom2.setEnabled(True)
            self.buttonPrintLabel.setEnabled(True)
            self.buttonAssemblyTop.setEnabled(True)
            self.checkVisualPcbaInspection.setChecked(True)
            self.checkAbsorberInstalled.setChecked(True)
            self.checkScrewsTorqued.setChecked(True)

            #changes the supervisor mode button to a pass fail button
            passfail = ["PASS","FAIL"]
            state, done1 = QtWidgets.QInputDialog.getItem(self, 'Input Dialog', 'PASS or FAIL module:',passfail)
            self.passFail= state
            self.updatePFlabel()

        #edits the pass/fail button if already in supe mode
        else:
            passfail = ["PASS","FAIL"]
            state, done1 = QtWidgets.QInputDialog.getItem(self, 'Input Dialog', 'PASS or FAIL module:',passfail)
            self.passFail= state
            self.updatePFlabel()

    #vhanges the /fail display to reflect the supervisors choice
    def updatePFlabel(self):
        if(self.passFail == "PASS"):
            color_effect = QGraphicsColorizeEffect()
            # setting color to color effect
            color_effect.setColor(Qt.darkGreen)
            self.PFlabel.setGraphicsEffect(color_effect)
        else:
            color_effect = QGraphicsColorizeEffect()
            # setting color to color effect
            color_effect.setColor(Qt.darkRed)
            self.PFlabel.setGraphicsEffect(color_effect)

        self.PFlabel.setText(self.passFail)

    #triggers on newPCB button click
    @QtCore.pyqtSlot(name="on_buttonBeginNewPcb_clicked")
    def clickBeginNewPcb(self):
        self.timer.stop()
        #sets a state to allow a confirmation on losing data if newpcb is clicked again
        if self.state != 'Ready':
            doCancel = utils.RunCancelDialog()
            if doCancel:
                self.state = 'Canceled'
                self.init()
                self.timer.stop()
            else:
                return
        self.state = 'Running'

        self.editCompletionStatus.setText("")

        #verify that a camera is connected
        if not self.cap:
            self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            utils.ErrorMsg("No camera detected - please make sure the camera is connected")
            return

        self.startTime = SqlFuncs.nowDateTime()
        self.timeStamp = SqlFuncs.datetimeToTimeStamp(self.startTime)

        # Delete any files that are in the image directory
        files = glob.glob(self.imagePath + "\\*")
        for file in files:
            os.remove(file)
            
        #unlocks next step
        if(self.techId):
            self.currentWidget = "editPartNumber"
            self.editSerialNumber.setReadOnly(False)
            self.editSerialNumber.setFocus()
        else:
            self.editTechnician.setReadOnly(False)
            self.currentWidget = "editTechnician"
            self.editTechnician.setFocus()
            
    def extract_date_code(self,serial_number):
        # Extract the first 6 characters as the date code
        return serial_number[:6]
        
    #checks for a keypress in textboxes verifys input when enter is clicked
    def keyPressEvent(self, e):
        #if key = 'enter'
        if e.key() == QtCore.Qt.Key_Enter - 1:
            #check which box were in
            if(str(self.currentWidget) == "editTechnician"):
                self.editTechnician.setReadOnly(True)
                labelText = self.editTechnician.text()
                self.techId, techName = utils.parseTechnicianId(labelText)
                if not self.techId:
                    self.editTechnician.setText("")
                    utils.ErrorMsg("Not a Valid Technician")
                    return
                self.editTechnician.setText(techName)

                #keep track of widget for now
                self.currentWidget = "editPartNumber"
                #unlock next text box
                self.editTechnician.setReadOnly(True)
                #lock this text box now that data is correct
                self.editSerialNumber.setReadOnly(False)
                self.editSerialNumber.setFocus()

            elif(self.currentWidget == "editPartNumber"):
                self.editSerialNumber.setReadOnly(True)
                labelText = self.editSerialNumber.text().upper().strip()
                try:
                    #checks relabel but also verifys that SN is valid
                    if self.checkReLabel.isChecked():
                        # The module is being relabeled after being reprogrammed
                        # Get most information from the label and database
                        label = utils.parseModuleLabel(labelText)
                        if not label:
                            utils.ErrorMsg("Could not read label")
                            self.editSerialNumber.setText("")
                            self.editSerialNumber.setReadOnly(False)
                            return
                        #print(label)
                        self.assySerialNumber = label['SerialNumber']
                        self.datecode = label['DateCode']
                        #print(label)
                        pcbId = SqlFuncs.getPCBIdfromAssy(self.assySerialNumber)
                        self.pcbaSerialNumber = SqlFuncs.lookupPcbaSn(pcbId)
                        #print(self.assySerialNumber)
                        
                    else:
                        # This is a new module, the labelTest is the PCBA SN
                        # from which we create a new module SN
                        self.pcbaSerialNumber = labelText
                        self.assySerialNumber = SqlFuncs.getModSn(self.pcbaSerialNumber)
                        if not self.assySerialNumber:
                            utils.ErrorMsg("Could not read label")
                            self.editSerialNumber.setText("")
                            self.editSerialNumber.setReadOnly(False)
                            return
                        #else:
                            #datacheck,present = SqlFuncs.CheckModule(self.assySerialNumber,"Assembly")
                            #if not (datacheck):
                                #if(present == 1):
                                   # utils.ErrorMsg("Failed Programming dont assemble")
                               # else:
                                   # utils.ErrorMsg("No data in database don't continue with this board")
                               # self.editSerialNumber.setText("")
                               # self.editSerialNumber.setReadOnly(False)
                               # return
                                
                        # Also create a new datecode
                        self.datecode = utils.getDateCode()

                    # Get the most recent PCB ID and ESN from the latest config
                    self.pcbId = SqlFuncs.lookupPcba(self.pcbaSerialNumber)
                    self.esn = SqlFuncs.getEsn(self.pcbId)
                    
                except Exception as err:
                    print(err)
                    traceback.print_exc()
                    if not self.SupervisorEnabled:
                        utils.ErrorMsg("Could not find board info in database\nYou Cannot procced without Floor Supervisors premisson")
                        self.editSerialNumber.setText("")
                        self.editSerialNumber.setReadOnly(False)
                        return

                #change to RaGE SN and get PN and rev from ini
                self.assyPartNumber = self.ini['board']['asyPn']
                serialDateCode = self.extract_date_code(self.assySerialNumber)

                # Compare the extracted date code with the cut off date code
                if serialDateCode >= self.ini['board']['cutOffDateCode']:
                    self.assyRevision = self.ini['board']['asyRevNew']
                else:
                    self.assyRevision = self.ini['board']['asyRev']
                # Update the GUI
                self.editPartNumber.setText(self.assyPartNumber)
                self.editSerialNumber.setText(self.assySerialNumber)
                self.editRevision.setText(self.assyRevision)
                self.editSerialNumber.setReadOnly(True)

                #no longer matters what the current widget is but it cant be the previous two
                self.currentWidget = "BeyondMe"
                if self.checkReLabel.isChecked():
                    self.buttonPrintLabel.setEnabled(True)
                    self.editRevision.setText(self.assyRevision)
                else:
                    self.checkVisualPcbaInspection.setEnabled(True)
                    self.checkVisualPcbaInspection.setFocus()
            elif(self.currentWidget == "Done"):
                if (self.scansn == 1):
                    self.Done.setReadOnly(True)
                    text = "Updating Database ..."
                    self.editCompletionStatus.setText(text)
                    app.processEvents()

                    # Update the database
                    self.UpdateDatabase()
                    text += " Done"
                    self.editCompletionStatus.setText(text)
                    app.processEvents()
                    try:
                        os.remove(os.getcwd() + "\label.txt")
                    except:
                        pass
                    # Clear the GUI to get ready for the next DUT
                    self.init()
                else:  
                    if(self.Done.text() == self.pcbaSerialNumber or self.Done.text() == self.assySerialNumber):
                        self.scansn = 1
                        self.Done.setText("")
                    elif (self.Done.text() == self.assyRevision):
                        self.scanrev = 1
                        self.Done.setText("")
                    elif(self.Done.text() ==  "1000-38534-00"):
                        self.scanpn = 1
                        self.Done.setText("")
                        
                    self.currentWidget = "Done"
                    self.Done.setFocus()
                
    #checkbox functionality for visual inspection
    @QtCore.pyqtSlot(int, name="on_checkVisualPcbaInspection_stateChanged")
    def clickVisualPcbaInspection(self, value):
        if self.checkVisualPcbaInspection.isChecked():
            self.checkVisualPcbaInspection.setEnabled(False)
            self.buttonChassisTopInside.setEnabled(True)

    #takes picture and shows it to user to verify it is good
    @QtCore.pyqtSlot(name="on_buttonChassisTopInside_clicked")
    def clickChassisTopInside(self):
        if(utils.TakePicture(self, "assyTopInside", self.assySerialNumber, self.timeStamp)):
            self.buttonChassisTopInside.setEnabled(False)
            self.checkAbsorberInstalled.setEnabled(True)

    #check box functionality
    @QtCore.pyqtSlot(int, name="on_checkAbsorberInstalled_stateChanged")
    def clickAbsorberInstalled(self, value):
        if self.checkAbsorberInstalled.isChecked():
            self.checkAbsorberInstalled.setEnabled(False)
            self.buttonChassisBottomInside.setEnabled(True)

    #takes picture
    @QtCore.pyqtSlot(name="on_buttonChassisBottomInside_clicked")
    def clickChassisBottomInside(self):
        if(utils.TakePicture(self, "assyBottomInside", self.assySerialNumber, self.timeStamp)):
            self.buttonChassisBottomInside.setEnabled(False)
            self.buttonAssemblyBottom1.setEnabled(True)

    #takes picture
    @QtCore.pyqtSlot(name="on_buttonAssemblyBottom1_clicked")
    def clickAssemblyBottom1(self):
        if(utils.TakePicture(self, "assyBottom1", self.assySerialNumber, self.timeStamp)):
            self.buttonAssemblyBottom1.setEnabled(False)
            self.checkScrewsTorqued.setEnabled(True)

    #check box functionality
    @QtCore.pyqtSlot(int, name="on_checkScrewsTorqued_stateChanged")
    def clickScrewsTorqued(self, value):
        if self.checkScrewsTorqued.isChecked():
            self.checkScrewsTorqued.setEnabled(False)
            self.buttonAssemblyBottom2.setEnabled(True)

    #takes picture
    @QtCore.pyqtSlot(name="on_buttonAssemblyBottom2_clicked")
    def clickAssemblyBottom2(self):
        if(utils.TakePicture(self, "assyBottom2", self.assySerialNumber, self.timeStamp)):
            self.buttonAssemblyBottom2.setEnabled(False)
            self.buttonPrintLabel.setEnabled(True)

    #constructs a csv to pass to the label print bat function to print a label
    @QtCore.pyqtSlot(name="on_buttonPrintLabel_clicked")
    def clickPrintLabel(self):
        column_names = ['sn','rev']
        csv_data = [{'sn':self.assySerialNumber, 'rev':self.assyRevision}]
        with open(os.getcwd() + "\label.csv",'w') as f:
           writer = csv.DictWriter(f, fieldnames = column_names)
           writer.writeheader()
           writer.writerows(csv_data)
        
        self.buttonPrintLabel.setEnabled(False)
        self.buttonAssemblyTop.setEnabled(True)

        barcode = self.assySerialNumber + ',' + self.esn[2:] + ',' + self.datecode + ',' + self.assyRevision + ',Wideband Antenna Module,5083561, RaGE Systems, Leidos PN: AX1000-38534-00'
        self.imgqr = qrcode.make(barcode)
        self.imgqr.save(self.imagePath + "//" + 'barcode_' + self.assySerialNumber + ".pdf")

    #You know we gotta take a picture of that fresh newlabel
    @QtCore.pyqtSlot(name="on_buttonAssemblyTop_clicked")
    def clickAssemblyTop(self):
        if(utils.TakePicture(self, "assyTop", self.assySerialNumber, self.timeStamp)):
            self.buttonAssemblyTop.setEnabled(False)
            self.Done.setReadOnly(False)
            self.currentWidget = "Done"
            self.Done.setFocus()

    #uploads info to database and pictures to the Synology drive
    def UpdateDatabase(self):
        # highnum = utils.roundup(self.pcbaSerialNumber)
        # lownum = int(highnum) - 99
        # foldername = str(lownum)+"_"+str(highnum)
        foldername = self.pcbaSerialNumber[4:6]
        datetime = SqlFuncs.nowDateTime()
        datetime = SqlFuncs.datetimeToTimeStamp(datetime)
        
        remotepath = self.ini['database']['remote_folder'] + "/" + foldername  
        if not os.path.isdir(remotepath):
            os.makedirs(remotepath)
        try:
            remoteFolder = utils.MakeTestFolder(remotepath, str(self.pcbaSerialNumber) + "_" + str(datetime))
        finally:
            utils.CopyFiles(self.imagePath, remoteFolder)
            impath = "WAM" +"/" + foldername + "/" + str(self.pcbaSerialNumber) + "_" + str(datetime)
       
        data = {}
        data['tech_id'] = str(self.techId)
        data['station_sw_revision'] = "'" + self.station_sw_revision + "'"
        data['pcb_id'] = str(self.pcbId)
        data['date_time'] = "'" + self.startTime + "'"
        data['module_part_number'] = "'" + self.assyPartNumber + "'"
        data['module_serial_number'] = "'" + self.assySerialNumber + "'"
        data['module_revision'] = "'" + self.assyRevision + "'"
        data['pcb_visual_ok'] = "'" + str(int(self.checkVisualPcbaInspection.isChecked())) + "'"
        data['antenna_absorber'] = "'" + str(int(self.checkAbsorberInstalled.isChecked())) + "'"
        data['screw_torque'] = "'" + str(int(self.checkScrewsTorqued.isChecked())) + "'"
        data['pass_fail'] = "'" + str(self.passFail) + "'"
        data['notes'] = "'" + self.editNotes.toPlainText() + "'"
        data['image_path'] = "'" + impath + "'"
        data['Supervisor'] = "'" + str(self.SupervisorEnabled) + "'"
        data['DateCode'] = "'" + str(self.datecode) + "'"
        
        


        try:
            SqlFuncs.updateTetraAssembly(data)
            SqlFuncs.ModulepostAss(self.assySerialNumber,self.passFail)
        except Exception as e:
            #Failed to upload
            utils.ErrorMsg(("Failed To upload to database due to following error - \n {}").format(e))
            return
            
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
