from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import sys
import os

# To open Designer: qt5-tools designer
# To convert .ui file to .py file: pyuic5 -x filename.ui -o filename.py

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
hour_labels = ["9:00", "9:50", "10:40", "11:30", "12:30", "1:30", "2:20", "3:10", "4:00"]

tab_titles = ["Teachers", "Classes", "Labs", "Relations", "Output Generator"]
tab_columns = [["Name", "Operation"], ["Name","Subjects","Lab Subjects", "Operation"], ["Name", "Operation"],["Subject", "Class", "Teacher", "Lectures", "Operation"], []]

class TimeTableGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.new_window_size = self.calculateNewWindowSize()
        self.data = {title: [] for title in tab_titles[:-1]}

    def initUI(self):
        self.setFixedSize(716, 553)
        self.setWindowTitle("Time Table Generator")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.createWidgets()

    def calculateNewWindowSize(self):
        main_window_size = self.size()
        new_window_width = main_window_size.width() * 0.8
        new_window_height = main_window_size.height() * 0.8
        return QtCore.QSize(int(new_window_width), int(new_window_height))

    def createWidgets(self):
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        for title, columns in zip(tab_titles, tab_columns):
            self.createTab(title, columns)

    def createTab(self, title, columns):
        tab = QWidget()
        self.tabs.addTab(tab, title)
        layout = QVBoxLayout()
        table = QTableWidget()
        table.setColumnCount(len(columns))
        table.setHorizontalHeaderLabels(columns)
        layout.addWidget(table)

        add_button_layout = QHBoxLayout()
        if title == "Output Generator":
            generate_button = QPushButton("Generate", self)
            generate_button.clicked.connect(self.generateButtonClicked)
            add_button_layout.addWidget(generate_button)
        else:
            add_button = QPushButton(f"Add {title}", self)
            import_button = QPushButton("Import from CSV", self)
            import_button.clicked.connect(self.importButtonClicked)
            add_button.clicked.connect(lambda _, t=title: self.addButtonClicked(t))
            add_button_layout.addWidget(add_button)
            add_button_layout.addWidget(import_button)
        layout.addLayout(add_button_layout)
        tab.setLayout(layout)

    def processData(self, title):
        current_tab_index = self.tabs.currentIndex()
        current_tab_title = self.tabs.tabText(current_tab_index)
        current_table = self.tabs.widget(current_tab_index).findChild(QTableWidget)
        row_position = current_table.rowCount()
        data = {col: self.lineEdits[col].text() for col in tab_columns[tab_titles.index(title)] if col != "Operation"}
        existing_data = self.data[title]
        existing_index = None
        for idx, item in enumerate(existing_data):
            if item['Name'] == data.get('Name'):
                existing_index = idx
                break
        if existing_index is not None:
            existing_data[existing_index] = data
        else:
            current_table.insertRow(row_position)
            existing_data.append(data)
            for idx, col in enumerate(tab_columns[tab_titles.index(title)]):
                if col == "Operation":
                    continue
                current_table.setItem(row_position, idx, QTableWidgetItem(data[col]))
            if title != "Output Generator":
                delete_button = QPushButton("Delete")
                delete_button.clicked.connect(lambda: self.deleteEntry(current_table, row_position))
                current_table.setCellWidget(row_position, len(tab_columns[tab_titles.index(title)]) - 1, delete_button)
        self.sender().parent().close()

    def addButtonClicked(self, title):
        dialog = QDialog(self)
        dialog.setFixedSize(self.new_window_size)
        dialog.setWindowTitle(f"Add {title}")
        layout = QVBoxLayout()
        grid_layout = QGridLayout()
        self.lineEdits = {}
        for idx, col in enumerate(tab_columns[tab_titles.index(title)]):
            if col == "Operation":
                continue
            label = QLabel(col + ":")
            line_edit = QLineEdit()
            grid_layout.addWidget(label, idx, 0)
            grid_layout.addWidget(line_edit, idx, 1)
            self.lineEdits[col] = line_edit
        layout.addLayout(grid_layout)
        button_layout = QHBoxLayout()
        btnFinish = QPushButton("Finish")
        btnFinish.clicked.connect(lambda: self.processData(title))
        button_layout.addWidget(btnFinish)
        btnCancel = QPushButton("Cancel")
        btnCancel.clicked.connect(dialog.close)
        button_layout.addWidget(btnCancel)
        layout.addLayout(button_layout)
        dialog.setLayout(layout)
        dialog.exec_()

    def importButtonClicked(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Import CSV", "", "CSV Files (*.csv)")
        if filename:
            try:
                with open(filename, 'r') as file:
                    csv_data = [line.strip().split(',') for line in file]
                current_tab_index = self.tabs.currentIndex()
                current_table = self.tabs.widget(current_tab_index).findChildren(QTableWidget)[0]
                current_table.setRowCount(0)
                for row_data in csv_data:
                    current_table.insertRow(current_table.rowCount())
                    for index, col_data in enumerate(row_data):
                        new_item = QTableWidgetItem(col_data)
                        current_table.setItem(current_table.rowCount() - 1, index, new_item)
            except Exception as e:
                print("Error during import operation:", e)

    def deleteEntry(self, current_table, row_position):
        current_tab_index = self.tabs.currentIndex()
        current_tab_title = self.tabs.tabText(current_tab_index)
        current_table = self.tabs.widget(current_tab_index).findChild(QTableWidget)
        current_table.removeRow(row_position)
        removed_item = self.data[current_tab_title].pop(row_position)
        print(f"Removed item: {removed_item}")

    def generateButtonClicked(self):
        os.system('cls')
        for title, data_list in self.data.items():
            print(f"{title} Data:", data_list)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TimeTableGenerator()
    win.show()
    sys.exit(app.exec_())