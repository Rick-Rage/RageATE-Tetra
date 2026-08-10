import utils
import RageComm
import time

ini = utils.ReadIni("tetra.ini")

#utils.TurnOnPowerSupplyBurn(
#    ini['burnin_power_supply']['port'],
#    ini['burnin_power_supply']['voltage'],
#    ini['burnin_power_supply']['current'])

bibs = []
mods = []
for ibib in range(1,2):
    bibs.append(ini['burnin'][f'BiB{ibib}'])
    m = []
    for imod in range(1,13):
        m.append(ini['burnin'][f'BiB{ibib}port{imod}'])
    mods.append(m)

for ibib in range(0,1):
    print("BIB", bibs[ibib])
    com = RageComm.RageComm(bibs[ibib], 38400)
    for imodule in range(0,12):
        com.consoleIo(f"poweron {imodule+1}")

    time.sleep(1)
    status = com.consoleIo("status")
    print(status)
    status = status.split('\n')
    for i,s in enumerate(status):
        if not s:
            continue
        f = s.split()
        curr = float(f[3])
        if curr > 100:
            comMod = RageComm.RageComm(mods[ibib][i-1])
            for itry in range(0,10):
                ok = comMod.Ping(1)
                if ok:
                    print(i, "GOOD")
                    break
            
    

    com.consoleIo(f"poweroff all")
    continue
    print(f"bib {bibs[ibib]}")
    for imod in range(0,12):
        try:
            com = RageComm.RageComm(mods[ibib][imod])
        except:
            com = None
            continue
        


        if not com:
            print(f"Com {mods[ibib][imod]} did not work")
            continue
        print(f"  mod {imod+1}: {mods[ibib][imod]} ", end='')
        if com.Ping(timeout=0.5):
            print("OK")
            print(com.consoleIo("esn"))
        else:
            print("EMPTY")
