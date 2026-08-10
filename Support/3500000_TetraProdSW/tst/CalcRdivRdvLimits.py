import sys
sys.path.append('../utils')
import utils
from RageComm import RageComm
import SqlFuncs

def GetAvgValues(table, valueNames):
    cmd = f"SELECT AVG({valueNames[0]})"
    for name in valueNames[1:]:
        cmd += f",AVG({name})"
    cmd += f" FROM {table} WHERE fpga_sw_revision = '2.1.14';"
    #print(cmd)
    try:
        res = SqlFuncs.executeOne(cmd)
        res = [float(a) for a in res[0]]
    except:
        print("Oops")
        res = "ERR!"
    return res

def GetValues(table, valueNames):
    cmd = f"SELECT {valueNames[0]}"
    for name in valueNames[1:]:
        cmd += f",{name}"
    cmd += f" FROM {table} WHERE fpga_sw_revision = '2.1.14';"
    #print(cmd)
    try:
        res = SqlFuncs.executeOne(cmd)
        #res = [float(a) for a in res[0]]
    except:
        print("Oops")
        res = "ERR!"
    return res


def CheckValues(table, value, value_hi, value_lo):
    a = GetValues(table, value)
    ok = True
    for r in a:
        for i,c in enumerate(r):
            try:
                if c < value_lo[i]:
                    print("FAIL LOW", value[i], c, value_lo[i]);
                    ok = False
                elif c > value_hi[i]:
                    print("FAIL HIGH", value[i], c, value_hi[i]);
                    ok = False
                else:
                    pass #print("PASS", value[i], c, value_lo[i], value_hi[i])
            except:
                print("EXCEPT", value[i], c, value_lo[i], value_hi[i], r)
    print("OK", ok)

mvolts = ["sw3p6_mV","sw5p5_mV","sw2p8a_mV","sw2p8b_mV","sw2p4_mV","sw1p4_mV"]
mv = [3.6,5.5,2.8,2.8,2.4,1.4]
mv_hi = [a*1.05*1000 for a in mv]
mv_lo = [a*0.90*1000 for a in mv]
a = CheckValues("TetraProd.tetra_configuration", mvolts, mv_hi, mv_lo)

ldo_mvolts = ["isu18p5_mV", "core1p0_mV", "xvr1p0_mV", "dig1p8_mV", "dig3p3_mV", "xvr1p2_mV", "div5p0_mV", "vdd3p3_mV", "rx2p5_mV", "tx2p5_mV", "adc1p8_mv"]
lmv = [18.5,1.0,1.0,1.8,3.3,1.2,5.0,3.3,2.5,2.5,1.8]
lmv_hi = [a*1.05*1000 for a in lmv]
lmv_lo = [a*0.95*1000 for a in lmv]
b = CheckValues("TetraProd.tetra_configuration", ldo_mvolts, lmv_hi, lmv_lo)

currs = ["sw3p6_mA","sw5p5_mA","sw2p8a_mA","sw2p8b_mA","sw2p4_mA","sw1p4_mA"]
c = GetAvgValues("TetraProd.tetra_configuration", currs)
c_hi = [a*1.12 for a in c]
c_lo = [a*0.87 for a in c]
b = CheckValues("TetraProd.tetra_configuration", currs, c_hi, c_lo)

print("\n[rdiv_limits] ; low mA, high mA, low mV, high mV")
for i in range(0,len(mv)):
    print(f"{mvolts[i][:-3]} = {int(c_lo[i])},{int(c_hi[i])},{int(mv_lo[i])},{int(mv_hi[i])}")

print("\n[rdv_limits] ; low mV, high mV")    
for i in range(0,len(lmv)):
    print(f"{ldo_mvolts[i][:-3]} = {int(lmv_lo[i])},{int(lmv_hi[i])}")
