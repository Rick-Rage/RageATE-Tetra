#from _typeshed import FileDescriptorLike
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import subprocess
import sys
import os
import datetime
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
sys.path.append('../utils')
import SqlFuncs
import utils
import math
import re
MINUTE = 60000
app = None

#This window displays the current conetents of the current Box 
#Allows the user to remove items from the box
#Shown when the the "box contents" button is pressed in MainWindow
class BoxContents(QWidget):

    def __init__(self,parent=None,path = None, name = None):
        super(BoxContents,self).__init__(parent)
        self.setWindowFlags(Qt.Window)
        uic.loadUi(os.path.join(os.getcwd(), 'BoxContents.ui'), self)
        #get the current contents of the carton
        self.content = SqlFuncs.checkCartonContent(parent.spinBox.value())
        self.spin = parent.spinBox.value()
        #clears the display
        for i in range(0,18):
            self.tableUut.setItem(i, 1, QTableWidgetItem(''))
        self.initUI()
        
    def initUI(self):
        #fills carton contents into the display
        for i in range(0,len(self.content)):
                self.tableUut.item(i, 1).setText(self.content[i])
        #gets the current carton number
        self.boxnum = SqlFuncs.getCartonNum(self.spin)
        self.choice = None
        self.show()
        
    #resets the display in the case of a deletion
    def reset(self):
        self.content = SqlFuncs.checkCartonContent(self.spin)
        self.choice = None
        for i in range(0,len(self.content)):
            self.tableUut.setItem(i, 1, QTableWidgetItem(''))
        for i in range(0,len(self.content)):
                self.tableUut.item(i, 1).setText(self.content[i])
                
    #removes the selected carton from the box 
    #prompts user to make sure this is the correct choice
    def remove(self):
        print(self.content)
        print(self.choice)
        if len(self.content) < self.choice or self.content == []:
            utils.WarningMsg("There is no module to remove")
            return
        buttonReply = QMessageBox.warning(self, 'Confirmation', f"Are you sure you want to remove {self.content[self.choice]}", QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            SqlFuncs.setCartonNum(self.content[self.choice])
            self.reset()
            
    #from here(63) to line 161 is simply the logic that allows the buttons to remove their corresponding module    
    @QtCore.pyqtSlot(name="on_buttRemove_1_clicked")
    def buttRemove1(self):
        self.choice = 0
        self.remove()
      
    @QtCore.pyqtSlot(name="on_buttRemove_2_clicked")
    def buttRemove2(self):
        self.choice = 1
        self.remove()
                        
    @QtCore.pyqtSlot(name="on_buttRemove_3_clicked")
    def buttRemove3(self):
        self.choice = 2
        self.remove()
                        
    @QtCore.pyqtSlot(name="on_buttRemove_4_clicked")
    def buttRemove4(self):
        self.choice = 3
        self.remove()
               
    @QtCore.pyqtSlot(name="on_buttRemove_5_clicked")
    def buttRemove5(self):
        self.choice = 4
        self.remove()
               
    @QtCore.pyqtSlot(name="on_buttRemove_6_clicked")
    def buttRemove6(self):
        self.choice = 5
        self.remove()
             
    @QtCore.pyqtSlot(name="on_buttRemove_7_clicked")
    def buttRemove7(self):
        self.choice = 6
        self.remove()
             
    @QtCore.pyqtSlot(name="on_buttRemove_8_clicked")
    def buttRemove8(self):
        self.choice = 7
        self.remove()
             
    @QtCore.pyqtSlot(name="on_buttRemove_9_clicked")
    def buttRemove9(self):
        self.choice = 8
        self.remove()
             
    @QtCore.pyqtSlot(name="on_buttRemove_10_clicked")
    def buttRemove10(self):
        self.choice = 9
        self.remove()
             
    @QtCore.pyqtSlot(name="on_buttRemove_11_clicked")
    def buttRemove11(self):
        self.choice = 10
        self.remove()
             
    @QtCore.pyqtSlot(name="on_buttRemove_12_clicked")
    def buttRemove12(self):
        self.choice = 11
        self.remove()
             
    @QtCore.pyqtSlot(name="on_buttRemove_13_clicked")
    def buttRemove13(self):
        self.choice = 12
        self.remove()
             
    @QtCore.pyqtSlot(name="on_buttRemove_14_clicked")
    def buttRemove14(self):
        self.choice = 13
        self.remove()
             
             
    @QtCore.pyqtSlot(name="on_buttRemove_15_clicked")
    def buttRemove15(self):
        self.choice = 14
        self.remove()
             
    @QtCore.pyqtSlot(name="on_buttRemove_16_clicked")
    def buttRemove16(self):
        self.choice = 15
        self.remove()
        
    @QtCore.pyqtSlot(name="on_buttRemove_17_clicked")
    def buttRemove17(self):
        self.choice = 16
        self.remove()
             
    @QtCore.pyqtSlot(name="on_buttRemove_18_clicked")
    def buttRemove18(self):
        self.choice = 17
        self.remove()
             
    @QtCore.pyqtSlot(name="on_buttRemove_19_clicked")
    def buttRemove19(self):
        self.choice = 18
        self.remove()
             
    @QtCore.pyqtSlot(name="on_buttRemove_20_clicked")
    def buttRemove20(self):
        self.choice = 19
        self.remove()

#the Main Window 
#Generates reports and verifys that modules have completed and passed all previous stations
class MainWindow(QMainWindow):
    #startup - only runs once
    def __init__(self):
        SqlFuncs.getPassword()
        # Call the inherited classes __init__ method
        super(MainWindow, self).__init__()
        # Load the .ui file
        uic.loadUi(os.path.join(os.getcwd(), 'FinalQc.ui'), self)
        self.centralwidget.setContentsMargins(20, 20, 20, 20)
        # Read INI file
        self.ini = utils.ReadIni('../utils/tetra.ini')
        self.scannerPort = self.ini['scanner']['port']
        self.spinBox.setValue(18)
        self.direct = os.getcwd()
        # Initialize the widget
        self.techId = None
        self.init()
        #self.editCompletionStatus.setText("")

        # Initialize the parameters
        self.techName = None
        self.pcbid = None
        self.asyid = None
        self.modulePartNumber = None
        self.moduleSerialNumber = None
        self.currentWidget = None
        self.PCBATestTime = None
        self.PCBATestPF = None
        self.AssemblyTime = None
        self.AssemblyPF = None
        self.BurnInTime = None
        self.BurnInPF = None
        self.FinalTestTime = None
        self.FinalTestPF = None
        self.LotDate = None
        self.ESN = None
        self.rx = None
        self.tx = None
        self.FPGAFWRev = None
        self.FPGASWRev = None
        self.PMICSWRev = None
        self.rev = None
        self.carton = None
        self.bounce = None
        self.spinBox.valueChanged.connect(self.spinBoxValueChanged)
        
        self.direct = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timerEvent)
       
    def timerEvent(self):
        self.timer.stop()
        self.techId = None
        self.init()
        
    #initialize - runs after a full run through of the program
    def init(self):
    
        if(self.techId):
            self.timer.start(((MINUTE)*2))
        else:
            self.editTechnician.setText("")
            
        #set buttons to false exceppt for begin new
        self.buttonBeginNewAss.setEnabled(True)
        self.buttonDone.setEnabled(False)
        self.view_cart_cont.setEnabled(True)
        #empty all text boxes
        os.chdir(self.direct)
        self.station_sw_revision = utils.gitRevText('..')
        self.Rev.setText("Rev: " + self.station_sw_revision)
        self.editSerialNumber.setText("")
        self.editPCBATest.setText("")
        self.editPCBATestPF.setText("")
        self.editAssembly.setText("")
        self.editAssemblyPF.setText("")
        self.editBurnIn.setText("")
        self.editBurnInPF.setText("")
        self.editFinalTest.setText("")
        self.editFinalTestPF.setText("")
        self.editLotDate.setText("")
        self.editESN.setText("")
        self.editFPGAFWRev.setText("")
        self.editFPGASWRev.setText("")
        self.editPMICSWRev.setText("")
        self.editNotes.setText("")
        
        #uncheck CheckBoxes
        self.printcheck.setChecked(False)
        self.checkBoxClean.setChecked(False)
        self.checkBoxClean.setEnabled(False)
        self.state = 'Ready'
        #set Carton State
        self.setCarton()
        
    def spinBoxValueChanged(self, value):
        self.setCarton()
    #gets the current amount of modules in the carton
    def setCarton(self):
        self.carton_num.setText(str(SqlFuncs.getCartonNum(self.spinBox.value())))
        self.carton_cont.setText(str(len(SqlFuncs.checkCartonContent(self.spinBox.value()))) + "/" + str(self.spinBox.value()))

    @QtCore.pyqtSlot(int, name="on_checkBoxClean_stateChanged")
    def clickAbsorberInstalled(self):
        if self.checkBoxClean.isChecked():
            self.buttonDone.setEnabled(True)
            
    @QtCore.pyqtSlot(name="on_view_cart_cont_clicked")
    def contentCheck(self):
        self.win2 = BoxContents(self)
        self.win2.show()
        self.setCarton()
        
        
    @QtCore.pyqtSlot(name="on_buttonBeginNewAss_clicked")
    def clickBeginNewAss(self):
        if self.state != 'Ready':
            doCancel = utils.RunCancelDialog()
            if doCancel:
                self.init()
            else:
                return
        self.state = 'Running'
        app.processEvents()
        # Get technician info from the scanner

        if(self.techId):
            self.currentWidget = "editSerialNumber"
            self.editSerialNumber.setReadOnly(False)
            self.editSerialNumber.setFocus()
        else:
            self.editTechnician.setReadOnly(False)
            self.currentWidget = "editTechnician"
            self.editTechnician.setFocus()
        

    @QtCore.pyqtSlot(name="on_buttonDone_clicked")
    def Upload(self):
        self.carton = str((SqlFuncs.getCartonNum(self.spinBox.value())))
        data = {}
        data['tech_id'] = str(self.techId)
        data['station_sw_revision'] = "'" + self.station_sw_revision + "'"
        data['asy_id'] = str(self.asyid)
        data['date_time'] = "'" + SqlFuncs.nowDateTime() + "'"
        data['module_part_number'] = "'" + self.ini['board']['asyPn'] + "'"
        data['module_serial_number'] = "'" + self.moduleSerialNumber + "'"
        data['module_revision'] = "'" + self.rev + "'"
        data['pass_fail'] = "'Pass'"
        data['notes'] = "'" + self.editNotes.toPlainText() + "'"
        data['Carton'] = "'" + self.carton + "'"
        try:
            SqlFuncs.updateTetraQC(data)
        except Exception as e:
            utils.ErrorMsg(e)
        else:
            foldername = self.moduleSerialNumber[4:6]

            datetime = SqlFuncs.nowDateTime()
            datetime = SqlFuncs.datetimeToTimeStamp(datetime)
            os.chdir('C:\\3500004_TetraProductionReportGenerator')
            remotepath = self.ini['database']['remote_folder'] + "/" + foldername  
            if not os.path.isdir(remotepath):
                os.makedirs(remotepath)
            newfilename = self.ini['database']['remote_folder'] + "/" + foldername + "/" + self.filename.split('.pdf')[0] + "_" + datetime + '.pdf'
            os.rename(self.filename,newfilename)
            os.chdir(self.direct)
            if self.printcheck.isChecked():
                utils.SilentPrint(newfilename,'EPSON4D7E6A (WF-7840 Series)')


        #initialize(clear all fields to start again)
        self.init()

    #For the User Scan inputs were just looking at keypresses and wont do anythin until enter is hit
    def keyPressEvent(self, e):
        #if key = 'enter'
        if e.key() == QtCore.Qt.Key_Enter - 1:
            #check which box were in
            if(str(self.currentWidget) == "editTechnician"):
                tid = self.editTechnician.text().upper()
                self.techId,self.techName = utils.parseTechnicianId(tid)
                if self.techId == None:
                    utils.WarningMsg("Invalid Name")
                    self.editTechnician.setText("")
                    return
                self.editTechnician.setText(self.techName)
                #WAM-000105,0x00003609B5D6,2232,C.05, Wideband Antenna Module,5083561, RaGE Systems, www.ragesystems.com

                #keep track of widget for now
                self.currentWidget = "editSerialNumber"
                #unlock next text box
                self.editTechnician.setReadOnly(True)
                #lock this text box now that data is correct
                self.editSerialNumber.setReadOnly(False)
                self.editSerialNumber.setFocus()

            #if we arent in editSerialNumber or edit technician I dont want the enter key to do anything
            elif (str(self.currentWidget) == "editSerialNumber"):
                pcb = self.editSerialNumber.text()
                parsed_name = utils.parseModuleLabel(pcb)
                pcb = self.editSerialNumber.text().upper()
                print(pcb)
                parsed_name = utils.parseModuleLabel(pcb)
           
                if (parsed_name == None):
                    utils.WarningMsg("Invalid Module number")
                    self.editSerialNumber.setText("")
                    return
                self.rev = parsed_name['Revision']
                self.moduleSerialNumber = parsed_name['SerialNumber']
                self.LotDate = (parsed_name['DateCode'])
                self.esn = parsed_name['ESN']

                self.editSerialNumber.setText(self.moduleSerialNumber)
                self.editSerialNumber.setReadOnly(True)

                self.asyid = SqlFuncs.getAssyIdFromModule(self.moduleSerialNumber)

                self.fillData()

                self.currentWidget = "Beyond"
                


    def fillData(self):
        #Look up tests in database to get test date and pass fail info
        try:
            ok = self.ConfigData()
        except:
            utils.ErrorMsg("No PCBAdata Found")
            self.init()
            return()
        if ok == -1:
            self.init()
            return()
           
        try:
            ok = self.AssemblyData()
        except:
            utils.ErrorMsg("No Assembly data found")
            self.init()
            return()
        if ok == -1:
            self.init()
            return()
           
        try:
            ok = self.BurnData()
        except:
            utils.ErrorMsg("No Burn in data found")
            self.init()
            return()
        if ok == -1:
            self.init()
            return()

        try:
            ok = self.FinalData()
        except Exception  as e:
            utils.ErrorMsg("No Final Data Found")
            self.init()
            return()
        if ok == -1:
           self.init()
           return()

        self.checklabel()

        self.editLotDate.setText(self.LotDate)
        self.editESN.setText(self.esn)

        self.FPGAFWRev = SqlFuncs.getFPGAfw(self.pcbid)
        self.editFPGAFWRev.setText(self.FPGAFWRev)
        self.FPGASWRev = SqlFuncs.getFPGAsw(self.pcbid)
        self.editFPGASWRev.setText(self.FPGASWRev)
        self.PMICSWRev = SqlFuncs.getPICsw(self.pcbid)
        self.editPMICSWRev.setText(self.PMICSWRev)

        self.checkBoxClean.setEnabled(True)


    def ConfigData(self):
        self.ConfigTestTime,self.ConfigTestPF,self.pcbid = SqlFuncs.lookupConfigTest(self.moduleSerialNumber)

        self.editPCBATest.setText(str(self.ConfigTestTime))
        self.editPCBATestPF.setText(self.ConfigTestPF.upper())
        
        if(self.ConfigTestPF.upper() != 'PASS' or self.ConfigTestPF.upper() == None or self.ConfigTestTime == None):
            utils.ErrorMsg("Did not Pass Programming")
            return(-1)
        return(1)
            

    def AssemblyData(self):
        self.AssemblyTime,self.AssemblyPF = SqlFuncs.lookupAssemblyTest(self.moduleSerialNumber)

        self.editAssembly.setText(str(self.AssemblyTime))
        self.editAssemblyPF.setText(self.AssemblyPF.upper())
       
        if(self.AssemblyPF.upper() != 'PASS' or self.AssemblyPF.upper() == None):
            utils.ErrorMsg("Did not pass Assembly - how is that possible?")
            return(-1)
        return(1)
        
    def BurnData(self):
        self.BurnInTime, self.BurnInPF = SqlFuncs.lookupBurnInTest(self.moduleSerialNumber)
        self.editBurnIn.setText(str(self.BurnInTime))
        self.editBurnInPF.setText(self.BurnInPF.upper())
       
        if(self.BurnInPF.upper() != 'PASS' or self.BurnInPF.upper() == None or self.AssemblyTime == None):
            utils.ErrorMsg("Did not pass Burn in")
            return(-1)
        return(1)
        
    def FinalData(self):
        self.FinalTestTime,self.rx,self.tx,self.bounce = SqlFuncs.lookupFinalTest(self.moduleSerialNumber)
        if(self.rx == "Noid" or self.tx == "Noid" or self.bounce == "Noid"):
            utils.ErrorMsg("This board is missing a critical test id and must be retested")
            return(-1)
        self.direct = os.getcwd()
       
        os.chdir('C:\\3500004_TetraProductionReportGenerator')
       
        out = os.system(f"python finalTestOutcome.py -txid {self.tx} -rxid {self.rx} -bid {self.bounce} >Status.txt")
        with open("Status.txt") as fh:
            data = fh.readline()
            temp = data.split(":")[0]
        if temp == 'Overall Status  ':
            self.FinalTestPF = data.split(":")[1].strip()
        os.remove('Status.txt')
        try:
            os.system(f'python C:\\3500004_TetraProductionReportGenerator\\newreport.py -rxid {self.rx} -txid {self.tx} -bid {self.bounce}')
        except Exception  as e:
            utils.ErrorMsg("No Final Data Found")
            return(-1)
        
        if self.FinalTestPF == None:
            utils.ErrorMsg("Did not pass Final Test")
            return(-1)
            
        self.editFinalTest.setText(str(self.FinalTestTime))      
        self.editFinalTestPF.setText(self.FinalTestPF.upper())
        self.filename = "AM_"+self.moduleSerialNumber + ".pdf"
       
        if(self.FinalTestPF.upper() != 'PASS' or self.FinalTestPF.upper() == None or self.FinalTestTime == None):
            utils.ErrorMsg("Did not pass Final Test")
            return(-1)
            
        os.chdir(self.direct)
        return(1)
        
    def checklabel(self):
        return
        # self.esn = SqlFuncs.getEsn(self.pcbid)
        # if self.esnlbl not in self.esn:
            # utils.WarningMsg("ESN not consistent with database")

        # self.LotDate = SqlFuncs.getdatecode(self.moduleSerialNumber)
        # if(self.LotDate != self.LotDatelbl):
            # utils.WarningMsg("LotCode not consistent with database")





if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
