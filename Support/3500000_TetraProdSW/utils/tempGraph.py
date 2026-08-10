
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from deepdiff import DeepDiff

class Module:
    def __init__(self,sn,timetemp = {},ext1 = {},ext2 = {},ext3 = {},ext4 = {},isu18p5 = {},core1p0 = {},xvr1p0 = {},dig1p8 = {},
                 dig3p3 = {},xvr1p2 = {},div5p0 = {},vdd3p3 = {},rx2p5 = {},tx2p5 = {},adc1p8 = {},sw3p6A = {},sw5p5A = {},sw2p8aA = {},
                 sw2p8bA = {},sw2p4A = {},sw1p4A = {},sw3p6V = {},sw5p5V = {},sw2p8aV = {},sw2p8bV = {},sw2p4V = {},sw1p4V = {}):
        self.sn = sn

        self.timetemp = timetemp
        self.ext1 = ext1
        self.ext2 = ext2
        self.ext3 = ext3
        self.ext4 = ext4
  
        self.isu18p5 = isu18p5
        self.core1p0 = core1p0
        self.xvr1p0 = xvr1p0
        self.dig1p8 = dig1p8
        self.dig3p3 = dig3p3
        self.xvr1p2 = xvr1p2
        self.div5p0 = div5p0
        self.vdd3p3 = vdd3p3
        self.rx2p5 = rx2p5
        self.tx2p5 = tx2p5
        self.adc1p8 = adc1p8

        self.sw3p6A = sw3p6A
        self.sw5p5A = sw5p5A
        self.sw2p8aA = sw2p8aA
        self.sw2p8bA = sw2p8bA
        self.sw2p4A = sw2p4A
        self.sw1p4A = sw1p4A

        self.sw3p6V = sw3p6V
        self.sw5p5V = sw5p5V
        self.sw2p8aV = sw2p8aV
        self.sw2p8bV = sw2p8bV
        self.sw2p4V = sw2p4V
        self.sw1p4V = sw1p4V

modulenames = []
moduledict = {}
listofobjects = []
time = 0
with open('C:\\SynologyDrive\\WAM\\BurnIn\\BurnBook-1.txt') as f:
    for line in f.readlines():
        temp = None
        meas = None
        if 'WAM' in line:
            sn = line.split()
            sn = sn[0]
            if sn in modulenames:
                objsn = moduledict[sn]
            else:
                modulenames.append(sn)
                objsn = Module(sn,{},{},{},{},{},{},{},{},{},
                 {},{},{},{},{},{},{},{},{},{},
                 {},{},{},{},{},{},{}, {},{})
                listofobjects.append(objsn)
                moduledict[sn] = objsn

        elif 'int' in line:
            temp = line.split()
            temp = float(temp[1])
            print(temp)
            objsn.timetemp[time] = temp
            

        elif 'ext1' in line:
            temp = line.split()
            temp = temp[1]
            objsn.ext1[time] = temp
            

        elif 'ext2' in line:
            temp = line.split()
            temp = temp[1]
            objsn.ext2[time] = temp
            

        elif 'ext3' in line:
            temp = line.split()
            temp = temp[1]
            objsn.ext3[time] = temp
            

        elif 'ext4' in line:
            temp = line.split()
            temp = temp[1]
            objsn.ext4[time] = temp
            

        elif 'isu18p5' in line:
            meas = line.split()
            meas = meas[1]
            objsn.isu18p5[time] = meas
            

        elif 'core1p0' in line:
            meas = line.split()
            meas = meas[1]
            objsn.core1p0[time] = meas
            

        elif 'xvr1p0' in line:
            meas = line.split()
            meas = meas[1]
            objsn.xvr1p0[time] = meas
            

        elif 'dig1p8' in line:
            meas = line.split()
            meas = meas[1]
            objsn.dig1p8[time] = meas
            

        elif 'dig3p3' in line:
            meas = line.split()
            meas = meas[1]
            objsn.dig3p3[time] = meas
            

        elif 'xvr1p2' in line:
            meas = line.split()
            meas = meas[1]
            objsn.xvr1p2[time] = meas
            

        elif 'div5p0' in line:
            meas = line.split()
            meas = meas[1]
            objsn.div5p0[time] = meas
            

        elif 'vdd3p3' in line:
            meas = line.split()
            meas = meas[1]
            objsn.vdd3p3[time] = meas
            

        elif 'rx2p5' in line:
            meas = line.split()
            meas = meas[1]
            objsn.rx2p5[time] = meas
            

        elif 'tx2p5' in line:
            meas = line.split()
            meas = meas[1]
            objsn.tx2p5[time] = meas
            

        elif 'adc1p8' in line:
            meas = line.split()
            meas = meas[1]
            objsn.adc1p8[time] = meas
            

        elif 'sw3p6' in line:
            meas = line.split()
            ma = meas[2].replace(',','')
            mv = meas[4]
            objsn.sw3p6A[time] = ma
            objsn.sw3p6V[time] = mv
            

        elif 'sw5p5' in line:
            meas = line.split()
            ma = meas[2].replace(',','')
            mv = meas[4]
            objsn.sw5p5A[time] = ma
            objsn.sw5p5V[time] = mv
            

        elif 'sw2p8a' in line:
            meas = line.split()
            ma = meas[2].replace(',','')
            mv = meas[4]
            objsn.sw2p8aA[time] = ma
            objsn.sw2p8aV[time] = mv
            

        elif 'sw2p8b' in line:
            meas = line.split()
            ma = meas[2].replace(',','')
            mv = meas[4]
            objsn.sw2p8bA[time] = ma
            objsn.sw2p8bV[time] = mv
            

        elif 'sw2p4' in line:
            meas = line.split()
            ma = meas[2].replace(',','')
            mv = meas[4]
            objsn.sw2p4A[time] = ma
            objsn.sw2p4V[time] = mv
            

        elif 'sw1p4' in line:
            meas = line.split()
            ma = float(meas[2].replace(',',''))
            mv = float(meas[4])
            objsn.sw1p4A[time] = ma
            objsn.sw1p4V[time] = mv
            

        elif 'PowerSupply' in line:
            time = time + 1

print(moduledict['WAM-000140'].timetemp[0])
print(moduledict['WAM-000141'].timetemp[0])
if (moduledict['WAM-000140'].timetemp == moduledict['WAM-000141'].timetemp):
    print("AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
    exit()

df = pd.DataFrame(columns = ['time','int','ext1','ext2','ext3','ext4','isu18p5','core1p0','xvr1p0','dig1p8',
                'dig3p3','xvr1p2','div5p0','vdd3p3','rx2p5','tx2p5','adc1p8','sw3p6A','sw5p5A','sw2p8aA',
                'sw2p8bA','sw2p4A','sw1p4A','sw3p6V','sw5p5V','sw2p8aV','sw2p8bV','sw2p4V','sw1p4V','ModuleSn'])

for objname in listofobjects:

    x = []
    y = [] 
    y1 = []
    y2 = [] 
    y3 = []
    y4 = []

    yv1 = []
    yv2 = []
    yv3 = []
    yv4 = []
    yv5 = []
    yv6 = []

    yi1 = []
    yi2 = []
    yi3 = []
    yi4 = []
    yi5 = []
    yi6 = []
    yrdv1 = []
    yrdv2 = []
    yrdv3 = []
    yrdv4 = []
    yrdv5 = []
    yrdv6 = []
    yrdv7 = []
    yrdv8 = []
    yrdv9 = []
    yrdv10 = []
    yrdv11 = []
    
    for key in objname.timetemp:
        x.append(int(key))
        y.append(float(objname.timetemp[key]))
        y1.append(float(objname.ext1[key]))
        y2.append(float(objname.ext2[key]))
        y3.append(float(objname.ext3[key]))
        y4.append(float(objname.ext4[key]))

        yi1.append(float(objname.sw3p6A[key]))
        yi2.append(float(objname.sw5p5A[key]))
        yi3.append(float(objname.sw2p8aA[key]))
        yi4.append(float(objname.sw2p8bA[key]))
        yi5.append(float(objname.sw2p4A[key]))
        yi6.append(float(objname.sw1p4A[key]))

        yv1.append(float(objname.sw3p6V[key]))
        yv2.append(float(objname.sw5p5V[key]))
        yv3.append(float(objname.sw2p8aV[key]))
        yv4.append(float(objname.sw2p8bV[key]))
        yv5.append(float(objname.sw2p4V[key]))
        yv6.append(float(objname.sw1p4V[key]))

        yrdv1.append(float(objname.isu18p5[key]))
        yrdv2.append(float(objname.core1p0[key]))
        yrdv3.append(float(objname.xvr1p0[key]))
        yrdv4.append(float(objname.dig1p8[key]))
        yrdv5.append(float(objname.dig3p3[key]))
        yrdv6.append(float(objname.xvr1p2[key]))
        yrdv7.append(float(objname.div5p0[key]))
        yrdv8.append(float(objname.vdd3p3[key]))
        yrdv9.append(float(objname.rx2p5[key]))
        yrdv10.append(float(objname.tx2p5[key]))
        yrdv11.append(float(objname.adc1p8[key]))

        entry = pd.DataFrame.from_dict({
            'time':[key],
            'int': [float(objname.timetemp[key])],
            'ext1':[float(objname.ext1[key])],
            'ext2':[float(objname.ext2[key])],
            'ext3':[float(objname.ext3[key])],
            'ext4':[float(objname.ext4[key])],
            'isu18p5':[float(objname.isu18p5[key])],
            'core1p0':[float(objname.core1p0[key])],
            'xvr1p0':[float(objname.xvr1p0[key])],
            'dig1p8':[float(objname.dig1p8[key])],
            'dig3p3':[float(objname.xvr1p2[key])],
            'xvr1p2':[float(objname.xvr1p2[key])],
            'div5p0':[float(objname.div5p0[key])],
            'vdd3p3':[float(objname.vdd3p3[key])],
            'rx2p5':[float(objname.rx2p5[key])],
            'tx2p5':[float(objname.tx2p5[key])],
            'adc1p8':[float(objname.adc1p8[key])],
            'sw3p6A':[float(objname.sw3p6A[key])],
            'sw5p5A':[float(objname.sw5p5A[key])],

            'sw2p8aA':[float(objname.sw2p8aA[key])],
            'sw2p8bA':[float(objname.sw2p8bA[key])],
            'sw2p4A':[float(objname.sw2p4A[key])],
            'sw1p4A':[float(objname.sw1p4A[key])],
            'sw3p6V':[float(objname.sw3p6V[key])],
            'sw5p5V':[float(objname.sw5p5V[key])],
            'sw2p8aV':[float(objname.sw2p8aV[key])],
            'sw2p8bV':[float(objname.sw2p8bV[key])],
            'sw2p4V':[float(objname.sw2p4V[key])],
            'sw1p4V':[float(objname.sw1p4V[key])],
            'ModuleSn':[objname.sn]
            })

        df = pd.concat([df, entry], ignore_index=True)

   

    
        
    #figT = plt.figure()
    #plt.title(f"{objname.sn}-Temps")
    #plt.xlabel('Time(minutes)')
    #plt.ylabel('Temp(C)')
    #plt.plot(x,y,label = 'int')
    #plt.plot(x,y1,label = 'ext1')
    #plt.plot(x,y2,label = 'ext2')
    #plt.plot(x,y3,label = 'ext3')
    #plt.plot(x,y4,label = 'ext4')
    #plt.legend()
    #figT.savefig(f'C:\\Users\\CharlieAuwerda\\OneDrive - Rage Systems\\Desktop\\temps\\{objname.sn}-Temps.png')
    #figT=None

    #figI = plt.figure()
    #plt.title(f"{objname.sn}-I")
    #plt.xlabel('Time(minutes)')
    #plt.ylabel('mA')
    #plt.plot(x,yi1,label = 'sw3p6')
    #plt.plot(x,yi2,label = 'sw5p5')
    #plt.plot(x,yi3,label = 'sw2p8a')
    #plt.plot(x,yi4,label = 'sw2p8b')
    #plt.plot(x,yi5,label = 'sw2p4')
    #plt.plot(x,yi6,label = 'sw1p4')
    #plt.legend()

    #figI.savefig(f'C:\\Users\\CharlieAuwerda\\OneDrive - Rage Systems\\Desktop\\temps\\{objname.sn}-I.png')
    #figI = None

    #figV = plt.figure()
    #plt.title(f"{objname.sn}-V")
    #plt.xlabel('Time(minutes)')
    #plt.ylabel('mV')
    #plt.plot(x,yv1,label = 'sw3p6')
    #plt.plot(x,yv2,label = 'sw5p5')
    #plt.plot(x,yv3,label = 'sw2p8a')
    #plt.plot(x,yv4,label = 'sw2p8b')
    #plt.plot(x,yv5,label = 'sw2p4')
    #plt.plot(x,yv6,label = 'sw1p4')
    #plt.legend()
    #figV.savefig(f'C:\\Users\\CharlieAuwerda\\OneDrive - Rage Systems\\Desktop\\temps\\{objname.sn}-V.png')
    #figV=None

    #figRDV = plt.figure()
    #plt.title(f"{objname.sn}-RDV")
    #plt.xlabel('Time(minutes)')
    #plt.ylabel('mA')
    #plt.plot(x,yrdv1,label = 'isu18p5')
    #plt.plot(x,yrdv2,label = 'core1p0')
    #plt.plot(x,yrdv3,label = 'xvr1p0')
    #plt.plot(x,yrdv4,label = 'dig1p8')
    #plt.plot(x,yrdv5,label = 'dig3p3')
    #plt.plot(x,yrdv6,label = 'xvr1p2')
    #plt.plot(x,yrdv7,label = 'div5p0')
    #plt.plot(x,yrdv8,label = 'vdd3p3')
    #plt.plot(x,yrdv9,label = 'rx2p5')
    #plt.plot(x,yrdv10,label = 'tx2p5')
    #plt.plot(x,yrdv11,label = 'adc1p8')
    #plt.legend()
    #figRDV.savefig(f'C:\\Users\\CharlieAuwerda\\OneDrive - Rage Systems\\Desktop\\temps\\{objname.sn}-RDV.png')
    #figRDV = None


df.to_csv(f'C:\\Users\\CharlieAuwerda\\OneDrive - Rage Systems\\Desktop\\temps\\Burnin-readings.csv')