from threading import local
import mysql.connector
import openpyxl
import sys
import os
from psycopg2 import sql
import csv

header = "tetra_dvt_header"

def ProcessTestResults(location,cursor,idnum):


	#Connect to SQL:


	#checking whether data is RX or TX
	if (location.find('TX') != -1):
		data = "tetra_TX_data"
	else:
		data = "Tetra_RX_data"

	columnname,headervalues,line_count = ReadHeader(location)

	state = ('INSERT INTO {} (id,').format(header)

	for item in columnname:
		state = state + item + ","

	state = state.rstrip(state[-1]) + ')'
	state = state + ' VALUES ({},'.format(idnum)

	for item in headervalues:
		state = state + "'" + item + "',"

	state = state.rstrip(state[-1]) + ')'

	print(state)
	cursor.execute(state)

	ReadWriteData(location,line_count,data,cursor,idnum)

def ReadHeader(location):
	headervalues = []
	columnnames =[]
	Testinfo = ''
	with open(location) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			line_count = line_count+1
			if row != []:
				if( row[0] != '#Begin Data' and row[0] != '#RaGE Systems LLC'):
					if row[0] != '':
						if not (row[0].startswith('#INST')):
							row = row[0].replace("'","")
							row = row.replace('#','')
							row = row.replace('/','_')
							row = row.split(":",1)
							print(row)
							headervalues.append(row[1])
							columnnames.append(row[0].replace(" ","_"))
							if(columnnames[len(columnnames)-1] == 'TestType'):

								if (headervalues[len(headervalues)-1].find('TX') != -1):
									columnnames.append('TestVersion')
									headervalues.append('TX')
								else:
									columnnames.append('TestVersion')
									headervalues.append('RX')


						else:
							print("nope")
				elif row[0] == '#Begin Data':
					break

	return(columnnames,headervalues,line_count)

def ReadWriteData(location,line_count,data,cursor,idnum):
	state = (('INSERT INTO {} (id,').format(data))
	state =  getcolumnnames(location,line_count,state)
	state = state + ' VALUES ({},'.format(idnum)
	with open(location) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		count = 0
		for row in csv_reader:
			count=count+1
			query = state
			if count > line_count+1:
				for item in row:
					query = query + "'" + item + "',"
				query = query.rstrip(query[-1]) + ')'
				print(query)
				cursor.execute(query)


def getcolumnnames(location,line_count,state):
	with open(location) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		count = 0
		for row in csv_reader:
			count=count+1
			if count == line_count+1:
				for item in row:
					item = item.replace('(','_')
					item = item.replace(')','_')
					item = item.replace(' ','_')
					state = state + "`" + item + "`,"
				break
		state = state.rstrip(state[-1]) + ')'
		return(state)


if __name__ == '__main__':
	try:
		cnx = mysql.connector.connect(user='Charlie', password='42022RaGE!',database = 'testdb',host = '192.168.3.100')
	except mysql.connector.Error as err:
		print(err)
	cursor = cnx.cursor()

	cursor.execute("SELECT id from tetra_dvt_header ORDER BY id DESC LIMIT 1;")
	idnum = cursor.fetchone()
	try:
		idnum = idnum[0]
	except:
		idnum = 0

	for arg in sys.argv:
		if(arg.find("NewDVT.py") != -1):
			continue
		else:
			ProcessTestResults(arg,cursor,idnum)
	cnx.commit()
	cnx.close()
