"""
Parameters:
  -COM<port>    Choose a specific COM port (e.g. -COM5). If omitted, I auto-pick the first one.
  -dynamic      Once the HW init is done, It’ll also turn off ISU SOS over TCP on the default IP.
  -real         configure RX data as 'real' before init.
  -h, -help     Show this help and exit.

Usage example:
  python rfsm_ctrl.py -COM5 -dynamic -real

Everything returns a value so LabVIEW can block until each step finishes.
"""

from RageComm import RageComm
import socket
import sys
import re

# Default tester IP for ISU SOS control
_IP = "169.254.70.191"
_TCP_PORT = 7


def TurnOffIsuSos(ip=_IP, port=_TCP_PORT):
    """
    Sends the 'm' command over TCP to turn off ISU SOS.
    Returns the raw response bytes.
    """
    write = b'm'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        s.send(write)
        data = s.recv(1024)
        s.shutdown(socket.SHUT_RDWR)
    return data


def initHw(com):
    """
    Applies my standard register setup for rxdata transmission.
    Returns True on success.
    """
    # Disable sequence mode
    com.consoleIo('seq off')

    # Register/value pairs I always use
    register_config = {
        0x02: 0x0400,
        0x03: 0x0000,
        0x04: 1032,
        0x05: 4,
        0x06: 10,
        0x08: 256,
        0x09: 51,
        0x0A: 4,
        0x0E: 8000,
        0x0F: 0x5555,
        0x10: 0x0055,
        0x11: 0xAAAA,
        0x12: 0x00AA,
        0x1A: 0x0000,
        0x1B: 0x0000,
        0x17: 0x0300,
        0x18: 0x0000,
    }

    for reg, value in register_config.items():
        com.consoleIo(f'wr reg 0x{reg:02X} 0x{value:04X}')

    # Final SOS command
    com.consoleIo('sos')
    return True

# python AmInit.py -dynamic -COM6
def main(argv):
    """
    Parses CLI flags, picks or auto-selects a COM port, does init, then optional ISU SOS off.
    Returns 0 on full success, non-zero on error.
    """
    # grab flags
    selected_port = None
    dynamic = False
    real = False

    for arg in argv[1:]:
        if re.fullmatch(r'-[cC][oO][mM]\d+', arg):
            selected_port = arg.lstrip('-')
        elif arg.lower() == '-dynamic':
            dynamic = True
        elif arg.lower() == '-real':
            real = True
        elif arg.lower() in ('-h', '-help'):
            print(__doc__)
            return 0
        else:
            print(f"Unknown option: {arg}")
            return 1

    # instantiate and list ports
    com = RageComm()
    ports = com.getPorts()
    if not ports:
        print("Error: No COM ports found.")
        com.close()
        return 1

    # pick the COM port
    if selected_port:
        if selected_port not in ports:
            print(f"Error: {selected_port} not in available ports: {ports}")
            return 1
        port_to_use = selected_port
    else:
        port_to_use = ports[0]  # auto-select

    try:
        # open port
        com.setPortName(port_to_use)
        com.open()

        # optional real mode
        if real:
            com.consoleIo('rxdata real')

        # do the register init
        if not initHw(com):
            print("Error during hardware init.")
            com.close()
            return 1

    finally:
        com.close()

    # optional ISU SOS off step
    if dynamic:
        resp = TurnOffIsuSos()
        # return code 0 but print raw bytes too
        print(f"ISU SOS response: {resp}")

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))