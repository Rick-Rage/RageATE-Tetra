import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import QMessageBox
import time
from TetraSim import TetraSim

def showComPortErrorDialog():
   msg = QMessageBox()
   msg.setIcon(QMessageBox.Warning)
   msg.setText("Error opening console")
   msg.setWindowTitle("Console Error")
   msg.setStandardButtons(QMessageBox.Ok)	
   retval = msg.exec_()

class RageComm:
    def __init__(self, portName=None, debugOut=None):
        self.PortName = portName
        self.DebugOut = debugOut
        self.Serial = None
        self.Sim = TetraSim()
        self.IgnoreError = False

    def setDebugOut(self, debugOut):
        self.DebugOut = debugOut

    def getPorts(self):
        validPorts = []
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if not port.vid or not port.pid:
                continue
            print('%x %x' % (port.vid, port.pid))
            if (port.vid == int('403', 16)) and ((port.pid == int('6010', 16)) or (port.pid == int('6001', 16))):
                validPorts.append(port.device)
        validPorts.append("<OFFLINE>")
        return validPorts

    def setPortName(self, name):
        self.PortName = name

    def close(self):
        if self.Serial:
            if self.Serial != self.PortName:
                self.Serial.close()
            self.Serial = None

    def localOpen(self):
        if self.PortName == "<OFFLINE>":
            return self.PortName
        if self.Serial:
            return self.Serial
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.port = self.PortName
        ser.timeout = 5
        for i in range(0,5):
            try:
                ser.open()
                return ser
            except:
                if not self.IgnoreError:
                    showComPortErrorDialog()
            time.sleep(1)
        return None

    def open(self):
        if self.Serial:
            return self.Serial
        self.Serial = self.localOpen()
        return self.Serial

    def consoleIo(self, cmdText, ignoreError=False):
        a = -1
        resp = ''
        # Display command
        if self.DebugOut:
            self.DebugOut.appendPlainText('>' + cmdText)
        else:
            print(cmdText)
        # if it is offline, return 0
        if self.PortName == "<OFFLINE>":
            resp = self.Sim.consoleIo(cmdText)
        else:
            ser = self.localOpen()
            if not ser:
                return None
            try:
                ser.write(cmdText.encode('utf-8') + b'\n')
                #ser.flush()
                try:
                    state = 0
                    done = False
                    while not done:
                        cmd = ser.read(1)
                        if cmd == b'>':
                            # Ready for next command
                            if resp and (resp[-1] == '\n'):
                                resp = resp[:-1]
                            done = True
                        elif (state == 0) and (cmd == b'\n'):
                            # end of command
                            state = 1
                        elif cmd == b'\r': 
                            pass
                        elif state == 1:
                            # Receiving response, convert to unicode
                            resp += cmd.decode("utf-8")
                except:
                    if ignoreError:
                        return None
                    else:
                        raise
                if not self.Serial:
                    ser.close()
                    self.Serial = None
            except:
                raise
        if resp and self.DebugOut:
            self.DebugOut.appendPlainText(resp)
        return resp

if __name__ == '__main__':
    from PyQt5.QtWidgets import *
    import sys
    app = QApplication(sys.argv)
    w = QPlainTextEdit()
    com = RageComm(w)
    p = com.getPorts()
    if p:
        com.setPortName(p[0])
        print("Found", p[0])
        resp = com.consoleIo("help")
        resp = com.consoleIo("verbose 1")
        resp = com.consoleIo("verbose")
        resp = com.consoleIo("verbose 0")
        resp = com.consoleIo("verbose")
    w.setWindowTitle('Testing RageComm')
    w.show()
    sys.exit(app.exec_())
