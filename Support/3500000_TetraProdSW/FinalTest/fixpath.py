import mysql.connector
import os


try:
		cnx = mysql.connector.connect(
			user='root', password='Pr0dRag343Ver!', database='TetraProd', host='192.168.3.66')
except mysql.connector.Error as err:
		print(err)
		print("FAIL")
cursor = cnx.cursor()



for id in range(89,591):
    q = f"SELECT Result_File_Path FROM tetra_header where id = {id};"
    cursor.execute(q)
    path = cursor.fetchone()
    if path:
        path = path[0]

        filename = os.path.basename(path)
        filename=filename.split('_')
        path = ((f'WAM/FinalTest/{filename[9]}/{filename[8]}').replace(" ", ""))
        q = f"UPDATE `tetra_header` SET `Result_File_Path` = '{path}' WHERE (`id` = {id});"
        print(q)
        cursor.execute(q)

cnx.commit()
cnx.close()
