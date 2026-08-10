import xml.etree.ElementTree as ET

def parse_int(v):
    try:
        v = v.lower().strip()
        if v.startswith("0x"):
            v = int(v[2:], 16)
        else:
            v = int(v)
    except:
        print("Parsing (%s)" % v)
    return v

class DeviceRegisterBitField():
    def __init__(self, offset, sz, name, parent=None):
        self.Parent = parent
        self.Offset = offset
        self.Size = sz
        self.Name = name

    def dump(self):
        print(self.Offset, self.Size, self.Name)

    def value(self):
        regValue = self.Parent.Value
        return (regValue >> self.Offset) & (2**self.Size-1)

    def setValue(self, value):
        regValue = self.Parent.Value
        mask = (2**self.Size-1)
        regValue &= ~(mask << self.Offset)
        regValue += (value & mask) << self.Offset
        self.Parent.setValue(regValue)

class DeviceRegister():
    def __init__(self, address, sz, name, typ, comm):
        self.Address = address
        self.Size = sz
        self.Name = name
        self.Typ = typ
        self.Comm = comm
        self.BitFields = None
        self.BitFieldsByName = {}
        self.Value = 0
        self.HwValue = -1

    def addBitField(self, offset, sz, name):
        bf = DeviceRegisterBitField(offset, sz, name, self)
        if self.BitFields is None:
            self.BitFields = [bf]
        else:
            self.BitFields.append(bf)
        self.BitFieldsByName[name] = bf

    def dump(self):
        print("0x%X" % self.Address, self.Size, self.Name, "0x%X" % self.Value)
        if not self.BitFields is None:
            for bf in self.BitFields:
                bf.dump()

    def setValue(self, value):
        if isinstance(value, str):
            value = parse_int(value)
        self.Value = value

    def value(self):
        return self.Value

    def __getitem__(self, key):
        return self.BitFieldsByName[key]

    def write(self, value=None):
        if not value is None:
            self.Value = value
        if self.Typ == "fpd":
            cmdText = "i2c 14 wr 0x%x 0x%x" % (self.Address, self.Value)
        else:
            cmdText = "wr %s 0x%x 0x%x" % (self.Typ, self.Address, self.Value)
        self.Comm.consoleIo(cmdText)
        self.HwValue = self.Value

    def read(self):
        if self.Typ == "fpd":
            cmdText = "i2c 14 wr 0x%x rd 1" % self.Address
        else:
            cmdText = "rd %s 0x%x" % (self.Typ, self.Address)
        resp = self.Comm.consoleIo(cmdText)
        fields = resp.split(':')
        if len(fields) != 2:
            print("Bad", resp)
        value = parse_int(fields[1])
        self.Value = value
        self.HwValue = value

class DeviceRegisters():
    def __init__(self, typ, comm, path=None):
        self.Typ = typ
        self.Comm = comm
        self.RegsByAddress = {}
        self.RegsByName = {}
        if path:
            self.loadXmlDefinitions(path)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.RegsByAddress[key]
        return self.RegsByName[key]

    def loadXmlDefinitions(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        regs = {}
        for etreg in root.iter('register'):
            sz = 16
            if 'size' in etreg.attrib:
                sz = parse_int(etreg.attrib['size'])
            offset = parse_int(etreg.attrib['offset'])
            reg = DeviceRegister(offset, 16, etreg.attrib['name'], self.Typ, self.Comm)
            for etbf in etreg.iter('bitfield'):
                try:
                    low = int(etbf.attrib['low'])
                except:
                    print("What;s up?", etbf.attrib['low'])
                    raise
                high = int(etbf.attrib['high'])
                sz = high - low + 1
                reg.addBitField(int(etbf.attrib['low']), sz, etbf.attrib['name'])
            regs[offset] = reg
        self.RegsByAddress = regs
        for reg in self.RegsByAddress.values():
            self.RegsByName[reg.Name] = reg

    def save(self, file_path):
        with open(file_path, "w") as fp:
            for addr,reg in self.RegsByAddress.items():
                fp.write("0x%X,0x%X\n" % (reg.Address, reg.Value))

    def load(self, file_path):
        with open(file_path, "r") as fp:
            for line in fp:
                fields = line.split(',')
                address = parse_int(fields[0])
                value = parse_int(fields[1])
                try:
                    self.RegsByAddress[address].Value = value
                except:
                    print('%x' % address)

    def writeAll(self):
        self.Comm.open()
        for reg in self.RegsByAddress.values():
            reg.write()
        self.Comm.close()

    def readAll(self):
        self.Comm.open()
        for reg in self.RegsByAddress.values():
            reg.read()
        self.Comm.close()

    def dump(self):
        print(self.Typ)
        for reg in self.RegsByAddress.values():
            reg.dump()

if __name__ == "__main__":
    # For testing purposes
    from RageComm import RageComm
    comm = RageComm("<OFFLINE>")
    fpga_regs = DeviceRegisters('reg', comm, 'Regs/fpga_registers.xml')
    reg = fpga_regs['FPGA Control']
    print(reg.value())
    fpga_regs['FPGA Control']['LED ON/OFF'].setValue(1)
    print(reg.value())
    print(fpga_regs['FPGA Control']['LED ON/OFF'].value())
    reg.write()

