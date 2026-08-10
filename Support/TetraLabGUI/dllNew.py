"""
Field Test Shell CLI – Python 3.6 compatible.

Prereqs:
  pip install pythonnet
  pip install pyreadline   # optional, for Windows line-editing
"""

import sys
import traceback
import clr  # comes from pythonnet
# try to pull in the pythonnet CLR bridge
# optional: nicer REPL on Windows
try:
    import readline  # Unix
except ImportError:
    try:
        import pyreadline as readline  # Windows
    except ImportError:
        pass

# load the .NET FieldTestClient assembly
clr.AddReference('FieldTestClient')
from cFieldTestClient import Client, TestLongShortEnums


class FieldTestShell(object):
    """
    Shell for talking to the Field Test server.
    """

    def __init__(self):
        # create client, but don’t connect yet
        self.client = Client()
        self.connected = False

    def connect(self, host='localhost', port=50501):
        """Connect to host:port (defaults localhost:50501)."""
        if self.connected:
            print("→ Already connected")
            return
        print("→ Connecting to {}:{}…".format(host, port))
        if self.client.Open(host, port):
            self.connected = True
            print("✔ Connected")
        else:
            print("✘ Connection failed")

    def disconnect(self):
        """Disconnect if we’re connected."""
        if not self.connected:
            print("→ Not connected")
            return
        self.client.Close()
        self.connected = False
        print("✔ Disconnected")

    def start_test(self, length='SHORT_TEST'):
        """Start a FULL_TEST or SHORT_TEST."""
        try:
            enum = getattr(TestLongShortEnums, length)
        except AttributeError:
            print("Invalid length '{}'. Use FULL_TEST or SHORT_TEST.".format(length))
            return
        print("→ Starting {}…".format(length))
        self.client.StartTest(enum)

    def vco_calibration(self, length='SHORT_TEST'):
        """Run VCO calibration for FULL_TEST or SHORT_TEST."""
        try:
            enum = getattr(TestLongShortEnums, length)
        except AttributeError:
            print("Invalid length '{}'. Use FULL_TEST or SHORT_TEST.".format(length))
            return
        print("→ VCO calibration ({})…".format(length))
        self.client.VcoCalibration(enum)

    def set_cw_freq(self, freq, ch, filt, mute=False):
        """
        Set CW frequency.
          freq: float in GHz
          ch:   int channel number
          filt: int 1=Low, 2=High, 3=Auto
          mute: bool
        """
        ok = self.client.setCWFreq(freq, ch, filt, mute)
        print("→ CW {} GHz ch{} filt={} mute={} → {}".format(
            freq, ch, filt, mute, "OK" if ok else "FAIL"
        ))

    def exit_test(self):
        """Exit current running test."""
        if self.client.ExitCurrentTest():
            print("✔ Test exited")
        else:
            print("✘ Failed to exit test")

    def arm_rfsm(self):
        """Arm the RF switch matrix."""
        print("→ Arming RFSM…")
        self.client.RFSMRESETARM()
        print("✔ RFSM armed")

    def print_help(self):
        """Show available commands."""
        print("""
Commands:
  open [host] [port]  
      Connect (defaults: localhost 50501)
  close               
      Disconnect
  start_test [FULL_TEST|SHORT_TEST]
      Run the main test
  vco_calibration [FULL_TEST|SHORT_TEST]
      Perform VCO calibration
  set_cw_freq <GHz> <channel> <filter> [mute]
      Set CW frequency (filter: 1=Low,2=High,3=Auto)
  exit_test          
      Exit current test
  armrfsm            
      Arm RF switch matrix
  help               
      Show this help
  exit, quit         
      Disconnect & exit
""".strip())

    def run(self):
        """Main interactive loop."""
        print("Field Test Shell (type 'help')")
        while True:
            try:
                line = input("FT> ").strip()
            except KeyboardInterrupt:
                print("\n(use 'exit' to quit)")
                continue
            if not line:
                continue

            parts = line.split()
            cmd = parts[0].lower()

            # exit
            if cmd in ('exit', 'quit'):
                self.disconnect()
                print("Goodbye.")
                break

            # help
            if cmd == 'help':
                self.print_help()
                continue

            # connection commands
            if cmd == 'open':
                host = parts[1] if len(parts) > 1 else 'localhost'
                port = int(parts[2]) if len(parts) > 2 else 50501
                self.connect(host, port)
                continue
            if cmd == 'close':
                self.disconnect()
                continue

            # require connection for everything else
            if not self.connected:
                print("→ Not connected; use 'open'")
                continue

            # test/control commands
            try:
                if cmd == 'start_test':
                    length = parts[1].upper() if len(parts) > 1 else 'SHORT_TEST'
                    self.start_test(length)
                elif cmd == 'vco_calibration':
                    length = parts[1].upper() if len(parts) > 1 else 'SHORT_TEST'
                    self.vco_calibration(length)
                elif cmd == 'set_cw_freq':
                    if len(parts) < 4:
                        print("Usage: set_cw_freq <GHz> <channel> <filter> [mute]")
                    else:
                        freq = float(parts[1])
                        ch   = int(parts[2])
                        filt = int(parts[3])
                        mute = 'mute' in parts[4:]
                        self.set_cw_freq(freq, ch, filt, mute)
                elif cmd == 'exit_test':
                    self.exit_test()
                elif cmd in ('armrfsm', 'arm_rfsm'):
                    self.arm_rfsm()
                else:
                    print("Unknown command:", cmd)
            except Exception as e:
                print("Error:", e)
                traceback.print_exc()


if __name__ == '__main__':
    FieldTestShell().run()
