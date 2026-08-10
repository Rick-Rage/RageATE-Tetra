import mysql.connector
import sys
import os
import csv

header = "tetra_header"

class Error(Exception):
	pass

def ProcessTestResults(location, cursor):
	#checking whether data is RX or TX
	if (location.find('TX') != -1 and location.find('TETRA') != -1):
		data = "tetra_TX_data"
		if(location.find('ATTEN') != -1):
			data = "tetra_ATT"

	elif(location.find('RX') != -1 and location.find('TETRA') != -1):
		data = "tetra_RX_data"

	else:
		print("Unrecognized File Name")
		raise Error

	columnname, headervalues, line_count = ReadHeader(location)

	state = ('INSERT INTO {} (').format(header)

	for item in columnname:
		state = state + item + ","

	state = state.rstrip(state[-1]) + ')'
	state = state + ' VALUES ('

	for item in headervalues:
		state = state + "'" + item + "',"

	state = state.rstrip(state[-1]) + ')'

	cursor.execute(state)

	ReadWriteData(location, line_count, data, cursor)


def ReadHeader(location):
	headervalues = []
	columnnames = []
	Testinfo = ''
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
								uploadFile(zipdir)
								row = keep
							row = row[0].replace("'", "")
							row = row.replace('#', '')
							row = row.replace('/', '_')
							row = row.split(":", 1)
							if row[0] == 'Date_Time':
								date = row[1].split('_')
								time = date[2].split(' ')[1]
								date = date[2].split(' ')[0] + '-' + date[0].replace(" ", "") + '-' +  date[1]
								datetime = date + ' ' + time
								headervalues.append(datetime)
								columnnames.append(row[0])
							else:
								headervalues.append(row[1])
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


def ReadWriteData(location, line_count, data, cursor):
	cursor.execute("SELECT id from tetra_header ORDER BY id DESC LIMIT 1;")
	idnum = cursor.fetchone()
	try:
		idnum = idnum[0]
	except:
		idnum = 0

	state = (('INSERT INTO {} (id,').format(data))
	state =  getcolumnnames(location,line_count,state)
	state = state + ' VALUES ({},'.format(idnum)

	with open(location) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		count = 0
		for row in csv_reader:
			count = count+1
			query = state
			if count > line_count+1:
				for item in row:

					query = query + "'" + item + "',"
				query = query.rstrip(query[-1]) + ')'
				cursor.execute(query)


def getcolumnnames(location, line_count, state):
	with open(location) as csv_file:
		names = []
		csv_reader = csv.reader(csv_file, delimiter=',')
		count = 0
		for row in csv_reader:
			count = count+1
			if count == line_count+1:
				for item in row:
					item = item.replace('(', '_')
					item = item.replace(')', '_')
					item = item.replace(' ', '_')
					item = "`" + item + "`"
					names.append(item)
					state = state + item + ","
				break
		state = state.rstrip(state[-1]) + ')'
		return(state)


def uploadFile(path):
	filename = os.path.basename(path)
	try:
		os.replace(path, ("C:\Users\ThomasWattson\temp\\{}").format(filename))
	except Exception as e:
		print(("Could not move {} to Synology Drive due to the following error:").format(filename))
		print(e)
	else:
		print(("Moved {} to Synology Drive").format(filename))


if __name__ == '__main__':
	#Connect to SQL:
	try:
		cnx = mysql.connector.connect(
			user='root', password='Pr0dRag343Ver!', database='TetraProd', host='192.168.3.66')
	except mysql.connector.Error as err:
		print(err)
		print("FAIL")
	cursor = cnx.cursor()


	for arg in sys.argv:
		if(arg.find(".py") != -1):
			continue
		else:
			filename = os.path.basename(arg)
			print(arg)
			cursor.execute(("SELECT id FROM `tetra_header` WHERE Result_File_Path LIKE '%{}'").format(filename))
			idnum = cursor.fetchone()
			print(idnum)
			if idnum != None:
				print("It seems this file already exists in the database would you like to overwrite it?(y/n)")
				userinput = input()
				if(userinput == 'y'):
					cursor.execute(("DELETE * FROM TetraProd.tetra_header WHERE id = '{}'").format(idnum))
					continue
				elif(userinput == 'n'):
					print("Exiting code")
					exit()
			filename = os.path.basename(arg)

			ProcessTestResults(arg, cursor)
			try:
				i = 0
			except Exception as e:
				print(("Failed to process: {} ").format(filename))
				print(("Due to the following error: {}").format(e))
				print("Stopping upload Process")
				exit()
			else:
				print(("Uploaded to database: {} ").format(filename))

	for arg in sys.argv:
		if(arg.find("NewFinalTest.py") != -1):
			continue
		else:
			uploadFile(arg)
			
			

	print("SUCCESS")
	cnx.commit()
	cnx.close()
