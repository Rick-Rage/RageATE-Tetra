import clr
import argparse
import sys
import traceback
from pyreadline3 import Readline 

clr.AddReference('FieldTestClient')
from cFieldTestClient import Client, TestLongShortEnums, ProdSubtestEnums

class FieldTestShell:
    def __init__(self):
        self.client = Client()
        self.connected = False
        self.parser = self.create_parser()
        
    def create_parser(self):
        # Create parent parser with common test arguments
        parent_parser = argparse.ArgumentParser(add_help=False)
        parent_parser.add_argument(
            "--test_length", 
            choices=['FULL_TEST', 'SHORT_TEST'], 
            default='SHORT_TEST',
            help="Test duration (default: SHORT_TEST)"
        )

        # Main parser setup
        main_parser = argparse.ArgumentParser(
            description="Field Test Client Shell", 
            add_help=False,
            usage="%(prog)s [command] [options]"
        )
        subparsers = main_parser.add_subparsers(dest='command', help='Available commands')

        # Connection commands
        open_parser = subparsers.add_parser('open', help='Connect to server')
        open_parser.add_argument("--host", default="localhost", help="Server hostname (default: localhost)")
        open_parser.add_argument("--port", type=int, default=50501, help="Server port (default: 50501)")

        subparsers.add_parser('close', help='Disconnect from server')
        subparsers.add_parser('help', help='Show help message')

        # Test commands using parent parser
        subparsers.add_parser('start_test', parents=[parent_parser], 
                            help='Start main test sequence')
        subparsers.add_parser('vco_calibration', parents=[parent_parser], 
                            help='Perform VCO calibration')

        # CW Frequency command
        cw_parser = subparsers.add_parser('set_cw_freq', help='Set continuous wave frequency')
        cw_parser.add_argument("--frequency", type=float, required=True,
                            help="Frequency in GHz (required)")
        cw_parser.add_argument("--channel", type=int, required=True,
                            help="Channel number (required)")
        cw_parser.add_argument("--filter", type=int, choices=[1,2,3], required=True,
                            help="Filter selection: 1=Low, 2=High, 3=Auto (required)")
        cw_parser.add_argument("--mute", action="store_true",
                            help="Mute output during configuration")

        # System commands
        subparsers.add_parser('exit_test', help='Exit current running test')
        subparsers.add_parser('armRFSM', help='Arm RF Switch Matrix')

        return main_parser

    def handle_command(self, cmd_line):
        try:
            args = self.parser.parse_args(cmd_line.split())
            self.execute_command(args)
        except SystemExit:
            pass  # Prevent argparse from exiting the program
        except Exception as e:
            print(f"Error: {str(e)}")

    def execute_command(self, args):
        if not hasattr(args, 'command'):
            self.parser.print_help()
            return

        command = args.command.lower()
        
        if command == 'open':
            self.handle_connect(args)
        elif command == 'close':
            self.handle_disconnect()
        elif command == 'help':
            self.parser.print_help()
        elif not self.connected:
            print("Not connected! Use 'open' first")
        else:
            self.handle_test_command(args)

    def handle_connect(self, args):
        if self.connected:
            print("Already connected to server")
            return
            
        print(f"Connecting to {args.host}:{args.port}...")
        if self.client.Open(args.host, args.port):
            self.connected = True
            print("Connection established")
        else:
            print("Connection failed")

    def handle_disconnect(self):
        if self.connected:
            self.client.Close()
            self.connected = False
            print("Connection closed")
        else:
            print("Not currently connected")

    def handle_test_command(self, args):
        try:
            if args.command == 'start_test':
                self.handle_start_test(args)
            elif args.command == 'vco_calibration':
                self.handle_vco_calibration(args)
            elif args.command == 'set_cw_freq':
                self.handle_set_cw_freq(args)
            elif args.command == 'exit_test':
                self.handle_exit_test()
            elif args.command == 'armrfsm' or args.command == 'armRFSM':
                self.handle_arm_rfsm()
            else:
                print(f"Unknown command: {args.command}")

        except Exception as e:
            print(f"Command execution failed: {str(e)}")
            traceback.print_exc()

    def handle_start_test(self, args):
        test_enum = getattr(TestLongShortEnums, args.test_length)
        print("Starting Start Test")
        result = self.client.StartTest(test_enum)


    def handle_vco_calibration(self, args):
        test_enum = getattr(TestLongShortEnums, args.test_length)
        print("Starting VCO Calibration")
        result = self.client.VcoCalibration(test_enum)


    def handle_set_cw_freq(self, args):
        success = self.client.setCWFreq(
            args.frequency,
            args.channel,
            args.filter,
            args.mute
        )
        config = f"{args.frequency}GHz on ch{args.channel} "
        config += f"(filter: {args.filter}, mute: {args.mute})"
        status = "successful" if success else "failed"
        print(f"CW frequency setup {status}: {config}")

    def handle_exit_test(self):
        if self.client.ExitCurrentTest():
            print("Current test exited successfully")
        else:
            print("Failed to exit current test")

    def handle_arm_rfsm(self):
        print("Armming RFSM")
        self.client.RFSMRESETARM()
        print("RFSM armed and ready")

    def shell_loop(self):
        print("Field Test Client Shell - Type 'help' for available commands")
        while True:
            try:
                cmd = input("FT> ").strip()
                if not cmd:
                    continue
                
                if cmd.lower() in ['exit', 'quit']:
                    self.handle_disconnect()
                    print("Exiting shell")
                    break
                
                self.handle_command(cmd)
                
            except KeyboardInterrupt:
                print("\nUse 'exit' or 'quit' to terminate the shell")
            except Exception as e:
                print(f"Unexpected error: {str(e)}")
                traceback.print_exc()

if __name__ == "__main__":
    FieldTestShell().shell_loop()