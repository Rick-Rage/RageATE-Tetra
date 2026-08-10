							

			






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
			data = "tetra_TX_ATT_data"

	elif(location.find('RX') != -1 and location.find('TETRA') != -1):
		data = "tetra_RX_data"

	else:
		print("Unrecognized File Name")
		raise Error

	columnname, headervalues, line_count = ReadHeader(location)

	getcolumnnames(location,line_count,data)


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
							row = row[0].replace("'", "")
							row = row.replace('#', '')
							row = row.replace('/', '_')
							row = row.split(":", 1)
							columnnames.append(row[0].replace(" ", "_"))
							if(columnnames[len(columnnames)-1] == 'TestType'):
								if (headervalues[len(headervalues)-1].find('TX') != -1):
									columnnames.append('TestVersion')
								else:
									columnnames.append('TestVersion')
							try:
								if columnnames[len(columnnames)-1] == 'Date_Time':
									cursor.execute(("ALTER TABLE {} ADD COLUMN {} DATETIME").format(
									header, columnnames[len(columnnames)-1]))

								cursor.execute(("ALTER TABLE {} ADD COLUMN {} VARCHAR(255)").format(
									header, columnnames[len(columnnames)-1]))
							except:
								continue
						else:
							continue
				elif row[0] == '#Begin Data':
					break

	return(columnnames, headervalues, line_count)

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def getcolumnnames(location, line_count, data):
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
			elif count == line_count+2:
				print(names)
				i = 0
				for item in row:
					length = len(item)+10
					
					if names[i].find("Bool") != -1:
						length = ('BOOL')

					elif item.isnumeric():
						length = ('INT')

					elif isfloat(item):
						length = ('FLOAT')
					else:
						length = ('VARCHAR(255)').format(length)					
					try:
						cursor.execute(("ALTER TABLE {} ADD COLUMN {} {}").format(data, names[i],length))
					except mysql.connector.Error as err:
						print(err)
						print(("ALTER TABLE {} ADD COLUMN {} {}").format(data, names[i],length))
					finally:
						i = i + 1
				break

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
			print(arg)
			continue
		else:
			filename = os.path.basename(arg)
			try:
				ProcessTestResults(arg, cursor)
			except Exception as e:
				print(("Failed to process: {} ").format(filename))
				print(("Due to the following error: {}").format(e))
				print("Stopping upload Process")
				exit()
			else:
				print(("Uploaded to database: {} ").format(filename))

	print("SUCCESS")
	cnx.commit()
	cnx.close()
