import sys
sys.path.append('../utils')
from RageComm import RageComm
from time import sleep
import numpy as np
from matplotlib import pyplot as plt
import math
from datetime import date, datetime, timedelta

TABLE_ID_ANTENNA_SELECT   = 0x03
TABLE_ID_RX_GAIN_TABLE    = 0x17

AM_RO_FPGA_CONTROL2 = 0x070

AM_RB_FPGA_CONTROL2_RX_DATA_FORMAT = 8
AM_RB_FPGA_CONTROL2_ENABLE_ADC_DRIVER         = 1

reg_settings = [
    [0x02, 0x0400], # AM_RO_ANT_SEL_INITIAL_DELAY_LSB, MSB
    [0x03, 0x0000], #
    [0x04, 1032],   # AM_RO_NUM_CLOCKS_PER_ANT_CHANGE
    [0x05, 2],      # AM_RO_NUM_ANT_CHANGES
    [0x06, 10],     # AM_RO_ADC_INITIAL_DELAY
    [0x08, 256],    # AM_RO_NUM_ADC_SAMPLES_PER_CHIRP
    [0x09, 51],     # AM_RO_ADC_INTRA_CHIRP_DELAY
    [0x0A, 0],      # AM_RO_NUM_CHIRPS_FPD_READ
    [0x17, 0x0300], # AM_RO_DDR_FRAME_BUFF_ADDR_LSB, MSB
    [0x18, 0x0000]  #
]


def readAdc(com):
    resp = com.consoleIo('rd data')
    strData = resp.split()
    intData = np.array([int(s) for s in strData])
    return intData


def saveSignal(data, fileName):
    if not fileName:
        return
    fname = "data/" + fileName + '_' + datetime.now().strftime('%Y%m%d_%H%M%S') + '.txt'
    with open(fname, "w") as fp:
        for ichannel,datum in enumerate(data):
            for iloop,signal in enumerate(datum):
                for isample,sample in enumerate(signal):
                    fp.write(f"{ichannel},{iloop},{isample},{sample}\n")


def plotSignal(data):
    fig, axs = plt.subplots(2, 2)
    for i,datum in enumerate(data):
        ax = axs[i//2,i%2]
        ax.set_ylabel("Amplitude")
        ax.set_xlabel("Sample #")
        for signal in datum:
            ax.plot(list(range(305,320)), signal[305:320])
        ax.grid(True)
    plt.show()


def rdReg(com, addr):
    resp = com.consoleIo(f"rd reg 0x{addr:X}")
    fields = resp.split(':')
    value = fields[1][3:]
    value = int(value,16)
    return value


def wrReg(com, addr, value):
    com.consoleIo(f"wr reg 0x{addr:X} 0x{value:X}")


def wrTable(com, table, values):
    txt = f"wr table 0x{table:X}"
    for value in values:
        txt += f" 0x{value:X}"
    com.consoleIo(txt)


def run(com, fileName):

    # Set for real data capture
    control2 = rdReg(com, AM_RO_FPGA_CONTROL2)
    print(f"0x{control2:x}")
    control2 = control2 | (1 << AM_RB_FPGA_CONTROL2_RX_DATA_FORMAT)
    control2 = control2 & ~(1 << AM_RB_FPGA_CONTROL2_ENABLE_ADC_DRIVER)
    wrReg(com, AM_RO_FPGA_CONTROL2, control2)

    # Init the hardware registers to collect data
    for pr in reg_settings:
        wrReg(com, pr[0], pr[1])

    # Init the DEMUX tables to tell the hardware where to put the data
    for table in range(0,4):
        wrTable(com, 0x10 + table, [table+1, table+1])

    # Set the RX Gain table to go from 0 to 7
    wrTable(com, TABLE_ID_RX_GAIN_TABLE, [0x09A, 0x701])

    # Reset the delay selects
    com.consoleIo(f"gpio wr 9 1 0")

    data = [[]]
    for method in range(1,2):
        if method == 1:
            control2 = control2 | (1 << AM_RB_FPGA_CONTROL2_ENABLE_ADC_DRIVER)
            wrReg(com, AM_RO_FPGA_CONTROL2, control2)
        chdata = []
        for channel in range(0,4):
            data = []
            # set up the ant table to sample the current channel
            wrTable(com, TABLE_ID_ANTENNA_SELECT, [0x1100, 0x1000 + (0x100 << channel)]) # Skipping the first chirp which has had problems

            for loop in range(0,5):
                com.consoleIo("sos")

                data.append(readAdc(com))
            chdata.append(data)
    if fileName:
        saveSignal(chdata, fileName)
    else:
        plotSignal(chdata)


def main(argv):
    portName = ''
    fileName = ''
    argv.pop(0)
    while len(argv) > 0:
        arg = argv.pop(0)
        if arg == "-o":
            if len(argv) > 0:
                fileName = argv.pop(0)
        elif arg == "-p":
            if len(argv) > 0:
                portName = argv.pop(0)

    if len(argv) > 1:
        # If the function is called with an argument, assume it is the name of
        # the port to open
        portName = argv[1]
    else:
        # If no name is provided, see what ports are available
        com = RageComm()
        p = com.getPorts()
        if p:
            # If ports are available use, the first
            print("Found", p[0])
            portName = p[0]

    if not portName:
        print("No COM found")
    else:
        com.setPortName(portName)
        com.open()
        run(com, fileName)
        com.close()

if __name__ == '__main__':
    import sys
    main(sys.argv)
