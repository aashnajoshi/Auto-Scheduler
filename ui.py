from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import sys
import os
from generator import *

# To open Designer: qt5-tools designer
# To convert .ui file to .py file: pyuic5 -x filename.ui -o filename.py

os.system('cls')

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
hour_labels = ["9:00", "9:50", "10:40", "11:30", "12:30", "1:30", "2:20", "3:10", "4:00"]

tab_titles = ["Teachers", "Classes", "Labs", "Relations", "Output Generator"]
tab_columns = [["Name", "Operation"], ["Name","Subjects","Lab Subjects", "Operation"], ["Name", "Operation"],["Subject", "Class", "Name", "Lectures", "Operation"], []]

class TimeTableGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.new_window_size = self.calculateNewWindowSize()
        self.data={
        'Teachers': [{'Name': 'teacher1'}, {'Name': 'teacher2'}, {'Name': 'teacher3'}, {'Name': 'teacher4'}, {'Name': 'teacher5'}],
        'Classes': [{'Name': 'aiml', 'Subjects': 'sub1,sub2,sub3,sub4', 'Lab Subjects': 'lab_sub3,lab_sub2'}, {'Name': 'cse', 'Subjects': 'sub1,sub2,sub4,sub5', 'Lab Subjects': 'lab_sub2,lab_sub5'}, {'Name': 'ece', 'Subjects': 'sub1,sub5,sub6', 'Lab Subjects': 'lab_sub1'}], 
        'Labs': [{'Name': 'lab1'}, {'Name': 'lab2'}, {'Name': 'lab3'}, {'Name': 'lab4'}],
        'Relations': [{'Subject': 'sub1', 'Class': 'aiml', 'Name': 'teacher1', 'Lectures': '3'}, {'Subject': 'sub1', 'Class': 'cse', 'Name': 'teacher1', 'Lectures': '3'}, {'Subject': 'sub5', 'Class': 'ece', 'Name': 'teacher1', 'Lectures': '3'}, {'Subject': 'sub2', 'Class': 'aiml', 'Name': 'teacher2', 'Lectures': '3'}, {'Subject': 'sub2', 'Class': 'cse', 'Name': 'teacher2', 'Lectures': '2'}, {'Subject': 'sub1', 'Class': 'ece', 'Name': 'teacher2', 'Lectures': '3'}, {'Subject': 'lab_sub2', 'Class': 'aiml', 'Name': 'teacher2', 'Lectures': '1'}, {'Subject': 'lab_sub2', 'Class': 'cse', 'Name': 'teacher2', 'Lectures': '1'}, {'Subject': 'sub3', 'Class': 'aiml', 'Name': 'teacher3', 'Lectures': '2'}, {'Subject': 'lab_sub3', 'Class': 'aiml', 'Name': 'teacher3', 'Lectures': '1'}, {'Subject': 'lab_sub1', 'Class': 'ece', 'Name': 'teacher3', 'Lectures': '1'}, {'Subject': 'sub4', 'Class': 'aiml', 'Name': 'teacher4', 'Lectures': '4'}, {'Subject': 'sub4', 'Class': 'cse', 'Name': 'teacher4', 'Lectures': '2'}, {'Subject': 'sub5', 'Class': 'cse', 'Name': 'teacher5', 'Lectures': '4'}, {'Subject': 'sub6', 'Class': 'ece', 'Name': 'teacher5', 'Lectures': '3'}, {'Subject': 'lab_sub5', 'Class': 'cse', 'Name': 'teacher5', 'Lectures': '1'},]}
        self.classes_data = {item['Name']: item for item in self.data['Classes']}
        self.teachers_data = {item['Name']: item for item in self.data['Teachers']}
        self.initUI()

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
        self.fillData()

    def createTab(self, title, columns):
        tab = QWidget()
        self.tabs.addTab(tab, title)
        layout = QVBoxLayout()

        if title == "Output Generator":
            dropdown_layout = QHBoxLayout()
            self.class_dropdown = QComboBox()
            self.class_dropdown.addItem("Select Class Timetable")
            for cls in self.classes_data.keys():
                self.class_dropdown.addItem(f"Class Timetable ({cls})")
            self.class_dropdown.currentIndexChanged.connect(self.show_class_timetable)
            dropdown_layout.addWidget(self.class_dropdown)

            self.teacher_dropdown = QComboBox()
            self.teacher_dropdown.addItem("Select Teacher's Timetable")
            for teacher in self.teachers_data.keys():
                self.teacher_dropdown.addItem(f"Teacher's Timetable ({teacher})")
            self.teacher_dropdown.currentIndexChanged.connect(self.show_teacher_timetable)
            dropdown_layout.addWidget(self.teacher_dropdown)
            layout.addLayout(dropdown_layout)

            self.table_widget = QTableWidget()
            layout.addWidget(self.table_widget)

            generate_button = QPushButton("Generate")
            generate_button.clicked.connect(self.generateButtonClicked)
            layout.addWidget(generate_button)

        else:
            table = QTableWidget()
            table.setColumnCount(len(columns))
            table.setHorizontalHeaderLabels(columns)
            layout.addWidget(table)

            add_button_layout = QHBoxLayout()
            add_button = QPushButton(f"Add {title}", self)
            import_button = QPushButton("Import from CSV", self)
            import_button.clicked.connect(self.importButtonClicked)
            add_button.clicked.connect(lambda _, t=title: self.addButtonClicked(t))
            add_button_layout.addWidget(add_button)
            add_button_layout.addWidget(import_button)
            if title == "Relations":
                import_button.hide()
            layout.addLayout(add_button_layout)
        tab.setLayout(layout)

    def fillData(self):
        for title, data_list in self.data.items():
            tab_index = tab_titles.index(title)
            current_table = self.tabs.widget(tab_index).findChild(QTableWidget)
            current_table.setRowCount(0)  # Clear existing data
            for row, item in enumerate(data_list):
                current_table.insertRow(row)
                for col, (key, value) in enumerate(item.items()):
                    item_widget = QTableWidgetItem(value)
                    current_table.setItem(row, col, item_widget)
                if current_table.cellWidget(row, len(tab_columns[tab_titles.index(title)]) - 1) is None:
                    delete_button = QPushButton("Delete")
                    delete_button.clicked.connect(lambda _, r=row: self.deleteEntry(current_table, r))
                    current_table.setCellWidget(row, len(tab_columns[tab_titles.index(title)]) - 1, delete_button)

    def processData(self, title):
        current_tab_index = self.tabs.currentIndex()
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
            if current_table.cellWidget(existing_index, len(tab_columns[tab_titles.index(title)]) - 1) is None:
                delete_button = QPushButton("Delete")
                delete_button.clicked.connect(lambda: self.deleteEntry(current_table, existing_index))
                current_table.setCellWidget(existing_index, len(tab_columns[tab_titles.index(title)]) - 1, delete_button)
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
        for title, data_list in self.data.items():
            if title == current_tab_title:
                continue
            for item in data_list:
                for key, value in item.items():
                    if isinstance(value, str) and value == removed_item.get('Name'):
                        item[key] = None

    def generateButtonClicked(self):
        index = self.class_dropdown.currentIndex()
        if index != 0:
            cls = list(self.classes_data.keys())[index - 1]
            initialize(self.data)
            T_T_G([cls])
            output = f"{cls}\n"
            for r in ctt[cls]:
                output += str(r) + "\n"
            self.table_widget.clear()
            self.table_widget.setRowCount(len(ctt[cls]))
            self.table_widget.setColumnCount(len(ctt[cls][0]))
            self.populate_table(ctt[cls])

        index = self.teacher_dropdown.currentIndex()
        if index != 0:
            teacher = list(self.teachers_data.keys())[index - 1]
            initialize(self.data)
            T_T_G([teacher])
            output = f"{teacher}\n"
            for r in ttt[teacher]:
                output += str(r) + "\n"
            self.table_widget.clear()
            self.table_widget.setRowCount(len(ttt[teacher]))
            self.table_widget.setColumnCount(len(ttt[teacher][0]))
            self.populate_table(ttt[teacher])

    def show_class_timetable(self, index):
        if index != 0:
            cls = list(self.classes_data.keys())[index - 1]
            self.populate_table(ctt[cls])

    def show_teacher_timetable(self, index):
        if index != 0:
            teacher = list(self.teachers_data.keys())[index - 1]
            self.populate_table(ttt[teacher])

    def populate_table(self, data):
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        hour_labels = ["9:00", "9:50", "10:40", "11:30", "12:30", "1:30", "2:20", "3:10", "4:00"]

        self.table_widget.clear()
        self.table_widget.setRowCount(len(data))
        self.table_widget.setColumnCount(len(data[0]))
        self.table_widget.setVerticalHeaderLabels(days_of_week)
        self.table_widget.setHorizontalHeaderLabels(hour_labels)

        for r, row in enumerate(data):
            for c, cell in enumerate(row):
                item = QTableWidgetItem(str(cell))
                self.table_widget.setItem(r, c, item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TimeTableGenerator()
    win.show()
    sys.exit(app.exec_())