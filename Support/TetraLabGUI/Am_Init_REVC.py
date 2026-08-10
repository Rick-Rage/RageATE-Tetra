from RageComm import RageComm
import socket

ip ="169.254.70.191" # uncomment this line to use with tester in NBP

def TurnOffIsuSos(ip):
    port = 7
    buffer = 1024
    write = b'm'
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.connect((ip , int(port)))
    s.send(write)
    data = s.recv(1024)
    # print(data)
    # data =  int.from_bytes(data,byteorder ='little')
    s.shutdown(2)

def initHw(com):
    #configure AM Module for rxdata transmission
    resp = com.consoleIo('seq off')
    # resp = com.consoleIo('rxfilt mid')
    # resp = com.consoleIo('rxport 8')
    # resp = com.consoleIo('rxdata real')
    #end  AM config
    # AM_RO_ANT_SEL_INITIAL_DELAY_LSB
    resp = com.consoleIo('wr reg 0x02 0x0400')

    # AM_RO_ANT_SEL_INITIAL_DELAY_MSB
    resp = com.consoleIo('wr reg 0x03 0x0000')

    # AM_RO_NUM_CLOCKS_PER_ANT_CHANGE
    resp = com.consoleIo('wr reg 0x04 1032')

    # AM_RO_NUM_ANT_CHANGES
    resp = com.consoleIo('wr reg 0x05 4')

    # AM_RO_ADC_INITIAL_DELAY
    resp = com.consoleIo('wr reg 0x06 10')

    # AM_RO_NUM_ADC_SAMPLES_PER_CHIRP
    resp = com.consoleIo('wr reg 0x08 256')

    # AM_RO_ADC_INTRA_CHIRP_DELAY
    resp = com.consoleIo('wr reg 0x09 51')

    # AM_RO_NUM_CHIRPS_FPD_READ
    resp = com.consoleIo('wr reg 0x0A 4')

    # AM_RO_FPD_INITIAL_DELAY
    resp = com.consoleIo('wr reg 0x0E 8000')

    # AM_RO_FPD_SOF_SENTINEL_LSB, MSB
    resp = com.consoleIo('wr reg 0x0F 0x5555')
    resp = com.consoleIo('wr reg 0x10 0x0055')

    # AM_RO_FPD_EOF_SENTINEL_LSB, MSB
    resp = com.consoleIo('wr reg 0x11 0xAAAA')
    resp = com.consoleIo('wr reg 0x12 0x00AA')

    # AM_RO_FPD_IDLE_SENTINEL_LSB, MSB
    resp = com.consoleIo('wr reg 0x1A 0x0000')
    resp = com.consoleIo('wr reg 0x1B 0x0000')

    # AM_RO_DDR_FRAME_BUFF_ADDR_LSB, MSB
    resp = com.consoleIo('wr reg 0x17 0x0300')
    resp = com.consoleIo('wr reg 0x18 0x0000')
    resp = com.consoleIo('sos')


def main():
    com = RageComm()
    p = com.getPorts()
    dynamic = False
    argn = 1
    help = False
    import sys

    while argn < len(sys.argv):
        arg = sys.argv[argn]
        argn += 1
        if arg == "-dynamic":
            dynamic = True
        else:
            print("Unknown option %s" % arg)
            return
    if help:
        #print("-a <antenna>   RX antenna 1-8")
        print("-dynamic          Turns ISU SOS Off")

        return

    if not p:
        print("No COM found")
    else:
        print("Found", p[0])
        com.setPortName(p[0])
        com.open()
        initHw(com)
        com.close()
        if dynamic:
            TurnOffIsuSos(ip)
        


if __name__ == '__main__':
    import sys
    main()
