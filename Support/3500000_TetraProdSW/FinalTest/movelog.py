import os
import os.path
import re
from datetime import datetime
import sys
import time
import mysql.connector


def normalize_pass_fail(value):
    value = value.strip()
    match = re.match(r'^\s*(PASS|FAIL)', value, re.IGNORECASE)
    if match:
        return match.group(1).upper()
    return value.split('(')[0].strip()


def parse_fields(line):
    line = line.strip().rstrip('\r')
    if '\t' in line:
        return [f.strip() for f in line.split('\t')]
    return [f.strip() for f in line.split(',')]


def updateSQL(last_line):
    try:
        cnx = mysql.connector.connect(
            user='root', password='Pr0dRag343Ver!', database='TetraProd', host='192.168.3.66')
    except mysql.connector.Error as err:
        print(err)
        print("FAIL")
        return
    cursor = cnx.cursor()
    fields = parse_fields(last_line)
    pass_fail = normalize_pass_fail(fields[6])
    q = (
        f"UPDATE Module set TXATTN_ID = '{fields[2]}', RXTest_ID = '{fields[4]}', "
        f"TXTest_ID = '{fields[3]}', BounceTest_ID = '{fields[5]}', "
        f"FinalTest_PF = '{pass_fail}' WHERE Module_SN = '{fields[7]}'"
    )
    try:
        cursor.execute(q)
    except Exception as err:
        print(err)

    cnx.commit()
    cursor.close()
    cnx.close()


def writetolog(filename, last_line):
    with open(f"C:\\SynologyDrive\\Logfile\\{filename}", "a", newline='') as file:
        file.write(last_line)


def createlog(filename, first_line):
    with open(f"C:\\SynologyDrive\\Logfile\\{filename}", "w", newline='') as file:
        file.write(first_line)


def openlocal(localfile):
    with open(localfile, "rb") as file:
        first_line = file.readline().decode()
        try:
            file.seek(-2, os.SEEK_END)
            while file.read(1) != b'\n':
                file.seek(-2, os.SEEK_CUR)
        except OSError:
            file.seek(0)
        last_line = file.readline().decode()
    return first_line, last_line


if __name__ == "__main__":
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    if currentMonth < 10:
        currentMonth = "0" + str(currentMonth)

    filename = "ATELog" + str(abs(currentYear) % 100) + str(currentMonth) + ".csv"

    try:
        first_line, last_line = openlocal(sys.argv[1])
    except Exception as err:
        print(f"Failed to upload due to: {err}")
        print("trying again...")
        time.sleep(1)
        try:
            first_line, last_line = openlocal(sys.argv[1])
        except:
            print("FAILED")
            exit()

    if os.path.isfile(f"C:\\SynologyDrive\\Logfile\\{filename}"):
        pass
    else:
        try:
            createlog(filename, first_line)
        except Exception as err:
            print(f"Failed to create file because: {err}")
            print("trying again")
            time.sleep(1)
            try:
                createlog(file, first_line)
            except:
                print("FAILED")
                exit()
    try:
        writetolog(filename, last_line)
    except Exception as err:
        print(f"Failed to update file because: {err}")
        print("trying again")
        time.sleep(1)
        try:
            writetolog(filename, last_line)
        except:
            print("FAILED")
            exit()
    updateSQL(last_line)
    print("SUCCESS")
