from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import warnings

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

        self.createTab("Instructors", ["Available", "Name", "Hours", "Operation"])
        self.createTab("Rooms", ["Available", "Name", "Operation"])
        self.createTab("Subjects", ["Code", "Name", "Type", "Instructors", "Operation"])
        self.createTab("Sections", ["Available", "Name", "Stay in Room", "Operation"])
        self.createTab("Scenario Manager", [])  # No columns for Scenario Manager

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
            elif title == "Subjects":
                add_button.clicked.connect(self.addSubjectButtonClicked)
            else:
                add_button.clicked.connect(lambda: self.addButtonClicked(title))
            add_button_layout.addWidget(add_button)

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

    def addButtonClicked(self, title):
        self.new_window = QMainWindow()
        self.new_window.setWindowTitle(title)
        self.new_window.setFixedSize(self.new_window_size)
        print(f"Add {title} Clicked")

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
        
        self.tableSchedule = QTableView()
        layout.addWidget(self.tableSchedule)
        
        button_layout = QHBoxLayout()
        self.btnFinish = QPushButton("Finish")
        self.btnCancel = QPushButton("Cancel")
        self.btnCancel.clicked.connect(instructor_dialog.close)  # Connect cancel button to close window
        button_layout.addWidget(self.btnFinish)
        button_layout.addWidget(self.btnCancel)
        layout.addLayout(button_layout)
        
        instructor_dialog.setLayout(layout)
        instructor_dialog.exec_()

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TimeTableGenerator()
    win.show()
    sys.exit(app.exec_())