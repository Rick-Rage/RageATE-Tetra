from RageComm import RageComm
import re
# Antenna table definition
ant_table = [
    # Chirp, Antenna, D1,     D2,     D3,     D4
    [1, 0x1100, 0x0001, 0x0000, 0x0000, 0x0000],
    [2, 0x1110, 0x0003, 0x0000, 0x0000, 0x0000],
    [3, 0x2110, 0x0005, 0x0000, 0x0000, 0x0000],
    [4, 0x2300, 0x0002, 0x0008, 0x0000, 0x0000],
    [5, 0x3300, 0x0004, 0x000A, 0x0000, 0x0000],
    [6, 0x3330, 0x0007, 0x000D, 0x0000, 0x0000],
    [7, 0x4300, 0x0006, 0x000C, 0x0000, 0x0000],
    [8, 0x4330, 0x0009, 0x000F, 0x0000, 0x0000],
    [9, 0x5330, 0x000B, 0x0011, 0x0000, 0x0000],
    [10, 0x5600, 0x0000, 0x000E, 0x0014, 0x0000],
    [11, 0x6600, 0x0000, 0x0010, 0x0016, 0x0000],
    [12, 0x6660, 0x0000, 0x0013, 0x0019, 0x0000],
    [13, 0x7600, 0x0000, 0x0012, 0x0018, 0x0000],
    [14, 0x7660, 0x0000, 0x0015, 0x001B, 0x0000],
    [15, 0x8660, 0x0000, 0x0017, 0x001D, 0x0000],
    [16, 0x8C00, 0x0000, 0x0000, 0x001A, 0x0020],
    [17, 0x9C00, 0x0000, 0x0000, 0x001C, 0x0022],
    [18, 0x9CC0, 0x0000, 0x0000, 0x001F, 0x0025],
    [19, 0xAC00, 0x0000, 0x0000, 0x001E, 0x0024],
    [20, 0xACC0, 0x0000, 0x0000, 0x0021, 0x0027],
    [21, 0xBCC0, 0x0000, 0x0000, 0x0023, 0x0029],
    [22, 0xB800, 0x0000, 0x0000, 0x0000, 0x0026],
    [23, 0xC800, 0x0000, 0x0000, 0x0000, 0x0028],
    [24, 0xC880, 0x0000, 0x0000, 0x0000, 0x002A],
]


def loadAntTable(com):
    """
    Loads the antenna table into the FPGA using RageComm.
    Sends the configuration data for all antennas and demodulation tables.
    """
    tableAnt = 'wr table 3'
    tabledemod1 = 'wr table 0x10'
    tabledemod2 = 'wr table 0x11'
    tabledemod3 = 'wr table 0x12'
    tabledemod4 = 'wr table 0x13'

    for row in ant_table:
        print(f"Loading: {row}")
        tableAnt += f" 0x{row[1]:X}"
        tabledemod1 += f" {row[2]}"
        tabledemod2 += f" {row[3]}"
        tabledemod3 += f" {row[4]}"
        tabledemod4 += f" {row[5]}"

    # Send commands to the hardware
    com.consoleIo(tableAnt)
    com.consoleIo(tabledemod1)
    com.consoleIo(tabledemod2)
    com.consoleIo(tabledemod3)
    com.consoleIo(tabledemod4)


def dynamic_mode_init(com):
    """
    Initializes the hardware for dynamic mode scanning.
    Configures registers and loads the antenna table.
    """
    # Enable dynamic mode sequence
    com.consoleIo('seq on')

    # Dictionary to store register addresses and values
    register_config = {
        0x001: 0x01C7,  # FPGA_CONTROL
        0x002: 0x0400,  # ANT_SELECT_INIT_DELAY_LSW
        0x003: 0x0000,  # ANT_SELECT_INIT_DELAY_MSW
        0x004: 1032,    # NUM_CLOCKS_PER_ANT_CHANGE
        0x005: 24,      # NUM_ANTENNA_CHANGES
        0x006: 10,      # ADC_INITIAL_DELAY
        0x008: 256,     # NUM_ADC_SAMPLES_PER_CHIRP
        0x009: 51,      # ADC_INTRACHIRP_DELAY
        0x00A: 42,      # NUM_CHIRPS_FPD_READ
        0x00B: 206,     # FILTER_SWITCH_DELAY1
        0x00C: 616,     # FILTER_SWITCH_DELAY2
        0x00E: 8000,    # FPD_INITIAL_DELAY
        0x00F: 0x5555,  # FPD_START_SENTINEL_LSW
        0x010: 0x0055,  # FPD_START_SENTINEL_MSW
        0x011: 0xAAAA,  # FPD_END_SENTINEL_LSW
        0x012: 0x00AA,  # FPD_END_SENTINEL_MSW
        0x013: 128,     # NUM_CLOCKS_PER_VVA_CHANGE
        0x014: 1,       # NUM_VVA_CHANGES_PER_CHIRP
        0x017: 0x0300,  # DDR_FRAME_BUF_ADDR_LSW
        0x018: 0x0000,  # DDR_FRAME_BUF_ADDR_MSW
        0x019: 0x0000,  # SOFTWARE_SCAN_TRIGGER
        0x01A: 0x0000,  # FPD_IDLE_SENTINEL_LSW
        0x01B: 0x0000,  # FPD_IDLE_SENTINEL_MSW
        0x01D: 0x06DB,  # RX_AMP_CONTROL
        0x032: 0x0000,  # TX_SP4T_MATRIX_OVERRIDE
        0x033: 0x0000,  # TX_FILTERSWITCH_OVERRIDE
        0x034: 0x0000,  # RX_SP2T_SWITCH_OVERRIDE
        0x050: 0x0667,  # VGA0_TABLE
        0x051: 0x0667,  # VGA1_TABLE
        0x052: 0x0667,  # VGA2_TABLE
        0x053: 0x0667,  # VGA3_TABLE
        0x05A: 0x0000,  # ADC_TEST_PATTERN
        0x05B: 0x0001,  # SCRATCH
    }

    # Write register values to the hardware
    for reg, value in register_config.items():
        com.consoleIo(f'wr reg 0x{reg:03X} 0x{value:04X}')

    # Load antenna table
    loadAntTable(com)


# python DynamicModeInit.py -COM6

def main(argv):
    """
    Main entry point for dynamic mode initialization.
    Identifies the appropriate COM port and initializes the hardware.
    """
    port_name = None

    for arg in argv[1:]:
        if re.fullmatch(r'-[cC][oO][mM]\d+', arg):
            port_name = arg.lstrip('-')
    
    if port_name == None :
        # Otherwise, scan for available COM ports
        com = RageComm()
        ports = com.getPorts()
        if len(ports) > 1:
            print("Available COM ports:")
            for i, port in enumerate(ports):
                print(f"{i}: {port}")
            try:
                index = int(input("Select COM port index: "))
                if index < 0 or index >= len(ports):
                    print("Invalid selection.")
                    return
                # Swap selected port to index 0
                port_name = ports[index]
            except ValueError:
                print("Invalid input. Must be an integer.")
                return
        else:
            port_name = ports[0]

    if not port_name:
        print("No COM port found.")
        return

    # Initialize hardware with the specified port
    com = RageComm()
    com.setPortName(port_name)
    com.open()
    dynamic_mode_init(com)
    com.close()


if __name__ == '__main__':
    import sys
    main(sys.argv)
