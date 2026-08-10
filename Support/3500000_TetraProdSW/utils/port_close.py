from RageComm import RageComm

import time

def read_reg(com):
    resp = com.consoleIo('seq off')


    resp = com.consoleIo('wr reg 0x12 0x00AA')

def main():
    com = RageComm()
    p = com.getPorts()
    if not p:
        print("No COM found")
    else:
        print("Found", p[0])
        com.setPortName(p[0])
        com.open()
        start = time.time()
        for i range(10):
            read_reg(com)
        com.close()
        print(f'Execution time in seconds without only one close operation: {time.time() -start} ')




if __name__ == '__main__':
    import sys
    main()
