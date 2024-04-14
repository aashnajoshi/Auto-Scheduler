from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import warnings
import sys

warnings.filterwarnings("ignore", category=DeprecationWarning)

class TimeTableGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.new_window_size = self.calculateNewWindowSize()

    def initUI(self):
        self.setFixedSize(716, 553)
        self.setWindowTitle("Time Table Generator")
        self.setWindowIcon(QIcon('icon.png'))

        self.createMenuBar()
        self.createWidgets()

    def createMenuBar(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")
        self.createMenuItem(file_menu, "New", self.newFile)
        self.createMenuItem(file_menu, "Save As", self.saveAs)
        self.createMenuItem(file_menu, "Settings", self.settings)
        self.createMenuItem(file_menu, "Exit", self.close)

        help_menu = menubar.addMenu("Help")
        self.createMenuItem(help_menu, "Instructions", self.instructions)
        self.createMenuItem(help_menu, "About", self.about)

    def createMenuItem(self, menu, title, function):
        action = QAction(title, self)
        action.triggered.connect(function)
        menu.addAction(action)

    def createWidgets(self):
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        tab_titles = ["Instructors", "Rooms", "Subjects", "Sections", "Scenario Manager"]
        tab_columns = [["Available", "Name", "Hours", "Operation"], ["Available", "Name", "Operation"], ["Code", "Name", "Type", "Instructors", "Operation"], ["Available", "Name", "Stay in Room", "Operation"], []]

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

        if title != "Scenario Manager":
            add_button_layout = QHBoxLayout()
            add_button = QPushButton(f"Add {title[:-1]}", self)
            if title == "Instructors":
                add_button.clicked.connect(self.addInstructorButtonClicked)
            elif title == "Rooms":
                add_button.clicked.connect(self.addRoomButtonClicked)
            elif title == "Subjects":
                add_button.clicked.connect(self.addSubjectButtonClicked)
            elif title == "Sections":
                add_button.clicked.connect(self.addSectionButtonClicked)
            else:
                add_button.clicked.connect(lambda: self.addButtonClicked(title))
            add_button_layout.addWidget(add_button)

            if title != "Sections":
                import_button = QPushButton("Import from CSV", self)
                import_button.clicked.connect(self.importButtonClicked)
                add_button_layout.addWidget(import_button)

            add_button_widget = QWidget()
            add_button_widget.setLayout(add_button_layout)
            layout.addWidget(add_button_widget)
        else:
            scenario_buttons_layout = QHBoxLayout()

            generate_button = QPushButton("Generate", self)
            generate_button.clicked.connect(self.generateButtonClicked)
            scenario_buttons_layout.addWidget(generate_button)

            view_result_button = QPushButton("View Result", self)
            view_result_button.clicked.connect(self.viewResultButtonClicked)
            scenario_buttons_layout.addWidget(view_result_button)

            scenario_buttons_widget = QWidget()
            scenario_buttons_widget.setLayout(scenario_buttons_layout)
            layout.addWidget(scenario_buttons_widget)

        tab.setLayout(layout)
        if title == "Subjects":
            table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def newFile(self):
        print("New File")

    def saveAs(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save As", "", "All Files (*);;Text Files (*.txt)")
        if filename:
            print("Saving as", filename)

    def settings(self):
        print("Settings")

    def instructions(self):
        print("Instructions")

    def about(self):
        print("About")

    def calculateNewWindowSize(self):
        main_window_size = self.size()
        new_window_width = main_window_size.width() * 0.8
        new_window_height = main_window_size.height() * 0.8
        return QtCore.QSize(new_window_width, new_window_height)

    def addInstructorButtonClicked(self):
        instructor_dialog = QDialog(self)
        instructor_dialog.setFixedSize(self.new_window_size)
        instructor_dialog.setWindowTitle("Instructor")
        
        layout = QVBoxLayout()
        form_layout = QFormLayout()
        self.lineEditName = QLineEdit()
        self.lineEditHours = QLineEdit()
        form_layout.addRow("Name", self.lineEditName)
        form_layout.addRow("Available Hours", self.lineEditHours)
        layout.addLayout(form_layout)

        self.availability_table = QTableWidget()
        self.availability_table.setColumnCount(5)  # Days of week
        self.availability_table.setRowCount(9)    # Hours
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        hour_labels = ["9:00", "9:50","10:40", "11:30", "12:30", "1:30", "2:20", "3:10", "4:00"]
        self.availability_table.setHorizontalHeaderLabels(days_of_week)
        self.availability_table.setVerticalHeaderLabels(hour_labels)

        for row in range(9):
            for col in range(6):
                item = QTableWidgetItem("Available")
                item.setBackground(QtGui.QColor(0, 255, 0))
                self.availability_table.setItem(row, col, item)

        self.availability_table.cellClicked.connect(lambda row, col: self.changeCellColor(row, col))
        layout.addWidget(self.availability_table)
        
        button_layout = QHBoxLayout()
        self.btnFinish = QPushButton("Finish")
        self.btnCancel = QPushButton("Cancel")
        self.btnCancel.clicked.connect(instructor_dialog.close)  # Connect cancel button to close window
        button_layout.addWidget(self.btnFinish)
        button_layout.addWidget(self.btnCancel)
        layout.addLayout(button_layout)
        
        instructor_dialog.setLayout(layout)
        instructor_dialog.exec_()

    def changeCellColor(self, row, col):
        current_item = self.availability_table.item(row, col)
        current_color = current_item.background().color()

        if current_color == QtGui.QColor(0, 255, 0):  # Check if the current color is the custom green color
            current_item.setBackground(QtGui.QColor("red"))
            current_item.setText("Unavailable")
        else:
            current_item.setBackground(QtGui.QColor(0, 255, 0))
            current_item.setText("Available")
        self.availability_table.clearSelection()

    def addRoomButtonClicked(self):
        room_dialog = QDialog(self)
        room_dialog.setFixedSize(self.new_window_size)
        room_dialog.setWindowTitle("Add Room")

        layout = QVBoxLayout()
        name_label = QLabel("Name:")
        self.room_name_lineEdit = QLineEdit()
        layout.addWidget(name_label)
        layout.addWidget(self.room_name_lineEdit)

        type_group = QGroupBox("Type")
        type_layout = QHBoxLayout()
        self.radio_lab = QRadioButton("Laboratory")
        self.radio_lec = QRadioButton("Lecture")
        type_layout.addWidget(self.radio_lab)
        type_layout.addWidget(self.radio_lec)
        type_group.setLayout(type_layout)
        layout.addWidget(type_group)

        self.availability_table = QTableWidget()
        self.availability_table.setColumnCount(6)  # Days of week
        self.availability_table.setRowCount(9)     # Hours
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        self.availability_table.setHorizontalHeaderLabels(days_of_week)
        hour_labels = ["9:00", "9:50", "10:40", "11:30", "12:30", "1:30", "2:20", "3:10", "4:00"]
        self.availability_table.setVerticalHeaderLabels(hour_labels)
        
        for row in range(9):
            for col in range(6):
                item = QTableWidgetItem("Available")
                item.setBackground(QtGui.QColor(0, 255, 0))
                self.availability_table.setItem(row, col, item)
        
        self.availability_table.cellClicked.connect(lambda row, col: self.changeCellColor(row, col))
        layout.addWidget(self.availability_table)

        button_layout = QHBoxLayout()
        finish_button = QPushButton("Finish")
        finish_button.clicked.connect(lambda: self.processRoomData(room_dialog, self.availability_table))
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(room_dialog.reject)
        button_layout.addWidget(finish_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)
        room_dialog.setLayout(layout)
        room_dialog.finished.connect(lambda result: self.cleanupRoomDialog())
        room_dialog.exec_()

    def cleanupRoomDialog(self):
        self.availability_table.cellClicked.disconnect()

    def addSubjectButtonClicked(self):
        subject_dialog = QDialog(self)
        subject_dialog.setFixedSize(self.new_window_size)
        subject_dialog.setWindowTitle("Subject")

        layout = QVBoxLayout()
        grid_layout = QGridLayout()
        self.lineEditName = QLineEdit()
        self.lineEditHours = QLineEdit()
        self.lineEditCode = QLineEdit()
        self.lineEditDescription = QLineEdit()

        grid_layout.addWidget(QLabel("Name:"), 0, 0)
        grid_layout.addWidget(self.lineEditName, 0, 1)
        grid_layout.addWidget(QLabel("Hours/Week:"), 0, 2)
        grid_layout.addWidget(self.lineEditHours, 0, 3)
        grid_layout.addWidget(QLabel("Code:"), 1, 0)
        grid_layout.addWidget(self.lineEditCode, 1, 1)
        grid_layout.addWidget(QLabel("Description:"), 1, 2)
        grid_layout.addWidget(self.lineEditDescription, 1, 3)
        layout.addLayout(grid_layout)

        group_type = QGroupBox("Type")
        group_type_layout = QHBoxLayout()
        self.radioLec = QRadioButton("Lecture")
        group_type_layout.addWidget(self.radioLec)
        self.radioLab = QRadioButton("Laboratory")
        group_type_layout.addWidget(self.radioLab)
        self.radioBoth = QRadioButton("Both")
        group_type_layout.addWidget(self.radioBoth)
        group_type.setLayout(group_type_layout)
        layout.addWidget(group_type)

        button_layout = QHBoxLayout()
        self.btnFinish = QPushButton("Finish")
        button_layout.addWidget(self.btnFinish)
        self.btnCancel = QPushButton("Cancel")
        button_layout.addWidget(self.btnCancel)
        self.btnCancel.clicked.connect(subject_dialog.close)
        layout.addLayout(button_layout)

        subject_dialog.setLayout(layout)
        subject_dialog.exec_()

    def importButtonClicked(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Import CSV", "", "CSV Files (*.csv)")
        if filename:
            try:
                with open(filename, 'r') as file:
                    csv_data = [] # Read the CSV data
                    for line in file:
                        csv_data.append(line.strip().split(','))

                # Get the current tab and table widget to add the CSV data
                current_tab_index = self.tabs.currentIndex()
                current_table = self.tabs.widget(current_tab_index).findChildren(QTableWidget)[0]
                current_table.setRowCount(0)

                for row_data in csv_data: # Add CSV data to the table
                    current_table.insertRow(current_table.rowCount())
                    for index, col_data in enumerate(row_data):
                        new_item = QTableWidgetItem(col_data)
                        current_table.setItem(current_table.rowCount() - 1, index, new_item)
            except Exception as e:
                print("Error during import operation:", e)

    def generateButtonClicked(self):
        print("Generate Button Clicked")

    def viewResultButtonClicked(self):
        print("View Result Button Clicked")

    def addSectionButtonClicked(self):
        section_dialog = QDialog(self)
        section_dialog.setFixedSize(self.new_window_size)
        section_dialog.setWindowTitle("Add Section")

        layout = QVBoxLayout()
        name_label = QLabel("Name:")
        self.section_name_lineEdit = QLineEdit()
        layout.addWidget(name_label)
        layout.addWidget(self.section_name_lineEdit)
        self.stay_in_room_checkbox = QCheckBox("Stay in Room")
        layout.addWidget(self.stay_in_room_checkbox)

        self.availability_table = QTableWidget()
        self.availability_table.setColumnCount(6)  # Days of week
        self.availability_table.setRowCount(9)     # Hours
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        self.availability_table.setHorizontalHeaderLabels(days_of_week)
        hour_labels = ["9:00", "9:50", "10:40", "11:30", "12:30", "1:30", "2:20", "3:10", "4:00"]
        self.availability_table.setVerticalHeaderLabels(hour_labels)

        for row in range(9):
            for col in range(6):
                item = QTableWidgetItem("Available")
                item.setBackground(QtGui.QColor(0, 255, 0))
                self.availability_table.setItem(row, col, item)
        
        self.availability_table.cellClicked.connect(lambda row, col: self.changeCellColor(row, col))
        layout.addWidget(self.availability_table)
        button_layout = QHBoxLayout()
        finish_button = QPushButton("Finish")
        finish_button.clicked.connect(lambda: self.processSectionData(section_dialog))
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(section_dialog.reject)
        button_layout.addWidget(finish_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)
        section_dialog.setLayout(layout)
        section_dialog.finished.connect(self.cleanupSectionDialog)
        section_dialog.exec_()

    def cleanupSectionDialog(self):
        self.availability_table.cellClicked.disconnect()

    def processSectionData(self, dialog):
        section_name = self.section_name_lineEdit.text()
        stay_in_room = self.stay_in_room_checkbox.isChecked()
        print("Section Name:", section_name)
        print("Stay in Room:", stay_in_room)
        dialog.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TimeTableGenerator()
    win.show()
    sys.exit(app.exec_())