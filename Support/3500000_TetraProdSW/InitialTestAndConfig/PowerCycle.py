import sys
sys.path.append('../utils')
import utils
import time

ini = utils.ReadIni('../utils/tetra.ini')
ps_port = ini['config_power_supply']['port']
ps_volt = float(ini['config_power_supply']['voltage'])
ps_curr = float(ini['config_power_supply']['current'])

ok = utils.TurnOffPowerSupply(ps_port)
if ok:
    time.sleep(1)
    errMsg,measVolt,measCurr = utils.TurnOnPowerSupply(ps_port, ps_volt, ps_curr)
    print(errMsg,measVolt,measCurr)
