import RageComm
from TetraRegisters import parse_int

class TetraSim():
    def __init__(self):
        self.name = "tom"
        self.FpgaRegs = 256*[0]
        self.Txm1Regs = 258*[0]
        self.Txm2Regs = 258*[0]
        self.Txm3Regs = 258*[0]
        self.Rxm1Regs = 258*[0]
        self.Rxm2Regs = 258*[0]
        self.Adc1Regs = 256*[0]
        self.Adc2Regs = 256*[0]
        self.GpioRegs = 8*[0]

        self.AntTable = [0]
        self.TxFilter1Table = [0]
        self.TxFilter2Table = [0]
        self.RxFilterTable = [0]
        self.IndexTable0 = [0]
        self.IndexTable1 = [0]
        self.IndexTable2 = [0]
        self.IndexTable3 = [0]

    def consoleIo(self, cmdText):
        fields = [field.strip() for field in cmdText.split()]
        if fields[0] == 'wr':
            offset = parse_int(fields[2])
            value = parse_int(fields[3])
            if fields[1] == "reg":
                self.FpgaRegs[offset] = value
            elif fields[1] == "txm1" or fields[1] == "txm":
                self.Txm1Regs[offset] = value
            elif fields[1] == "txm2":
                self.Txm2Regs[offset] = value
            elif fields[1] == "txm3":
                self.Txm3Regs[offset] = value
            elif fields[1] == "rxm1":
                self.Rxm1Regs[offset] = value
            elif fields[1] == "rxm2":
                self.Rxm2Regs[offset] = value
            elif fields[1] == "adc1":
                self.Adc1Regs[offset] = value
            elif fields[1] == "adc2":
                self.Adc2Regs[offset] = value
            elif fields[1] == "gpio":
                self.GpioRegs[offset] = value
            elif fields[1] == "table":
                tableId = offset
                values = parse_int(fields[3:])
                print(cmdText, tableId) # TBD
                if tableId == 3:
                    self.AntTable = values
                elif tableId == 16:
                    self.IndexTable0 = values
                elif tableId == 17:
                    self.IndexTable1 = values
                elif tableId == 18:
                    self.IndexTable2 = values
                elif tableId == 19:
                    self.IndexTable3 = values
                elif tableId == 20:
                    self.TxFilter1Table = values
                elif tableId == 21:
                    self.TxFilter2Table = values
                elif tableId == 22:
                    self.RxFilterTable = values
                else:
                    return "ERR"
            else:
                return "ERR"
            return ""
        elif fields[0] == 'rd':
            count = 1
            offset = parse_int(fields[2])
            if len(fields) == 4:
                count = parse_int(fields[3])
            if fields[1] == "reg":
                value = self.FpgaRegs[offset]
            elif fields[1] == "txm1" or fields[1] == "txm":
                value = self.Txm1Regs[offset]
            elif fields[1] == "txm2":
                value = self.Txm2Regs[offset]
            elif fields[1] == "txm3":
                value = self.Txm3Regs[offset]
            elif fields[1] == "rxm1":
                value = self.Rxm1Regs[offset]
            elif fields[1] == "rxm2":
                value = self.Rxm2Regs[offset]
            elif fields[1] == "adc1":
                value = self.Adc1Regs[offset]
            elif fields[1] == "adc2":
                value = self.Adc2Regs[offset]
            elif fields[1] == "gpio":
                value = self.GpioRegs[offset]
            elif fields[1] == "table":
                tableId = offset
                if tableId == 3:
                    values = self.AntTable
                elif tableId == 16:
                    values = self.IndexTable0
                elif tableId == 17:
                    values = self.IndexTable1
                elif tableId == 18:
                    values = self.IndexTable2
                elif tableId == 19:
                    values = self.IndexTable3
                elif tableId == 20:
                    values = self.TxFilter1Table
                elif tableId == 21:
                    values = self.TxFilter2Table
                elif tableId == 22:
                    values = self.RxFilterTable
                else:
                    return "ERR"
                text = "0x0:"
                for value in values:
                    text += " 0x%04X" % value
                return text
            else:
                return "ERR"
            return "0x%x: 0x%x" % (offset, value)
        return "ERR"


if __name__ == '__main__':
    import sys
    com = RageComm.RageComm()
    com.Sim = TetraSimIO()
    p = com.getPorts()
    com.setPortName(p[-1])
    print(com.consoleIo("wr reg 0x80 0x55"))
    print(com.consoleIo("rd reg 0x80"))
