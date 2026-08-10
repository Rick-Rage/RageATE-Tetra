#VER 2.2.2

from typing import DefaultDict
import mysql.connector
import sys
import os
import csv
import shutil
import math
from collections import defaultdict

header = None

class Error(Exception):
    pass

def ProcessTestResults(location, cursor):
    #checking whether data is RX or TX
    if (location.find('TX') != -1 and location.find('TETRA') != -1):
        data = "tetra_TX_data"
        if(location.find('ATTEN') != -1):
            data = "tetra_TX_ATT_data"
        header = "tetra_header"

    elif(location.find('RX') != -1 and location.find('TETRA') != -1):
        data = "tetra_RX_data"
        header = "tetra_header"
        
    elif(location.find('BOUNCE') != -1 and location.find('WAM') != -1):
        data = "Bounce_data"
        header = "BounceHeader"
    
    else:
        print("Unrecognized File Name")
        raise Error

    columnname, headervalues, line_count = ReadHeader(location)

    state = ('INSERT INTO {} (').format(header)

    for item in columnname:
        item = item.strip()
        state = state + item + ","

    state = state.rstrip(state[-1]) + ')'
    state = state + ' VALUES ('

    for item in headervalues:
        item = item.strip()
        state = state + "'" + item + "',"

    state = state.rstrip(state[-1]) + ')'
    cursor.execute(state)


    cols = ReadWriteData(location, line_count, data, cursor,header)
    return(cols)

#reads and parses the header of the csv and creates a statement to execute
def ReadHeader(location):
    headervalues = []
    columnnames = []
    Testinfo = ''
    directorylist = ['#Test Parameters File Name','#Payload Name','#Setup vi name','#RF Cal Path','#Cal Path','#Out Cal Path']
    with open(location) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count = line_count+1
            if row != []:
                if(row[0] != '#Begin Data' and row[0] != '#RaGE Systems LLC'):
                    if row[0] != '':


                        if (row[0].startswith('#caladc')):
                            row[0] = row[0].replace('caladc', 'caladc:')
                        if not (row[0].startswith('#INST') or not (':' in row[0])):
                            if (row[0].startswith('#CaptureFileDirectory')):
                                keep = row
                                row = row[0].split(":", 1)
                                row[1] = row[1].replace(" ", "",1)
                                zipdir = row[1]
                                zipdir = zipdir.replace("'","")
                                uploadFile(zipdir,header)
                                row = keep
                            pathcheck = row[0].split(":", 1)
                            if pathcheck[0] not in directorylist:
                                row = row[0].replace("'", "")
                                row = row.replace('#', '')
                                row = row.replace('/', '_')
                            else:
                                row = row[0]
                                row = row.replace("'", "")
                                row = row.replace('#', '')
                                row=row.replace("\\",'/')
                            row = row.split(":", 1)
                            if row[0] == 'Result File Path':
                                columnnames.append(row[0].replace(" ","_"))
                                filename = os.path.basename(location)
                                folder = filename
                                folder=folder.split('_')
                                headervalues.append(f'WAM/FinalTest/{folder[5]}/{folder[4]}/{filename}')
                            elif row[0] == 'Date_Time':
                                date = row[1].split('_')
                                time = date[2].split(' ')[1]
                                date = date[2].split(' ')[0] + '-' + date[0].replace(" ", "") + '-' +  date[1]
                                datetime = date + ' ' + time
                                headervalues.append(datetime)
                                columnnames.append(row[0])
                            else:
                                headervalues.append(row[1].replace(" ", "", 1))
                                columnnames.append(row[0].replace(" ", "_"))
                            if(columnnames[len(columnnames)-1] == 'TestType'):
                                if (headervalues[len(headervalues)-1].find('TX') != -1):
                                    columnnames.append('TestVersion')
                                    headervalues.append('TX')
                                else:
                                    columnnames.append('TestVersion')
                                    headervalues.append('RX')
                        else:
                            continue
                elif row[0] == '#Begin Data':
                    break

    return(columnnames, headervalues, line_count)

#writes the majority of the data to the database
def ReadWriteData(location, line_count, data, cursor,header):
    #gets the corresponding id from the header table
    cursor.execute(f"SELECT id from {header} ORDER BY id DESC LIMIT 1;")
    idnum = cursor.fetchone()
    try:
        idnum = idnum[0]
    except:
        idnum = 0

    state = (('INSERT INTO {} (id,').format(data))
    state,timeslot,names =  getcolumnnames(location,line_count,state)
    state = state + ' VALUES ({},'.format(idnum)
    
    state = state.replace("`TBD`,","")
  
    
    cols = defaultdict(list)

    with open(location) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        for row in csv_reader:
            count = count+1
            query = state
            if count > line_count+1:
                itemcount=0
                for item in row:
                    name = names[itemcount]
                    if name == "`TBD`":
                        names.remove("`TBD`")
                        continue
                    if(item.find('ERROR') != -1):
                        item = 'null'
                    if(len(item)>255):
                        item = item[0:255]
                    if itemcount == timeslot:
                        datetime = item.split(' ')
                        date = datetime[0]
                        time = datetime[1]
                        if "PM" in time:
                            time = time.split(":")
                            time[0] = time[0] + 12
                        else:
                            time = time.split(":")

                        if int(time[0]) >= 24:
                            time[0] = "00"
                        try:
                            time = time[0] + ":" +time[1] + ":" +  time[2]
                        except:
                            time = time[0] + ":" + time[1] + ":00"

                        date = date.split("/")
                        try:
                            date = date[2] + "-" + date[0] + "-" + date[1]
                        except:
                            date = date[0]
                        item = date +" "+ time
                    query = query + "'" + item + "',"

                    cols[name].append(item)
                    itemcount = itemcount + 1
                query = query.rstrip(query[-1]) + ')'
                cursor.execute(query)

    return(cols)

def CheckUpload(location,cursor,cols,header):

    cursor.execute(f"SELECT id from {header} ORDER BY id DESC LIMIT 1;")
    idnum = cursor.fetchone()
    try:
        idnum = idnum[0]
    except:
        idnum = 0

    cursor.execute(f"SELECT Test_Name from {header} where id = {idnum}")
    testtype = cursor.fetchone()[0]


    if testtype == 'REV-C_TETRA_TX-PROD' or testtype == 'REV-C_TETRA_TX-PROD-DVT-TEMP':
        table = 'tetra_TX_data'
    elif testtype == 'REV-C_TETRA_RX-PROD' or testtype == 'REV-C_TETRA_RX-PROD-DVT-TEMP':
        table = 'tetra_RX_data'
    elif testtype == 'WAM-C_BOUNCE':
        table = 'Bounce_data'
    elif testtype == 'REV-C_TETRA_TX-ATTEN':
        table = 'tetra_TX_ATT_data'



    #cursor.execute(f"SELECT MIN(count_id) from {table} where id = {idnum}")
    #countid = cursor.fetchone()[0]

    #cursor.execute(f"SELECT MAX(count_id) from {table} where id = {idnum}")
    #countidmax = cursor.fetchone()[0]
    #flag = 0
    #for key in cols:
    #    truecount = 0
    #    for i in range(countid,countidmax+1):
    #        cursor.execute(f"SELECT {key} from {table} where id = {idnum} and count_id = {i}")
    #        value = cursor.fetchone()[0]
    #        print(i)
    #        try:
    #            value = float(value)
    #            cols[key][truecount] = float(cols[key][truecount])
    #        except:
    #            p = 2

    #        try:
    #            if(not (math.isclose(value,cols[key][truecount],abs_tol = 0.5))):
    #                flag = 1
    #        except:
    #            if(value != cols[key][truecount]):

    #                if(str(cols[key][truecount]).find("C:") != -1):
    #                    A = 2
    #                else:
    #                    print(cols[key][truecount])
    #                    print(value)
    #                    flag = 1

    #if(flag == 1):
    #     print("Verification Failed there could be a problem in the upload")
    print(testtype + f" database id: {idnum}")




#gets the column names of the data given the csv and the line count to #begindata
def getcolumnnames(location, line_count, state):
    with open(location) as csv_file:
        names = []
        timeslot=-1
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        for row in csv_reader:
            count = count+1
            if count == line_count+1:
                rowcount = 0
                for item in row:
                    item = item.replace('(', '_')
                    item = item.replace(')', '_')
                    item = item.replace(' ', '_')
                    item = item.replace('|','_')
                    item = item.replace('-','_')
                    item = item.replace('°','_')
                    item = item.replace('/','_')
                    item = "`" + item + "`"
                    names.append(item)
                    state = state + item + ","
                    if item == '`abs_time_stamp_`':
                        timeslot = rowcount
                    rowcount = rowcount + 1
                break
        state = state.rstrip(state[-1]) + ')'
        return(state,timeslot,names)

#uploads file to synology drive
def uploadFile(path,header):
    if path == "<nocapture>":
        return
    filename = os.path.basename(path)
    folder = filename
    folder=folder.split('_')

    
    if header == "BounceHeader":
        folder[5] = "Bounce"
        
    folderpath = folder[5] + '\\' + folder[4]

    try:
        os.mkdir(('C:\\SynologyDrive\\{}').format(folder[5]))
    except Exception as e:
        pass
    try:
        os.mkdir(('C:\\SynologyDrive\\{}\\{}').format(folder[5],folder[4]))
    except:
        pass
    try:
        shutil.copy2(path, ("C:\\SynologyDrive\\{}\\{}").format(folderpath,filename))
    except Exception as e:
        print(("Could not move {} to Synology Drive due to the following error:").format(filename))
        print(e)
    else:
        print(("Moved {} to Synology Drive").format(filename))
    return

if __name__ == '__main__':
    #Connect to SQL:
    try:
        cnx = mysql.connector.connect(
            user='root', password='Pr0dRag343Ver!', database='TetraProd', host='192.168.3.66')
    except mysql.connector.Error as err:
        print(err)
        print("FAIL")
    cursor = cnx.cursor()
    
    # go through system args don't care about python file
    for arg in sys.argv:
        if(arg.find(".py") != -1):
            continue
        else:
            filename = os.path.basename(arg)
            if (filename.find("BOUNCE") != -1):
                header = "BounceHeader"
            else:
                header = "tetra_header"
            cols = ProcessTestResults(arg, cursor)
            cnx.commit()
            CheckUpload(arg,cursor,cols,header)

    for arg in sys.argv:
        if(arg.find(".py") != -1):
            continue
        else:
            uploadFile(arg,header)



    print("SUCCESS")

    cnx.close()
