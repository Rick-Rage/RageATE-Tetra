import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTabWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QTextEdit, QLineEdit, QLabel, QTableWidget, QTableWidgetItem, QWidget, 
                             QSizePolicy)
from PyQt5.QtGui import QPixmap

from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
import mysql.connector
import datetime

cursor = None

class CustomTab(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.closeTab)

    def closeTab(self, index):
        if index > 0:  # 0 is the Home tab
            self.removeTab(index)

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setting up main window
        self.setWindowTitle('PyQt5 App')
        self.setGeometry(100, 100, 600, 400)
        self.apply_stylesheet()

        # Central widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Tab widget
        self.tabs = CustomTab(self)
        self.layout.addWidget(self.tabs)

        # Home tab
        self.home_tab = QWidget()
        self.home_layout = QVBoxLayout(self.home_tab)

        # Add logo and search in the home tab
        self.logo_and_search_layout = QHBoxLayout()

        # Multiple Search boxes and labels
        self.module_search_box = QLineEdit(self)
        self.module_search_box.setPlaceholderText("Search by Module Number...")
        
        self.deposition_search_box = QLineEdit(self)
        self.deposition_search_box.setPlaceholderText("Search by Deposition...")
        
        self.misc_search_box1 = QLineEdit(self)
        self.misc_search_box1.setPlaceholderText("Misc Search 1 (Dummy)...")
        
        self.misc_search_box2 = QLineEdit(self)
        self.misc_search_box2.setPlaceholderText("Misc Search 2 (Dummy)...")
        
        self.search_btn = QPushButton("Search", self)
        self.search_btn.clicked.connect(self.on_search)
        
        # Adding search boxes to the layout
        self.logo_and_search_layout.addWidget(self.module_search_box)
        self.logo_and_search_layout.addWidget(self.deposition_search_box)
        self.logo_and_search_layout.addWidget(self.misc_search_box1)
        self.logo_and_search_layout.addWidget(self.misc_search_box2)
        self.logo_and_search_layout.addWidget(self.search_btn)


        self.logo_label = QLabel(self)
        pixmap = QPixmap('RaGE_Color_100ppi_1in.png')
        self.logo_label.setPixmap(pixmap)
        self.logo_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.logo_and_search_layout.addWidget(self.logo_label)
        
        self.home_layout.addLayout(self.logo_and_search_layout)

        self.tabs.addTab(self.home_tab, "Home")

                # Add chart with two tabs
        self.chart_tab_widget = QTabWidget(self.home_tab)

        self.recent_chart = QTableWidget(1, 1, self)
        self.all_chart = QTableWidget(1, 1, self)

        self.populate_chart(self.recent_chart)
        self.populate_chart(self.all_chart)
        self.all_chart.setStyleSheet("background-color: #2a2a2a; color: #b9b9b9; gridline-color: #454545;")
        self.recent_chart.setStyleSheet("background-color: #2a2a2a; color: #b9b9b9; gridline-color: #454545;")
        
        self.chart_tab_widget.addTab(self.recent_chart, "Recent")
        self.chart_tab_widget.addTab(self.all_chart, "All")

        # Add the chart_tab_widget to home_layout
        self.home_layout.addWidget(self.chart_tab_widget)
        

    
        # Creating a search results table within chart_tab_widget
        self.search_results_chart = QTableWidget(5, 2, self)
        self.search_results_chart.setHorizontalHeaderLabels(['MRB id', 'Module SN', 'Location'])
        self.search_results_chart.setStyleSheet("background-color: #2a2a2a; color: #b9b9b9; gridline-color: #454545;")
        self.chart_tab_widget.addTab(self.search_results_chart, "Search Results")
        
        # Connecting the double-click event for the search_results_chart
        self.search_results_chart.cellDoubleClicked.connect(self.open_info_tab)
        self.recent_chart.cellDoubleClicked.connect(self.open_info_tab)
        self.all_chart.cellDoubleClicked.connect(self.open_info_tab)

    def populate_chart(self, chart):  
        cursor.execute("SELECT MRB.id,Module.id,Module.Module_SN,MRB.Location,MRB.FailLocation FROM MRB INNER JOIN Module ON MRB.Module_id = Module.id;")
        data = list(cursor)
        print(data)
        chart.verticalHeader().setVisible(False)
        chart.setColumnCount(len(data[0]))
        chart.setRowCount(len(data))
        chart.setHorizontalHeaderLabels(['MRB id','Module id', 'Module SN', 'Location','Fail Location'])
        
        for x in range(len(data)):
            for y in range(len(data[x])):

                chart.setItem(x, y, QTableWidgetItem(str(data[x][y])))


    def save_info(self):
        # Implement your save logic here.
        print("Save button clicked")

    def open_info_tab(self, row, col):
        module_info = self.sender().item(row, 2).text()
        module_id = self.sender().item(row,1).text()
        fail_station = self.sender().item(row,4).text()
        info_tab = QWidget()
        layout = QVBoxLayout(info_tab)
 
        layout.addWidget(QLabel(f"<h1><b>Serial Number: {module_info}</b></h1>\n"))
        
        cursor.execute(f"""SELECT config.ESN,config.date_time,config.pmic_sw_revision,config.fpga_sw_revision,config.fpga_fw_revision,tech.name
            FROM Module INNER JOIN tetra_configuration as config ON Module.Config_id = config.id
            INNER JOIN tetra_technicians as tech ON config.tech_id = tech.emp_id 
            Where Module.id = {module_id};""")
        data = list(cursor)
        if(fail_station == 'Config' or fail_station == 'Final'):
            layout.addWidget(QLabel(f"ESN: {data[0][0]}"))
            layout.addWidget(QLabel(f"Date Time: {data[0][1].strftime('%Y-%m-%d %H:%M:%S')}"))
            layout.addWidget(QLabel(f"PIC REV: {data[0][2]}"))
            layout.addWidget(QLabel(f"FPGA SoftWare REV: {data[0][3]}"))
            layout.addWidget(QLabel(f"FPGA FirmWare REV: {data[0][4]}"))
            layout.addWidget(QLabel("DC Test: {}"))
            layout.addWidget(QLabel("PASS/FAIL: {}"))
            layout.addWidget(QLabel(f"Operator: {data[0][5]}"))
        if(fail_station == 'Final'):
            layout.addWidget(QLabel(f"FinalTest Stuff: goes here"))
        layout.addWidget(QLabel(f"<h3>Dispotion for {module_info}<h3>"))
        self.disposition_text_edit = QTextEdit(self)
        layout.addWidget(self.disposition_text_edit)
        
        layout.addWidget(QLabel(f"<h3>Other Info for {module_info}<h3>"))
        self.other_info_text_edit = QTextEdit(self)
        layout.addWidget(self.other_info_text_edit)
        
        self.tabs.addTab(info_tab, f"Info for {module_info}")
        
        save_button = QPushButton("Save", self)
        save_button.clicked.connect(self.save_info)  # Connecting the button click to the save_info method
        layout.addWidget(save_button)

    def on_search(self):
        module_query = self.module_search_box.text()
        deposition_query = self.deposition_search_box.text()

        # For simplicity, we're assuming a match if either of the search boxes' content is a substring of the data
        matches = []
        for i in range(self.all_chart.rowCount()):
            module_item = self.all_chart.item(i, 0)
            if module_item and (module_query in module_item.text() or deposition_query in module_item.text()):
                matches.append((module_item.text(), self.all_chart.item(i, 1).text()))

        # Display results in the search_results_chart
        self.search_results_chart.setRowCount(len(matches))
        for i, (module, info) in enumerate(matches):
            self.search_results_chart.setItem(i, 0, QTableWidgetItem(module))
            self.search_results_chart.setItem(i, 1, QTableWidgetItem(info))

        # Switch to the "Search Results" tab
        self.chart_tab_widget.setCurrentWidget(self.search_results_chart)

    def apply_stylesheet(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2a2a2a;
            }
            QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem {
                background-color: #2a2a2a;
                border: 1px solid #454545;
                color: #b9b9b9;
            }
            QLabel {
                color: #b9b9b9;
            }
            QPushButton {
                background-color: #2a2a2a;
                color: #b9b9b9;
                border: 1px solid #454545;
            }
            QPushButton:hover {
                background-color: #454545;
                color: #ff0000;
            }
            QPushButton:pressed {
                background-color: #ff0000;
                color: #2a2a2a;
            }
            QHeaderView::section {
                background-color: #2a2a2a;
                color: #b9b9b9;
                border: 1px solid #454545;
                padding: 5px;
            }
            QTabWidget::pane {
                border: 1px solid #454545;
            }
            QTabWidget::tab-bar {
                left: 5px;
            }
            QTabBar::tab {
                background-color: #2a2a2a;
                border: 1px solid #454545;
                padding: 5px;
                margin: 2px;
            }
            QTabBar::tab:selected {
                background-color: #454545;
            }
            QTabBar::tab:hover {
                background-color: #ff0000;
                color: #2a2a2a;
            }
            QTableWidget {
                background-color: #2a2a2a;
                color: #b9b9b9;
                gridline-color: #454545;
            }
            QTableWidget QTableCornerButton::section {
                background-color: #2a2a2a;
                border: 1px solid #454545;
}
        """)

if __name__ == '__main__':
    try:
        cnx = mysql.connector.connect(
            user='root', password='Pr0dRag343Ver!', database='TetraProd', host='192.168.3.66')
    except mysql.connector.Error as err:
        print(err)
        print("FAIL")
    cursor = cnx.cursor()
    
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
