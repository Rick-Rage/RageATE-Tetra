from os import execl
import sys
import mysql.connector
from datetime import date, datetime, timedelta
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QDate
import csv

Password = "Pr0dRag343Ver!"

class SearchCriteriaDialog(QDialog):
    def __init__(self, module_serial_numbers, parent=None):
        super(SearchCriteriaDialog, self).__init__(parent)

        self.setWindowTitle("Select Search Criteria")
        self.layout = QVBoxLayout()

        # ComboBox for choosing search criteria
        self.choiceComboBox = QComboBox()
        self.choiceComboBox.addItem("Search by date range")
        self.choiceComboBox.addItem("Search by module serial number")
        self.choiceComboBox.currentIndexChanged.connect(self.on_choice_changed)
        self.layout.addWidget(self.choiceComboBox)

       
        # Label for date range or module serial number
        self.label = QLabel("Select a date range:")
        self.layout.addWidget(self.label)

        # Add date range selectors
        today_date = QDate.currentDate()
        one_week_ago_date = today_date.addDays(-7)

        self.startDateEdit = QDateEdit(one_week_ago_date)
        self.startDateEdit.setCalendarPopup(True)
        self.layout.addWidget(self.startDateEdit)

        self.endDateEdit = QDateEdit(today_date)
        self.endDateEdit.setCalendarPopup(True)
        self.layout.addWidget(self.endDateEdit)

         # Label and QLineEdit for module serial number
        self.serialNumberEdit = QLineEdit()
        self.serialNumberCompleter = QCompleter(module_serial_numbers)
        self.serialNumberEdit.setCompleter(self.serialNumberCompleter)
        self.layout.addWidget(self.serialNumberEdit)
        self.serialNumberEdit.hide()
        
        # Add OK and Cancel buttons
        self.okButton = QPushButton("OK")
        self.okButton.clicked.connect(self.accept)
        self.layout.addWidget(self.okButton)

        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.clicked.connect(self.reject)
        self.layout.addWidget(self.cancelButton)

        # Set the layout
        self.setLayout(self.layout)

    def on_choice_changed(self, index):
        if index == 0:
            self.label.setText("Select a date range:")
            self.startDateEdit.show()
            self.endDateEdit.show()
        elif index == 1:
            self.label.setText("Enter module serial number:")
            self.startDateEdit.hide()
            self.endDateEdit.hide()
            self.serialNumberEdit.show()
            
            
def connect():
    try:
        cnx = mysql.connector.connect(user='root', password=Password, database='TetraProd', host='192.168.3.66')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None
    else:
        return cnx
   
def write_to_csv(data, filename):
    # Open the file in write mode
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        if "Programming" in filename:
            writer.writerow(['PCB Serial #', 'Module ID', 'Config ID','ESN','ADCsync','Calcdc','SelfTest', 'Reason/Notes', 'fpga_fw_revision','fpga_sw_revision', 'pmic_sw_revision',])
        elif "FinalTest" in filename:
            writer.writerow(['id', 'Module_SN', 'PCB_SN', 'Config_ID', 'Asy_ID', 'Burnlot_ID', 'RXTest_ID', 'TXTest_ID', 'TXATTN_ID', 'BounceTest_ID', 'Config_PF', 'Asy_PF', 'Burnlot_PF', 'FinalTest_PF'])
            
        # Iterate through the list of lists and write each sublist as a row
        for row in data:
            writer.writerow(row[0:14])
            
def findFails(start_date,end_date,cursor):
    q=f"""SELECT m.PCB_SN, m.id, tc.id, tc.esn , tc.ADCsync,tc.calcdc,tc.SelfTest, tc.notes, tc.fpga_fw_revision, tc.fpga_sw_revision, tc.pmic_sw_revision
    FROM Module m
    JOIN tetra_configuration tc ON m.Config_ID = tc.id
    WHERE tc.date_time BETWEEN '{start_date}' AND '{end_date}' AND UPPER(m.Config_PF) = 'FAIL';"""
    cursor.execute(q)
    ans= list(cursor)
    if(not ans == []):
        write_to_csv(ans,f'Programming_Fails_{start_date}_{end_date}.csv')

    q=f"""SELECT m.*
    FROM Module m
    JOIN tetra_assembly ta ON m.Asy_ID = ta.id
    WHERE ta.date_time BETWEEN '{start_date}' AND '{end_date}' AND UPPER(m.Asy_PF) = 'FAIL';"""
    cursor.execute(q)
    ans= list(cursor)
    if(not ans == []):
        write_to_csv(ans,f'Assembly_Fails_{start_date}_{end_date}.csv')
        
    q=f"""SELECT m.*
    FROM Module m
    JOIN BounceHeader bh ON m.BounceTest_ID = bh.id
    WHERE bh.date_time BETWEEN '{start_date}' AND '{end_date}' AND UPPER(m.FinalTest_PF) = 'FAIL';"""
    cursor.execute(q)
    ans= list(cursor)
    if(not ans == []):
        write_to_csv(ans,f'FinalTest_Fails_{start_date}_{end_date}.csv')
        
def findFail_SN(MSN,cursor):
    q=f"""SELECT m.PCB_SN, m.id, tc.id, tc.esn , tc.ADCsync,tc.calcdc,tc.SelfTest, tc.notes, tc.fpga_fw_revision, tc.fpga_sw_revision, tc.pmic_sw_revision
    FROM Module m
    JOIN tetra_configuration tc ON m.Config_ID = tc.id
    WHERE m.Module_SN = '{MSN}';"""
    cursor.execute(q)
    ans= list(cursor)
    if(not ans == []):
        write_to_csv(ans,f'Programming_Fails_{start_date}_{end_date}.csv')

    q=f"""SELECT m.*
    FROM Module m
    JOIN tetra_assembly ta ON m.Asy_ID = ta.id
    WHERE ta.module_serial_number = '{MSN}';"""
    cursor.execute(q)
    ans= list(cursor)
    if(not ans == []):
        write_to_csv(ans,f'Assembly_Fails_{start_date}_{end_date}.csv')
        
    q=f"""SELECT m.*
    FROM Module m
    JOIN BounceHeader bh ON m.BounceTest_ID = bh.id
    WHERE bh.MSN =  '{MSN}';"""
    cursor.execute(q)
    ans= list(cursor)
    if(not ans == []):
        write_to_csv(ans,f'FinalTest_Fails_{start_date}_{end_date}.csv')
    
if __name__ == "__main__":
    cnx = connect()
    cursor = cnx.cursor(buffered=True)

    # Fetch module serial numbers from database (adapt this query for your database)
    cursor.execute("SELECT Module_SN FROM Module")
    module_serial_numbers = [row[0] for row in cursor.fetchall()]

    app = QApplication(sys.argv)
    dialog = SearchCriteriaDialog(module_serial_numbers)
    start_date = None
    end_date = None
    search_choice = None

    if dialog.exec_() == QDialog.Accepted:
        search_choice = dialog.choiceComboBox.currentText()

        if search_choice == "Search by date range":
            start_date = dialog.startDateEdit.date().toString(Qt.ISODate)
            end_date = dialog.endDateEdit.date().toString(Qt.ISODate)
            print(f"Search Choice: {search_choice}")
            print(f"Start Date: {start_date}")
            print(f"End Date: {end_date}")
        elif search_choice == "Search by module serial number":
            print(f"Search Choice: {search_choice}")
            MSN = dialog.serialNumberEdit.text()
    cursor = cnx.cursor(buffered=True)

    if search_choice == "Search by date range":
        findFails(start_date, end_date, cursor)
    elif search_choice == "Search by module serial number":
        findFail_SN(MSN,cursor)


    exit()
    sys.exit(app.exec_())