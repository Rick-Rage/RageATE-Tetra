import mysql.connector
import sys


try:
    cnx = mysql.connector.connect(user='root', password='Pr0dRag343Ver!', database='TetraProd', host='192.168.3.66')
except mysql.connector.Error as err:
    print(err)
    
cursor = cnx.cursor()
arglist = sys.argv[1].split(',')
print(arglist)
try:
    emp_num = arglist[0]
    emp_name = arglist[1]
except:
    print("Failed Expected command-line argument Employee Badge")
    
try:
    q = f"SELECT name FROM tetra_technicians WHERE emp_id = {emp_num}"
    cursor.execute(q)
    name = cursor.fetchone()
    name = name[0]
    print(f"Success: Employee Verified - {name}")   
except:
    print("Error: Unknown Employee Id - Check Badge ")
