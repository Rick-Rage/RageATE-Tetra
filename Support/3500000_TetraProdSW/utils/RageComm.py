from datetime import datetime
from tkinter import EXCEPTION
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import QMessageBox
import time
#from TetraSim import TetraSim

def showComPortErrorDialog():
   msg = QMessageBox()
   msg.setIcon(QMessageBox.Warning)
   msg.setText("Error opening console")
   msg.setWindowTitle("Console Error")
   msg.setStandardButtons(QMessageBox.Ok)
   retval = msg.exec_()

class RageComm:
    def __init__(self, portName=None,Baudrate=115200, debugOut=None):
        self.PortName = portName
        self.DebugOut = debugOut
        self.Serial = None
        #self.Sim = TetraSim()
        self.IgnoreError = False
        self.Baudrate = Baudrate
        self.Timeout = 20

    def setDebugOut(self, debugOut):
        self.DebugOut = debugOut

    def getPorts(self):
        validPorts = []
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if not port.vid or not port.pid:
                continue
            print('%x %x' % (port.vid, port.pid))
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
        ser.baudrate = self.Baudrate
        ser.port = self.PortName
        ser.timeout = 0 # Don't wait at all
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
                print("not ser")
                return (None)
            try:
                ser.reset_input_buffer()
                text = cmdText.encode('utf-8') + b'\n'
                ser.write(text)
                try:
                    state = 0
                    done = False
                    t0 = datetime.now()
                    while not done:
                        cmd = ser.read(1)
                        if len(cmd) == 0:
                            # Look for 5 second timeout
                            t1 = datetime.now()
                            t = t1 - t0
                            if t.total_seconds() > self.Timeout:
                                raise serial.SerialTimeoutException
                            continue
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
                       
                        if(cmdText == 'status' and cmd == b''):
                            ser.close()
                            
                            
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
        
        

    def boot(self, look_for="ADCSYNC FAILED"):
        resp = ''

        if self.PortName == "<OFFLINE>":
            print("Device is offline. Cannot listen for boot-up message.")
            return None

        ser = self.localOpen()

        if not ser:
            print("Could not open serial connection.")
            return None

        try:
            # Wait for 30 seconds to either see ">" or "ADCSYNC FAILED"
            t0 = datetime.now()
            text = b'\n'
            ser.write(text)
            additional_wait = False
            while True:
                cmd = ser.read(1)
                time.sleep(.075)
                # Check for 30-second timeout
                if (datetime.now() - t0).total_seconds() > 30:
                    print("Timeout waiting for '>' or 'ADCSYNC FAILED'.")
                    ser.close()
                    return "Error: Neither '>' nor 'ADCSYNC FAILED' found in 30 seconds."

                if len(cmd) == 0:
                    continue

                # Accumulate the response and look for the specific string
                resp += cmd.decode("utf-8")
                time.sleep(.075)
                if ">" in resp:
                    print("Found '>' within 30 seconds.")
                    ser.close()
                    return resp

                if look_for in resp:
                    print(f"Found specific message: {look_for}")
                    additional_wait = True
                    break

            # If "ADCSYNC FAILED" was found, wait an additional 2 minutes for ">"
            if additional_wait:
                t0 = datetime.now()
                while True:
                    cmd = ser.read(1)

                    # Check for 2-minute timeout
                    if (datetime.now() - t0).total_seconds() > 180:
                        print("Timeout waiting for '>'.")
                        ser.close()
                        return "Error: '>' not found in 2 minutes after 'ADCSYNC FAILED'."

                    if len(cmd) == 0:
                        continue

                    resp += cmd.decode("utf-8")
                    if ">" in resp:
                        print("Found '>' after 'ADCSYNC FAILED'")
                        ser.close()
                        return resp

        except serial.SerialTimeoutException:
            print("Timeout")
            ser.close()
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            ser.close()
            return None

        ser.close()
        return resp
    
    def Ping(self, ignoreError=False, timeout=None):
        if not timeout:
            timeout = self.Timeout
        ser = self.localOpen()
        if not ser:
            return False
        ser.reset_input_buffer()
        ser.write(b'\n')
        t0 = datetime.now()
        while True:
            time.sleep(0.01)
            if ser.in_waiting > 0:
                cmd = ser.read(1)
                if cmd == b'>':
                    return True
            else:
                # Look for N second timeout
                t = datetime.now() - t0
                if t.total_seconds() > timeout:
                    return False

if __name__ == '__main__':
    from PyQt5.QtWidgets import *
    import sys
    
    com = RageComm('COM6')
    com.boot()
    p = com.getPorts()
    print(p)

