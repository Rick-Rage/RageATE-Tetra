#######################################################################
# Usage: VerifySiTime.py <sn> <dir>
#
#  Reads the SiTime registers from the DUT attached via serial.  The
#  register values are written to the file <dir>/<sn>.txt.  The <dir>
#  directory must already exist.  The output file is then compared to
#  the wamGood.txt file.  If they match, the program prints "PASS",
#  otherwise it prints "FAIL"
#######################################################################

from RageCommSiTime import RageComm

def DebugOut(txt):
    lines = txt.split('\n')
    for line in lines:
        print(fp, "DBG:", line)

def ErrorOut(txt):
    lines = txt.split('\n')
    for line in lines:
        print("ERR!", line)

def printLine(fp, comm, cmd):
    fp.write(f"> {cmd}\n")
    fields = cmd.split()
    addr = fields[3]
    resp = comm.consoleIo(cmd)
    fields = resp.split(':')
    ans = fields[1]
    fp.write(f"{addr}:{ans}\n")
    

def test(comm, path):
    with open(path, "w") as fp:
        # Page 0
        printLine(fp, comm, 'pmb 0x69 wr 0xff 0')
        printLine(fp, comm, 'pmb 0x69 wr 0x01 rd 9')  # 0x00-0x08
        printLine(fp, comm, 'pmb 0x69 wr 0x0F rd 11') # 0x0F-0x19
        printLine(fp, comm, 'pmb 0x69 wr 0x23 rd 6')  # 0x23-0x28
        printLine(fp, comm, 'pmb 0x69 wr 0xD0 rd 2')  # 0xD0-0xD1
        printLine(fp, comm, 'pmb 0x69 wr 0xFE rd 1')  # 0xFE
        # Page 1
        printLine(fp, comm, 'pmb 0x69 wr 0xff 1')
        printLine(fp, comm, 'pmb 0x69 wr 0x02 rd 3')  # 0x02-0x04
        printLine(fp, comm, 'pmb 0x69 wr 0x06 rd 3')  # 0x06-0x08
        printLine(fp, comm, 'pmb 0x69 wr 0x0D rd 3')  # 0x0D-0x0F
        printLine(fp, comm, 'pmb 0x69 wr 0x11 rd 16') # 0x11-0x20
        printLine(fp, comm, 'pmb 0x69 wr 0x21 rd 16') # 0x21-0x30
        printLine(fp, comm, 'pmb 0x69 wr 0x31 rd 16') # 0x31-0x40
        printLine(fp, comm, 'pmb 0x69 wr 0x41 rd 6')  # 0x41-0x46
        printLine(fp, comm, 'pmb 0x69 wr 0x49 rd 7')  # 0x49-0x4F
        # Page 2
        printLine(fp, comm, 'pmb 0x69 wr 0xff 2')
        printLine(fp, comm, 'pmb 0x69 wr 0x0F rd 1')  # 0x0F
        printLine(fp, comm, 'pmb 0x69 wr 0x10 rd 16') # 0x10-0x1F
        printLine(fp, comm, 'pmb 0x69 wr 0x20 rd 16') # 0x20-0x2F
        printLine(fp, comm, 'pmb 0x69 wr 0x30 rd 16') # 0x30-0x3F
        printLine(fp, comm, 'pmb 0x69 wr 0x40 rd 16') # 0x40-0x4F
        # Page 3
        printLine(fp, comm, 'pmb 0x69 wr 0xff 3')
        printLine(fp, comm, 'pmb 0x69 wr 0x0F rd 1')  # 0x0F
        printLine(fp, comm, 'pmb 0x69 wr 0x10 rd 6')  # 0x10-0x16
        printLine(fp, comm, 'pmb 0x69 wr 0x17 rd 1')  # 0x17
        printLine(fp, comm, 'pmb 0x69 wr 0x18 rd 6')  # 0x18-0x1D
        printLine(fp, comm, 'pmb 0x69 wr 0x1F rd 1')  # 0x1F
        printLine(fp, comm, 'pmb 0x69 wr 0x20 rd 6')  # 0x20-0x26
        printLine(fp, comm, 'pmb 0x69 wr 0x27 rd 1')  # 0x27
        printLine(fp, comm, 'pmb 0x69 wr 0x28 rd 6')  # 0x28-0x2D
        printLine(fp, comm, 'pmb 0x69 wr 0x2F rd 1')  # 0x2F
        printLine(fp, comm, 'pmb 0x69 wr 0x30 rd 6')  # 0x30-0x36
        printLine(fp, comm, 'pmb 0x69 wr 0x37 rd 1')  # 0x37
        printLine(fp, comm, 'pmb 0x69 wr 0x38 rd 6')  # 0x38-0x3D
        printLine(fp, comm, 'pmb 0x69 wr 0x3F rd 1')  # 0x3F
        printLine(fp, comm, 'pmb 0x69 wr 0x40 rd 6')  # 0x40-0x46
        printLine(fp, comm, 'pmb 0x69 wr 0x47 rd 1')  # 0x47
        printLine(fp, comm, 'pmb 0x69 wr 0x48 rd 6')  # 0x48-0x4D
        printLine(fp, comm, 'pmb 0x69 wr 0x4F rd 1')  # 0x4F
        printLine(fp, comm, 'pmb 0x69 wr 0x50 rd 6')  # 0x50-0x56
        printLine(fp, comm, 'pmb 0x69 wr 0x57 rd 1')  # 0x57
        printLine(fp, comm, 'pmb 0x69 wr 0x5F rd 1')  # 0x5F
        printLine(fp, comm, 'pmb 0x69 wr 0x60 rd 6')  # 0x60-0x66
        printLine(fp, comm, 'pmb 0x69 wr 0x67 rd 1')  # 0x67
        printLine(fp, comm, 'pmb 0x69 wr 0x68 rd 6')  # 0x68-0x6D
        printLine(fp, comm, 'pmb 0x69 wr 0x6F rd 1')  # 0x6F
        printLine(fp, comm, 'pmb 0x69 wr 0xF2 rd 11') # 0xF2-0xFB
        # Page A
        printLine(fp, comm, f'pmb 0x69 wr 0xff 10')
        printLine(fp, comm, 'pmb 0x69 wr 0x00 rd 9')  # 0x00-0x08
        printLine(fp, comm, 'pmb 0x69 wr 0x10 rd 16') # 0x10-0x1F
        printLine(fp, comm, 'pmb 0x69 wr 0x20 rd 16') # 0x20-0x2F
        printLine(fp, comm, 'pmb 0x69 wr 0x30 rd 8')  # 0x30-0x37
        printLine(fp, comm, 'pmb 0x69 wr 0xD0 rd 2')  # 0xD0-0xD1
        # Page B
        printLine(fp, comm, f'pmb 0x69 wr 0xff 11')
        printLine(fp, comm, 'pmb 0x69 wr 0x00 rd 9')  # 0x00-0x08
        printLine(fp, comm, 'pmb 0x69 wr 0x10 rd 16') # 0x10-0x1F
        printLine(fp, comm, 'pmb 0x69 wr 0x20 rd 16') # 0x20-0x2F
        printLine(fp, comm, 'pmb 0x69 wr 0x30 rd 8')  # 0x30-0x37
        printLine(fp, comm, 'pmb 0x69 wr 0xD0 rd 2')  # 0xD0-0xD1
        # Page C
        printLine(fp, comm, f'pmb 0x69 wr 0xff 12')
        printLine(fp, comm, 'pmb 0x69 wr 0x00 rd 9')  # 0x00-0x08
        printLine(fp, comm, 'pmb 0x69 wr 0x10 rd 16') # 0x10-0x1F
        printLine(fp, comm, 'pmb 0x69 wr 0x20 rd 16') # 0x20-0x2F
        printLine(fp, comm, 'pmb 0x69 wr 0x30 rd 8')  # 0x30-0x37
        printLine(fp, comm, 'pmb 0x69 wr 0xD0 rd 2')  # 0xD0-0xD1
        # Page C
        printLine(fp, comm, f'pmb 0x69 wr 0xff 13')
        printLine(fp, comm, 'pmb 0x69 wr 0x00 rd 9')  # 0x00-0x08
        printLine(fp, comm, 'pmb 0x69 wr 0x10 rd 16') # 0x10-0x1F
        printLine(fp, comm, 'pmb 0x69 wr 0x20 rd 16') # 0x20-0x2F
        printLine(fp, comm, 'pmb 0x69 wr 0x30 rd 8')  # 0x30-0x37
        printLine(fp, comm, 'pmb 0x69 wr 0xD0 rd 2')  # 0xD0-0xD1
def main(args):
    import sys
    import filecmp
    comm = RageComm(debugOut=None, errorOut=ErrorOut)
    ports = comm.getPorts()
    comm.setPortName(ports[0])
    comm.open()
    sn = args[0]
    if len(sys.argv) > 2:
        dir = args[1]
    else:
        dir = '.'
    path = 'C:\\3500000_TetraProdSW\\utils\\test.txt'
    test(comm, path)
    comm.close()
    print(path)
    if filecmp.cmp(path, "C:\\3500000_TetraProdSW\\utils\\wamGood.txt"):
        return("PASS")
    else:
        return("FAIL")
        
if __name__ == '__main__':
    main(sys.argv)
