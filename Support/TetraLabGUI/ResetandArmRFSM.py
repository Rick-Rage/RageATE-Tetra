import clr
import sys

clr.AddReference('FieldTestClient')
from cFieldTestClient import Client

def reset_and_arm_rfsm(host='localhost', port=50501)

    client = Client()
    print(fConnecting to {host}{port}...)
    if not client.Open(host, port)
        print(Connection failed)
        sys.exit(1)

    print(Resetting and arming RF switch matrix...)
    try
        client.RFSMRESETARM()
        print("RF switch matrix reset and armed")
    except Exception as e
        print("Error during RFSM resetarm ", e)
    finally
        client.Close()
        print(Disconnected)

if __name__ == __main__

    if len(sys.argv)  1 and sys.argv[1] in ('-h', '--help')
        print(Usage python rfs_arm.py [host] [port])
        sys.exit(0)

    host = sys.argv[1] if len(sys.argv)  1 else 'localhost'
    port = int(sys.argv[2]) if len(sys.argv)  2 else 50501
    reset_and_arm_rfsm(host, port)