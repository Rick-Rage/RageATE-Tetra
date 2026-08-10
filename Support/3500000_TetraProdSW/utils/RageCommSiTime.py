import serial
import serial.tools.list_ports
import time

class RageComm:
    def __init__(self, portName=None, errorOut=None, debugOut=None, sim=None, baudRate=115200):
        self.PortName = portName
        self.BaudRate = baudRate
        self.ErrorOut = errorOut
        self.DebugOut = debugOut
        self.Sim = sim
        self.Serial = None

    def getPorts(self):
        validPorts = []
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if not port.vid or not port.pid:
                continue
            if (port.vid == int('403', 16)) and ((port.pid == int('6010', 16)) or (port.pid == int('6001', 16))):
                validPorts.append(port.device)
        if self.Sim:
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
        ser.baudrate = self.BaudRate
        ser.port = self.PortName
        ser.timeout = 5
        for i in range(0,5):
            try:
                ser.open()
                return ser
            except:
                if self.ErrorOut:
                    self.ErrorOut("Error Opening serial port")
            time.sleep(1)
        return None

    def open(self):
        if self.Serial:
            return self.Serial
        self.Serial = self.localOpen()
        return self.Serial

    def consoleIo(self, cmdText):
        a = -1
        resp = ''
        # Display command
        if self.DebugOut:
            self.DebugOut('>' + cmdText)
        # if it is offline, return 0
        if self.PortName == "<OFFLINE>":
            resp = self.Sim(cmdText)
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
                    raise
                if not self.Serial:
                    ser.close()
                    self.Serial = None
            except:
                raise
        if resp and self.DebugOut:
            self.DebugOut(resp)
        return resp

if __name__ == '__main__':
    import sys
    com = RageComm()
    p = com.getPorts()
    if p:
        com.setPortName(p[0])
        print("Found", p[0])
