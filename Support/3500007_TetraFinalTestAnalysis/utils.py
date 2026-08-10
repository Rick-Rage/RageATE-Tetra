
def ReadIni(path):
    ini = {}
    a = {}
    folder = ''
    with open(path, "r") as fp:
        for line in fp:
            if ';' in line:
                fields = line.split(';')
                line = fields[0]
            line = line.strip()
            if len(line) == 0:
                continue
            if line[0] == '[':
                if line[-1] == ']':
                    if len(a) > 0:
                        ini[folder] = a
                        a = {}
                    folder = line[1:-1]
            elif '=' in line:
                fields = line.split('=')
                key = fields[0].strip()
                value = fields[1].strip()
                a[key] = value
    if len(a) > 0:
        ini[folder] = a
        a = {}
    return ini



test_names = [
        'Transmit Power Supply Consumption Limits', 'Receive Power Supply Consumption Limits','Reference Source Port Return Loss','Transmit Output Frequency',
         'Transmit In-Band Output Peak Power', 'Harmonics','Transmit Power Flatness',
         "Receiver Input Frequency","Receiver Gain",'Receiver Noise Figure',"Bounce Test",
         'Temperature Sensors'
         ]
test_names = [
                {'txPwrCom':'Transmit Power Supply Consumption Limits'},{'rxPwrCom''Receive Power Supply Consumption Limits'}, {"rl":'Reference Source Port Return Loss'},{"txFreqOut":'Transmit Output Frequency'},
                {"txPout":'Transmit In-Band Output Peak Power'}, {"harm":'Harmonics'},{"flat":'Transmit Power Flatness'},
                { "rxFreq":"Receiver Input Frequency"},{"xcvrGain":"Receiver Gain"},{"nf":'Receiver Noise Figure'},{"bounce":"Bounce Test"},
                {"temp":'Temperature Sensors'}
         ]
table_one = [
        'RaGE Part Number',"Leidos Part Number",'Revision',
        'Serial Number','FW Revision',"SW Revision",'Test Code Revision',
        'pm-IC Revision','Date Tested','Report Type','Overall DUT Status',
        ]

table_two_col = [
        'Temperature','Power Supply','Reference Clock',
        'RF LO Frequency','RF LO Power'
        ]
table_two_data = [f'25°C','18.75 V','18.75 MHz','10-20 GHz','12.5 dBm']


nda_text="""This Specification includes materials which are Proprietary and Confidential to RaGE Systems Inc and Leidos Security Detection & Automation.
            This material is covered under an NDA and may only be used and disseminated in a manner
            consistent with said NDA.Any other use and or dissemination is strictly prohibited.(C) 2022 Rage Systems Co-op. All Rights Reserved"""

results_table_name = 'TEST RESULTS FOR ANTENNA WIDEBAND ANTENNA MODULE'
