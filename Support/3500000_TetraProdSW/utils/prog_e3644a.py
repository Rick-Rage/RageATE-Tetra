import pyvisa
import time
import os
import subprocess as sp

def reset(inst):
    inst.write("*rst; status:preset; *cls")

def SetV(inst,voltage):
    inst.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % voltage)

def SetILim(inst,ISupplySet):
    inst.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % ISupplySet)

def PowerOn(inst):
    inst.write(':OUTPut:STATe 1')

def PowerOff(inst):
    inst.write(':OUTPut:STATe 0')

def PowerCycle(inst):
    PowerOff(inst)
    PowerOn(inst)

def readDisplay(inst):
    voltCH1 = float(inst.query('MEAS:VOLT?'))
    time.sleep(7)
    currentCH1 = float(inst.query('MEAS:CURR?'))
    powerCH1 = voltCH1 * currentCH1
    print(f'V={voltCH1:.1f}V I={currentCH1:.2f}A P={powerCH1:.2f}W')
    return (voltCH1,currentCH1,powerCH1)




if __name__=='__main__':
     ISupplySet = 2#amps
     configTime = 7
     rm = pyvisa.ResourceManager()
     print(rm.list_resources())
     print(rm.list_resources())
     #inst = rm.open_resource('GPIB0::5::INSTR')
     #reset(inst)
     #SetV(inst,17)
     #SetILim(inst,ISupplySet)
     #PowerOn(inst)
#     v,i,p = readDisplay(inst)
#     pic_status = False
#     if (v >= 17) or (v <= 19):
#         print("Power Ok")
#         prog_pic()
#         with open("log.txt",'r') as fh:
#             content = fh.read()
#             if 'Program Succeeded.' in content:
#                 print('Pic Programmed Succesfully')
#                 pic_status = True
#             else:
#                 print('Pic failed to Program')
#     if pic_status:
#         PowerCycle(inst)
#         v,i,p = readDisplay(inst)
#         if (v >= 17) or (v <= 19):
#             print("Power Ok")

























# listMode = [5,0,5,0,5,0,5,0,5,0,5,0]
# try:
#    #Open Connection Keysight Visa
#     rm = visa.ResourceManager()
#    #Connect to VISA Address
#    #GPIB Connection: 'GPIP0::xx::INSTR'
#     myinst = rm.open_resource("GPIB0::13::INSTR")
#     #Set Timeout - 5 seconds
#     myinst.timeout = 5000
#     #*IDN? - Query Instrumnet ID
#     myinst.write("*IDN?")
#     print(myinst.read())
#     #Select Channel Output to program, This line is multiple channel output
#     myinst.write(':INSTrument:NSELect 1')
#     #Enable output ON
#     myinst.write(':OUTPut:STATe 1')
#     #generate voltage level output in sequence
#     for x in range (len(listMode)):
#         myinst.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % listMode[x])
#         #change this delay to increase or decrease output intervals
#         myinst.timeout = 1000
#
# #Close Connection
#     myinst.close()
#     print 'close instrument connection'
# except Exception as err:
#     print 'Exception: ' + str(err.message)
# finally:
# #perform clean up operations
#     print 'complete'
