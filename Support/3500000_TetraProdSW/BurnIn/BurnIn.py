from datetime import datetime
import math
import fnmatch
import sys
import os
import pathlib
import win32com.client as win32
import shutil
import glob
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
import threading
import glob
sys.path.append('../utils')

import utils
import SqlFuncs
from RageComm import RageComm

app = None

colorOK = QtGui.QColor(16, 239, 109)
colorFault = QtGui.QColor(252, 33, 27)

class Moduleclass:
    """
    Class for storing information about a module uner test
    """
    def __init__(self, bibIndex, port, com, num):
        """
        Initlaize a module object
        :param self: Reference to this object
        :param bibIndex: Index of the BiB this module is plugged into
        :param com: Serial port connected to this modulef
        :param num: Index of this module out of all modules under test
        :param fault: Fault indicator for this module
        :param asyId: Assembly serial number of the module
        """
        self.bibIndex = bibIndex
        self.port = port
        self.com = com
        self.num = num
        self.fault = False
        self.asyId = None
        self.sn = None
        self.temp_C = 0
        self.curr = 0
        self.current_mA = 0
        self.power_W = 0
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
            'tx2p5':   {'Value': 0, 'Low': 0, 'High': 0, 'Ok': False}}

        def __str__(self):
            return str(self.__class__) + ": " + str(self.__dict__)

class Worker(QObject):

    finished = pyqtSignal()
    finishedStartup = pyqtSignal(list,list)         # Startup work is done
    finishedIteration = pyqtSignal()       # Current test iteration is done
    setStatusText = pyqtSignal(str)
    displayModuleStatus = pyqtSignal(list)
    resizeTableUut = pyqtSignal()
    
    dialogErrMsg = pyqtSignal(str)
    clickStopandUpload = pyqtSignal()

    def __init__(self, ini, bibs, modules, logFileName):
        super(Worker, self).__init__()
        self.ini = ini
        self.bibs = bibs
        self.curr = 1
        self.modules = modules
        self.logFileName = logFileName
        self.f = None

        #======== Signals ===========

    #========= Slots ============

    def runStartUp(self):
        """
        Gets the hardware and data structures ready to begin testing
        Turns on the main supply, then sets up communications with the burn-in
        boards and the DUT serial connections
        """

        with open(self.logFileName, "a") as self.f:

            print("Looking for module connections ...")
            #BiB = Burn in Board
            imodule = 1
            self.bibs = []
            self.modules = []
            curr = .6
            ps_port = self.ini['burnin_power_supply']['port']
            for ibib in range(1,5):

                # Connecting to burn-in boards.  If the connection fails go on
                # to the next board
                try:
                    board = RageComm(self.ini['burnin'][f'BiB{ibib}'],38400)
                    self.bibs.append(board)
                    board.consoleIo("poweroff all")
                    board.consoleIo("faultoff")
                except:
                    continue

                # A burn-in board was found, look for modules connected to it
                for iport in range(1,13):
                    try:
                        newcom = RageComm(self.ini['burnin'][f'BiB{ibib}port{iport}'])
                        self.modules.append(Moduleclass(ibib-1, iport, newcom, imodule))
                    except:
                        pass
                    imodule = imodule + 1

            # Turn on each DUT and read it's ESN, currents and temperatures
            for module in self.modules:
                while(True):
                    self.setStatusText.emit(f"Powering up module {module.num} ...")

                    ok = self.turnOnDut(module)
                    if not ok:
                        continue

                    if module.sn:
                        if( not (SqlFuncs.CheckModule(module,"BurnIn"))):
                            utils.ErrorMsg(f"Module {module.sn} at location {module.bibIndex} has failed the database check please remove it before continuing")
                        else:
                            self.pollDutStatus(module)
                            self.displayModuleStatus.emit([module])
                            break
                    else:
                        break

            self.f.write('===========StartUp Finished=============')

        self.finishedStartup.emit(self.bibs, self.modules)
        self.finished.emit()


    def stop(self):
        self.threadactive = False


    #Does basically all of burn in
    #has a log file that logs everything
    #talks to all the boards for statuses
    def runIteration(self):

        #empty list to store the burn in status call-
        #This is neccessary becuase the info hear is needed later on in the
        #loop so it can't just be saved to the log file and ignored
        with open(self.logFileName, 'a') as self.f:

            burnstat = []
            for i,BiB in enumerate(self.bibs):
                self.f.write('Burnin Board: ' + str(i) + '\n')

                status, statusText = self.readBiBStatus(BiB)
                self.f.write(statusText)

                burnstat.append(status)

            supplyV,supplyC,supplyP,supplyfault = utils.CheckPowerSupplyBurn(self.ini['burnin_power_supply']['port'])
            self.f.write(f"PowerSupply:\n V = {supplyV}, C = {supplyC}, P = {supplyP}\n\n")
            print(supplyfault)
            if supplyfault.find('ERR') != -1 or supplyfault.find('8') != -1:
                self.f.write("OVER VOLTAGE EVENT POWERING DOWN")
                self.dialogErrMsg.emit("OVER VOLTAGE STOPPING TEST")
                try:
                    outlook = win32.Dispatch('outlook.application')
                    mail = outlook.CreateItem(0)
                    mail.To = 'Tetra_Production@ragesystems.com'
                    mail.Subject = 'Burn In Over Current'
                    mail.Body = 'Log file copy attached'
                    # To attach a file to the email (optional):
                    print(str(pathlib.Path(__file__).parent.resolve()) + "\\" + self.logFileName)
                    mail.Attachments.Add(str(pathlib.Path(__file__).parent.resolve()) + "\\" + self.logFileName)

                    mail.Send()
                except Exception as e:
                    print(e)
                    pass
                self.clickStopandUpload.emit()
                    
            for module in self.modules:
                if not module.sn or module.fault:
                    continue

                # Check the modules current via the burn-in board
                status = burnstat[module.bibIndex][module.port-1]
                dutStatus = status['status']
                module.current_mA = status['current_mA']
                module.power_W = supplyV * module.current_mA / 1000.0

                if (module.current_mA < float(self.ini['burnin']['min_current_mA'])
                        or dutStatus) == 'FAULT':
                    # This module faulted, turn it off, flag it and move on to
                    # the next
                    BiB = self.bibs[module.bibIndex]
                    BiB.consoleIo(f"poweroff {module.port}")
                    BiB.consoleIo('faulton')
                    module.fault = True
                    continue

                # See how the moule's doing
                self.pollDutStatus(module)

                # Update the table with the module's data
                self.displayModuleStatus.emit([module])

        # Finished the iteration
        self.finishedIteration.emit()
        self.finished.emit()


    def readBiBStatus(self, BiB):
        ret = None
        # Format of status response
        #
        # 1) OFF N/A      0.66 mA
        # 2) OFF N/A      0.66 mA
        # <skipped>
        #10) OFF N/A      1.33 mA
        #11) OFF N/A      0.66 mA
        #12) ON  OK     504.82 mA
        for itry in range(0,3):
            try:
                allStatus = BiB.consoleIo("status")
                print(allStatus)
                statusLines = allStatus.split('\n')
                allModules = []
                for iline,statusLine in enumerate(statusLines):
                    if not statusLine.strip():
                        continue
                    resp = {}
                    statusFields = [f.strip() for f in statusLine.split(')')]
                    resp['port'] = int(statusFields[0])
                    if resp['port'] != iline:
                        allModules = None
                        break
                    statusFields = [f.strip() for f in statusFields[1].split()]
                    resp['power'] = statusFields[0]
                    resp['status'] = statusFields[1]
                    resp['current_mA'] = float(statusFields[2])
                    allModules.append(resp)
                break
            except:
                allModules = None
        return allModules, allStatus


    def turnOnDut(self, module):
        # Turn on the EN line to the DUT's ECB
        # Read the FAULT bit and IMON current for the DUT
        # If all is within tolerance, read the ESN from the device
        # Use the ESN in the assembly table to lookup the assembly serial number
        # TBD
        BiB = self.bibs[module.bibIndex]
        BiB.consoleIo(f"poweron {module.port}")

        # sleep for a second just to relax I feel like were getting all wound up
        time.sleep(.5)

        # gonna check the status to make sure shes doing okay on startup
        status, statusText = self.readBiBStatus(BiB)
        if not status:
            utils.ErrorMsg.emit("Could not read status from burn-in controller")
            return False

        # get the status of the module we just turned on
        dutStatus = status[module.port-1]['status']
        current_mA = status[module.port-1]['current_mA']

        ps_port = self.ini['burnin_power_supply']['port']
        ok = False
        if (dutStatus == 'FAULT'):
            # Module is drawing too much current, turn it off and declare a
            # fault
            BiB.consoleIo(f"poweroff {module.port}")
            BiB.consoleIo('faulton')
            module.fault = True
            module.sn = "N/A"
            self.f.write(f'Over current on {module.bibIndex}.{module.port}\n')
            ok = True
        elif current_mA < float(self.ini['burnin']['min_current_mA']):
            # Assuming there is no module in this location
            BiB.consoleIo(f"poweroff {module.port}")
            ok = True
        else:
            time.sleep(0.25)
            self.curr = self.curr + .6
            utils.incVoltageBurn(ps_port)
            utils.setCurrent(ps_port,self.curr)
            try:
                for i in range(0,10):
                    time.sleep(1)
                    ok = module.com.Ping(timeout=1)
                    if ok:
                        break
                esn = utils.GetEsn(module.com).get("Serial")
                esn = esn.replace(' ','')
                print(esn)
                module.asyId, module.sn = SqlFuncs.lookupAssemblySn(esn)


                ok = True
            except Exception as e:
                print(e)
                BiB.consoleIo(f"poweroff {module.port}")
                BiB.consoleIo('faulton')
                module.fault = True
                module.sn = "N/A"
                self.f.write(f'Could not find module {module.bibIndex}.{module.port} in database \n')
                ok = True
        return ok


    def pollDutStatus(self, module):
        # Read the DUTs currents, voltages and temperatures
        #   gonna check the status to make sure shes doing okay
        if (module.fault == True):
            return

        self.f.write(module.sn + ' ' +  utils.GetDateTime() + '\n')

        #hours = self.run_time // 3600
        #minutes = (self.run_time - hours * 3600) // 60
        #seconds = self.run_time - hours * 3600 - minutes * 60
        #self.f.write(f"Elapsed Time: {hours:02d}:{minutes:02d}:{seconds:02d} \n\n")

        try:
            temps = module.com.consoleIo('rd tmon')
            self.f.write('Temps:\n' + temps + '\n')
            temps = temps.split('\n')
            module.temp_C = float(temps[0].split()[1])
            iv = utils.GetRdiv(module.com)
            rdv = utils.GetRdv(module.com)
            selftestcheck = utils.selfTest(module.com)
        except:
            self.f.write('ERR: Could not read serial. Powering down board\n')
            BiB = self.bibs[module.bibIndex]
            BiB.consoleIo(f"poweroff {module.port}")
            BiB.consoleIo('faulton')
            module.fault = True
            return

        # if selftestcheck['Test:'] != "PASSED":
            # self.f.write('ERR: Self test failed\n')
            # self.f.write(str(selftestcheck))
            # BiB = self.bibs[module.bibIndex]
            # BiB.consoleIo(f"poweroff {module.port}")
            # BiB.consoleIo('faulton')
            # module.fault = True
            

        ok1 = utils.UpdateIv(module.iv_info, self.ini, iv)
        if not ok1:
            for supply in module.iv_info.keys():
                for param in ['mA', 'mV']:
                    if not module.iv_info[supply][param]['Ok']:
                        v = module.iv_info[supply][param]['Value']
                        lo = module.iv_info[supply][param]['Low']
                        hi = module.iv_info[supply][param]['High']
                        txt = f"\nSupply {supply}: {v} {param} out of range {lo} to {hi} {param} "
                        module.fault = True

        ok2 = utils.UpdateV(module.v_info, self.ini, rdv)
        if not ok2:
            for supply in module.v_info.keys():
                if not module.v_info[supply]['Ok']:
                    v = module.v_info[supply]['Value']
                    lo = module.v_info[supply]['Low']
                    hi = module.v_info[supply]['High']
                    module.fault = True


        if module.fault:
            self.f.write('ERR: over Current or Voltage \n')
            BiB = self.bibs[module.bibIndex]
            BiB.consoleIo(f"poweroff {module.port}")
            BiB.consoleIo('faulton')


        ivfixxed = str(iv).replace('},','\n')
        ivfixxed = ivfixxed.replace("}}","\n")
        ivfixxed = ivfixxed.replace("{","")
        ivfixxed = ivfixxed.replace("'","")
        self.f.write('RDIV:\n ')
        self.f.write(ivfixxed)

        rdvfixxed = str(rdv).replace(',','\n')
        rdvfixxed = rdvfixxed.replace("{","")
        rdvfixxed = rdvfixxed.replace("}","")
        rdvfixxed = rdvfixxed.replace("'","")
        self.f.write('RDV:\n ')
        self.f.write(rdvfixxed)
        self.f.write('\n\n')


def dutRowColumn(ndut, idut):
    """
    Finds the starting position of the DUT's information in the display table
    :param ndut: Unused
    :param idut: Moudle's index number
    """
    if idut <= 24:
        row = idut - 1
        col = 1
    else:
        row = idut -25
        col = 6
    return row, col


class MainWindow(QMainWindow):

    def __init__(self):
        # Call the inherited classes __init__ method
        super(MainWindow, self).__init__()

        SqlFuncs.getPassword()

        # Load the .ui file
        uic.loadUi(os.path.join(os.getcwd(), 'BurnIn.ui'), self)
        self.showMaximized()

        self.centralwidget.setContentsMargins(20, 20, 20, 20)
        self.moduleSerialNumber = None
        self.assyId = None
        # Read INI file
        self.ini = utils.ReadIni(os.getcwd() +'//..//Utils//tetra.ini')
        self.maxNModules = 24
        self.buildTable()
        self.colorBackground = self.tableUut.item(0, 0).background()
        #self.tableUut.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.tableUut.resizeRowsToContents()
        self.tableUut.resizeColumnsToContents()
        self.init()
        self.editCompletionStatus.setText("")
        #self.resizeTableUut()
        self.measPsVoltages = None
        self.measPsCurrents = None

        #self.dutWatts = (self.maxNModules+1)*[0]
        #self.dutTemps = (self.maxNModules+1)*[0]
        #self.dutMaxWatts = (self.maxNModules+1)*[0]
        #self.dutMaxTemps = (self.maxNModules+1)*[0]
        #self.dutMinWatts = (self.maxNModules+1)*[0]
        #self.dutMinTemps = (self.maxNModules+1)*[0]

        self.duration = utils.ParseDuration(self.ini['burnin']['duration'])
        hours = self.duration // 3600
        minutes = (self.duration - hours * 3600) // 60
        seconds = self.duration - hours * 3600 - minutes * 60
        self.sduration = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        self.pollInterval = utils.ParseDuration(self.ini['burnin']['poll_interval'])
        self.nIterations = math.ceil(self.duration / self.pollInterval)
        self.currentIteration = 0
        self.timeOfLastTest = None
        self.startTime = None
        self.timeStamp = None
        self.thread = None
        self.bibs = []
        self.busy = False
        self.logDirName = 'logfiles'
        if not os.path.isdir(self.logDirName):
            os.mkdir(self.logDirName)
        self.logFileName = None
        self.f = None
        # TBD other variables needed for voltages, currents and temperatures
        # read from the DUTs over time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timerEvent)
        self.station_sw_revision = utils.gitRevText('..')
        self.Rev.setText("Rev: " + self.station_sw_revision)
        self.modules = []


    def dialogErrMsg(self, message):
        utils.ErrorMsg(message)


    def resizeTableUut(self):
        header = self.tableUut.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)


    def initTable(self):
        for x in range(0, 24):
            row = x
            col = 1
            self.tableUut.item(row, col-1).setBackground(self.colorBackground)
            for i in range(0,4):
                self.tableUut.item(row, col+i).setText('')
                self.tableUut.item(row, col+i).setBackground(self.colorBackground)
        for x in range(0, 24):
            row = x
            col = 6
            self.tableUut.item(row, col-1).setBackground(self.colorBackground)
            for i in range(0,4):
                self.tableUut.item(row, col+i).setText('')
                self.tableUut.item(row, col+i).setBackground(self.colorBackground)


    def buildTable(self):
        for x in range(0, 24):
            row = x
            col = 1
            for i in range(0,4):
                self.tableUut.setItem(row, col+i, QTableWidgetItem(''))
        for x in range(0, 24):
            row = x
            col = 6
            for i in range(0,4):
                self.tableUut.setItem(row, col+i, QTableWidgetItem(''))
        self.resizeTableUut()


    def init(self):
        self.tabWidget.setCurrentIndex(0)
        self.buttonBeginNewPcb.setEnabled(True)
        self.buttonStart.setEnabled(False)
        self.buttonDone.setEnabled(False)
        self.editTechnician.setText("")
        self.editNotes.setText("")
        self.labelStatus.setText("")
        self.initTable()
        self.state = 'Ready'
        self.statusText = ''
        self.passFail = None
        self.turnOffSupply()

    def setupThread(self):
        self.thread = QThread()

        # Step 3: Create a worker object
        self.worker = Worker(
            ini         = self.ini,
            bibs        = self.bibs,
            modules     = self.modules,
            logFileName = self.logFileName)

        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)

        # Step 5: Connect signals and slots
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.worker.setStatusText.connect(self.setStatusText)
        self.worker.displayModuleStatus.connect(self.displayModuleStatus)
        self.worker.resizeTableUut.connect(self.resizeTableUut)
        self.worker.dialogErrMsg.connect(self.dialogErrMsg)
        self.worker.clickStopandUpload.connect(self.clickStopandUpload)

    #========= Event Handlers ============

    #this timer event triggers whenever the specified poll interval is reached
    #if the previous poll has not finished executing nothing will happen as
    #opening the same thread at one time would be no good
    def timerEvent(self):

        # How long has it been since the last test was run?
        now = datetime.now()
        timeSinceLastTest = now - self.timeOfLastTest
        timeSinceLastTest_s = timeSinceLastTest.total_seconds()

        # Update the displayed run time
        run_time_s = math.floor(self.run_time + timeSinceLastTest_s)
        hours = run_time_s // 3600
        minutes = (run_time_s - hours * 3600) // 60
        seconds = run_time_s - hours * 3600 - minutes * 60
        self.labelStatus.setText(
            f"TIME: {hours:02d}:{minutes:02d}:{seconds:02d} out of {self.sduration}")

        # If enough time has past since the last test, start a new test
        if (timeSinceLastTest_s >= self.pollInterval):
            # If an old test is still running, quit for now
            if (self.busy):
                return

            with open(self.logFileName, "a") as self.f:
                self.f.write(f'\n*************** Iteration: {self.currentIteration+1} *******************\n')

            self.timeOfLastTest = now
            self.run_time += timeSinceLastTest_s

            # Start a new test thread
            self.busy = True

            self.setupThread()
            self.thread.started.connect(self.worker.runIteration)
            self.worker.finishedIteration.connect(self.iterationDone)
            self.thread.start()


    def keyPressEvent(self, e):
        """
        Handler for the keyPressEvent
        """
        # The only key that matters is the '\n' key which ends the string input.
        # This is used for the end of the tech ID text input.  When this is
        # reached, validate the name and prep the test for running.
        if e.key() == QtCore.Qt.Key_Enter - 1:
            tid = self.editTechnician.text()
            self.techId, name = utils.parseTechnicianId(tid)
            self.editTechnician.setText(name)
            if not self.techId:
                return

            #lock this text box now that data is correct
            self.editTechnician.setReadOnly(True)
            self.buttonStart.setEnabled(True)
            self.buttonStart.setFocus()

    #========= Slots ============
    def setStatusText(self, text):
        self.labelStatus.setText(text)
        app.processEvents()


    def displayModuleStatus(self, moduleStatus):
        module = moduleStatus[0]
        row, col = dutRowColumn(self.maxNModules, module.num)
        if module.fault:
            for i in range(-1,4):
                self.tableUut.item(row, col+i).setBackground(colorFault)
        else:
            for i in range(-1,4):
                self.tableUut.item(row, col+i).setBackground(colorOK)
        self.tableUut.item(row, col).setText(module.sn)
        self.tableUut.item(row, col+1).setText(f'{module.power_W:0.3f}')
        self.tableUut.item(row, col+2).setText(f'{module.temp_C:0.0f}')
        if module.fault:
            dutStatus = "FAULT"
        else:
            dutStatus = "OK"
        self.tableUut.item(row, col+3).setText(f'{dutStatus}')


    def startupDone(self, bibs, modules):
        self.bibs = bibs
        self.modules = modules
        self.timeOfLastTest = datetime.now()
        self.timer.start(1000)
        
    def killthread(self):
        self.thread = None
    #this is honestly unnecessary as thread.isRunning should do the same thing but there are cases online
    #of that failing so this is more just to be extra sure
    def busysignal(self):
        self.busy = not self.busy
        print(self.busy)

    #beautifully named function that does basically all of burn in
    #has a log file that logs everything
    #talks to all the boards for statuses
    def thewholething(self):
        #empty list to store the burn in status call-
        #This is neccessary becuase the info hear is needed later on in the
        #loop so it can't just be saved to the log file and ignored
        burnstat = []
        self.f = open(self.logFileName, 'a')

        self.f.write('\n')
        i= 1
        for BiB in self.BiB:
            self.f.write('Burnin Board: ' + str(i) + '\n')
            status = ''
            while(status == ''):
                try:
                    status = BiB.consoleIo("status")
                    split = status.split('\n')
                    if(split[1] == ' 1) Ous'):
                        status = ''
                except:
                    print('BiB ERR')

            self.f.write(status)
            self.f.write('\n')
            status = status.split('\n')
            i = i + 1

            burnstat.append(status)
        # self.f.close()
        # file = glob.glob('Temperature*')
        # print(file)
        # with open(file[0], 'r') as t:
            # for line in t:
                # print(line)
                # pass
            # last_line = line
        # self.f = open(self.logFileName, 'a')
        # temp = last_line.split()[2]
        # self.lineEditTemp.setText(temp)

        # aelf.f.write(f"Oven Temp:    {temp}")

        supplyV,supplyC,supplyP = utils.CheckPowerSupplyBurn(self.ini['burnin_power_supply']['port'])
        self.f.write(f"PowerSupply:\n V = {supplyV}, C = {supplyC}, P = {supplyP}\n\n")

        for module in self.module:
            sn = self.dutSn[module.num]
            if sn:
                if module.fault:
                    self.dutStatus[module.num] = 'FAULT'
                if not module.fault and self.dutStatus[module.num] == 'OK':
                    self.pollDutStatus(module)
                    index = self.BiB.index(module.biB)


                    current = burnstat[index][module.port].split()[3]
                    self.dutWatts[module.num] = current
                    self.dutStatus[module.num] = burnstat[index][module.port].split()[2]
                    if(self.dutStatus[module.num] == 'FAULT' or float(current) < 100):
                        module.biB.consoleIo(f"poweroff {module.port}")
                        module.biB.consoleIo('faulton')
                        self.dutStatus[module.num] = 'FAULT'
                        module.fault = True
                row, col = dutRowColumn(self.maxNModules, module.num)

                if(not module.fault):
                    self.tableUut.item(row, col-1).setBackground(QtGui.QColor(16, 239, 109))
                    self.tableUut.item(row, col).setBackground(QtGui.QColor(16, 239, 109))
                    self.tableUut.item(row, col+1).setBackground(QtGui.QColor(16, 239, 109))
                    self.tableUut.item(row, col+2).setBackground(QtGui.QColor(16, 239, 109))
                    self.tableUut.item(row, col+3).setBackground(QtGui.QColor(16, 239, 109))
                    self.tableUut.item(
                     row, col+1).setText(f'{float(self.dutWatts[module.num]):0.3f}')
                    self.tableUut.item(
                     row, col+2).setText(f'{float(self.dutTemps[module.num]):0.0f}')
                    self.tableUut.item(
                     row, col+3).setText(f'{self.dutStatus[module.num]}')
                    print(module.num)
                elif(module.fault):
                    self.tableUut.item(row, col-1).setBackground(QtGui.QColor(252, 33, 27))
                    self.tableUut.item(row, col).setBackground(QtGui.QColor(252, 33, 27))
                    self.tableUut.item(row, col+1).setBackground(QtGui.QColor(252, 33, 27))
                    self.tableUut.item(row, col+2).setBackground(QtGui.QColor(252, 33, 27))
                    self.tableUut.item(row, col+3).setBackground(QtGui.QColor(252, 33, 27))
                    self.tableUut.item(
                     row, col+1).setText('FAIL')
                    self.tableUut.item(
                     row, col+2).setText('FAIL')
                    self.tableUut.item(
                     row, col+3).setText(f'{self.dutStatus[module.num]}')
                self.resizeTableUut()
        self.busy = False
        nmodules = 0
        for module in self.modules:
            if module.sn and not module.fault:
                nmodules += 1
        if nmodules == 0:
            self.labelStatus.setText("No modules to test")
            self.testDone()
            return

        self.labelStatus.setText(f"TIME: 00:00:00 out of {self.sduration}")
        self.resizeTableUut()
        app.processEvents()

        #For the duration of the test, wait TBD seconds and poll the currents,
        # voltages and temperatures of each of the DUTs
        self.timeOfLastTest = datetime.now()
        


    def iterationDone(self):
        """
        Slot run at the end of the current test iteration
        """
        self.busy = False
        self.currentIteration += 1
        if self.currentIteration >= self.nIterations or self.stopRequested:
            # All the test iterations have been run, shut it all down
            self.testDone()


    @QtCore.pyqtSlot(name="on_MainWindow_resizeEvent")
    def resizeMainWindow(self):
        self.resizeTableUut()


    @QtCore.pyqtSlot(name="on_buttonBeginNewPcb_clicked")
    def clickBeginNewPcb(self):
        if self.state != 'Ready':
            doCancel = utils.RunCancelDialog()
            if doCancel:
                self.init()
            else:
                return
        self.state = 'Running'
        self.editCompletionStatus.setText("")
        app.processEvents()
        self.editTechnician.setReadOnly(False)
        self.editTechnician.setFocus()


    @QtCore.pyqtSlot(name="on_buttonStart_clicked")
    def clickStart(self):
        """
        Slot which starts tests running when the 'Start' button is clicked
        """
        self.buttonStart.setEnabled(False)
        self.labelStatus.setText("Powering up system ...")
        app.processEvents()
        self.stopRequested = False

        # Capture the current time which is used as the test start time and
        # will be used for the log file time stamp
        self.run_time = 0
        self.startTime = SqlFuncs.nowDateTime()
        self.timeStamp = SqlFuncs.datetimeToTimeStamp(self.startTime)
        self.logFileName = os.path.join(self.logDirName, f'BurnBook-{self.timeStamp}.txt')

        # Delete any files that are in the data directory
        files = glob.glob(os.path.join(self.logDirName, "*"))
        for file in files:
            pass # TBD LEAVE THE FILE FOR NOW os.remove(file)

        self.measPsVoltages = (self.nIterations+1)*[0]
        self.measPsCurrents = (self.nIterations+1)*[0]

        with open(self.logFileName, "w") as self.f:
            self.f.write('StartTime : ' + self.startTime + '\n' )
            self.f.write('Duration: ' + self.sduration +'\n' )
            self.f.write('\n\n')

            self.f.write('***************On StartUp*******************\n')
            self.currentIteration = 0

            print("Powering up ...")
            ok = self.turnOnSupply()
            time.sleep(1)
            if not ok:
                # Failure in the main supply
                return

        self.setupThread()
        self.thread.started.connect(self.worker.runStartUp)
        self.worker.finishedStartup.connect(self.startupDone)
        self.thread.start()

    def testDone(self):
        self.timer.stop()
        for BiB in self.bibs:
            BiB.consoleIo(("poweroff all"))

        self.turnOffSupply()

        moduleStatus = ["PASS", "FAIL"]
        bibId = ["A","B","C","D"]
        with open(self.logFileName, "a") as fp:
            # Count the number of pass and fail duts
            numpass = 0
            nmodules = 0
            for module in self.modules:
                if module.fault:
                    # The module was present but failed current
                    nmodules += 1
                elif module.sn:
                    # The module passed
                    nmodules += 1
                    numpass += 1
                if module.sn:
                    fp.write(f"{bibId[module.bibIndex]}.{module.num} {module.sn} {moduleStatus[module.fault]}"+"\n")

        self.labelStatus.setText(
            f"{numpass} out of {nmodules} PASSED")

        # When time is done, enable the DONE button
        self.buttonDone.setEnabled(True)
    def pollDutStatus(self,module):
        # Read the DUTs currents, voltages and temperatures
            #gonna check the status to make sure shes doing okay
        if(module.fault == True):
            return

        sn = self.dutSn[module.num]
        self.f.write(sn + ' ' +  utils.GetDateTime() + '\n')


        hours = self.run_time // 3600
        minutes = (self.run_time - hours * 3600) // 60
        seconds = self.run_time - hours * 3600 - minutes * 60
        self.f.write(f"Elapsed Time: {hours:02d}:{minutes:02d}:{seconds:02d} \n\n")

        try:
            temps = module.com.consoleIo(f'rd tmon')
            iv = utils.GetRdiv(module.com)
            rdv = utils.GetRdv(module.com)
        except:
            module.fault = True
            self.f.write('ERR: Could not read Serial Powering down board\n')
            module.biB.consoleIo(f"poweroff {module.port}")
            module.biB.consoleIo('faulton')
            self.dutStatus[module.num] = 'FAULT'
            self.f.close()
            return

        ok1 = utils.UpdateIv(self.iv_info, self.ini, iv)
        if not ok1:
            for supply in self.iv_info.keys():
                for param in ['mA', 'mV']:
                    if not self.iv_info[supply][param]['Ok']:
                        v = self.iv_info[supply][param]['Value']
                        lo = self.iv_info[supply][param]['Low']
                        hi = self.iv_info[supply][param]['High']
                        txt = f"\nSupply {supply}: {v} {param} out of range {lo} to {hi} {param} "
                        module.fault=True
                        self.f.write(txt)

        ok2 = utils.UpdateV(self.v_info, self.ini, rdv)
        if not ok2:
            for supply in self.v_info.keys():
                if not self.v_info[supply]['Ok']:
                    v = self.v_info[supply]['Value']
                    lo = self.v_info[supply]['Low']
                    hi = self.v_info[supply]['High']
                    txt = f"\nSupply {supply}: {v} {param} out of range {lo} to {hi} {param} "
                    module.fault = True
                    self.f.write(txt)

        if module.fault:
            module.fault = True
            self.f.write('ERR: over Current or Voltage \n')
            module.biB.consoleIo(f"poweroff {module.port}")
            module.biB.consoleIo('faulton')
            self.dutStatus[module.num] = 'FAULT'




        self.f.write('Temps:\n' + temps + '\n')
        temps = temps.split('\n')





        #self.dutWatts[module.num] = current
        self.dutTemps[module.num] = temps[0].split()[1]
        # TBD self.dutMaxWatts
        # TBD self.dutMaxTemps
        # TBD self.dutMinWatts
        # TBD self.dutMinTemps
        # TBD other variables needed for voltages, currents and temperatures
        # read from the DUTs over time
        num = module.num

        ivfixxed = str(iv).replace('},','\n')
        ivfixxed = ivfixxed.replace("}}","\n")
        ivfixxed = ivfixxed.replace("{","")
        ivfixxed = ivfixxed.replace("'","")
        self.f.write('IV:\n ')
        self.f.write(ivfixxed)


    @QtCore.pyqtSlot(name="on_buttonDone_clicked")
    def clickDone(self):
        self.buttonDone.setEnabled(False)

        # Update the database
        text = "Updating Database ..."
        self.editCompletionStatus.setText(text)
        app.processEvents()

        self.updateDatabase()

        text += " Done"
        self.editCompletionStatus.setText(text)
        app.processEvents()

        # Get ready for the next test
        self.init()


    @QtCore.pyqtSlot(name="on_ButtonStopandUpload_clicked")
    def clickStopandUpload(self):
        self.stopRequested = True


    def updateDatabase(self):
        # There are two databases used for Burn-in.  One table is used for each
        # burn-in lot and the other table holds separate entries for each module
        data = {}
        self.passFail = 'PASS'
        data['tech_id'] = str(self.techId)
        data['station_sw_revision'] = "'" + self.station_sw_revision + "'"
        data['start_date_time'] = "'" + self.startTime + "'"
        data['end_date_time'] = "'" + SqlFuncs.nowDateTime() + "'"
        data['pass_fail'] = "'" + self.passFail + "'"
        data['notes'] = "'" + self.editNotes.toPlainText() + "'"
        data['data_dir'] = "'" + os.path.join('BurnIn', os.path.basename(self.logFileName)) + "'"
        SqlFuncs.updateTetraBurnIn(data)

        lotId = SqlFuncs.lookupTetraBurnLotId(self.startTime)
        with open(self.logFileName, 'a') as self.f:
            for module in self.modules:
                data1 = {}
                if not module.asyId:
                    continue
                if module.fault:
                    passFail = "Fail"
                else:
                    passFail = "Pass"
                data1['DUTSN'] = "'" + str(module.sn) + "'"
                self.f.write("**********************************************************\n")
                self.f.write(f"Serial Number: {module.sn} at location {module.bibIndex}\n")
                data1['lot_id'] = "'" + str(lotId) + "'"
                self.f.write(f"lot_id: {lotId}\n")
                data1['asy_id'] = "'" + str(module.asyId) + "'"
                self.f.write(f"asy_id = {module.asyId}\n")
                data1['pass_fail'] = "'" + passFail + "'"
                SqlFuncs.updateTetraBurnInasy(data1)
                SqlFuncs.ModulepostBurn(module.sn,lotId,passFail)

        # Copy the local log file to the remote directory and remove the local
        # copy
        remoteFolder = self.ini['database']['remote_folder']
        dest = shutil.copy2(self.logFileName, remoteFolder)

    def turnOnSupply(self):
        statusText = "Turning on power supply ... "
        self.labelStatus.setText(statusText)

        ## Turn on the supply
        ps_port = self.ini['burnin_power_supply']['port']
        ps_volt = float(self.ini['burnin_power_supply']['voltage'])
        print("VOLTAGE" + str(ps_volt))
        ps_curr = float(self.ini['burnin_power_supply']['current'])
        OVolt = (self.ini['burnin_power_supply']['OVolt'])
        errMsg,measVolt,measCurr = utils.TurnOnPowerSupplyBurn(ps_port, ps_volt, ps_curr,OVolt)
         # Verify everything went OK
        ok = errMsg == ''
        
        if ok:
            # Verify limits, TBD
            statusText += "Done"
        else:
            statusText += err_msg

        # Display the status
        self.labelStatus.setText(statusText)
        return ok


    def turnOffSupply(self):
        statusText = "Turning off power supply ... "
        self.labelStatus.setText(statusText)

        ## Turn off the supply
        psPort = self.ini['burnin_power_supply']['port']
        ok, err_msg = utils.TurnOffPowerSupplyBurn(psPort)
        if ok:
            statusText += "Done"
        else:
            statusText += err_msg

        # Display the status
        self.labelStatus.setText(statusText)
        return ok


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    app.aboutToQuit.connect(win.turnOffSupply)
    win.show()
    sys.exit(app.exec())