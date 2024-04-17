from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QIcon
import warnings
import sys

warnings.filterwarnings("ignore", category=DeprecationWarning)

# To open Designer: qt5-tools designer
# To convert .ui file to .py file: pyuic5 -x filename.ui -o filename.py

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
hour_labels = ["9:00", "9:50", "10:40", "11:30", "12:30", "1:30", "2:20", "3:10", "4:00"]

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

    def calculateNewWindowSize(self):
        main_window_size = self.size()
        new_window_width = main_window_size.width() * 0.8
        new_window_height = main_window_size.height() * 0.8
        return QtCore.QSize(new_window_width, new_window_height)

    def createMenuBar(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")
        self.createMenuItem(file_menu, "New", self.newFile)
        self.createMenuItem(file_menu, "Save As", self.saveAs)
        self.createMenuItem(file_menu, "Exit", self.close)

        help_menu = menubar.addMenu("Help")
        self.createMenuItem(help_menu, "Instructions", self.instructions)
        self.createMenuItem(help_menu, "About", self.about)

    def createMenuItem(self, menu, title, function):
        action = QAction(title, self)
        action.triggered.connect(function)
        menu.addAction(action)

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

    def createWidgets(self):
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        tab_titles = ["Instructors", "Classes", "Labs", "Subjects", "Output Generator"]
        tab_columns = [["Name", "Hours", "Operation"], ["Name","Type", "Operation"], ["Name", "Operation"], ["Code", "Name","Class",  "Instructors", "Operation"], []]

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

        if title != "Output Generator":
            add_button_layout = QHBoxLayout()
            add_button = QPushButton(f"Add {title[:-1]}", self)
            if title == "Instructors":
                add_button.clicked.connect(self.addInstructorsButtonClicked)
            elif title == "Classes":
                add_button.clicked.connect(self.addClassesButtonClicked)
            elif title == "Labs":
                add_button.clicked.connect(self.addLabsButtonClicked)
            elif title == "Subjects":
                add_button.clicked.connect(self.addSubjectsButtonClicked)
            else:
                add_button.clicked.connect(lambda: self.addButtonClicked(title))
            add_button_layout.addWidget(add_button)

            if title != "Subjects":
                import_button = QPushButton("Import from CSV", self)
                add_button_layout.addWidget(import_button)
                import_button.clicked.connect(self.importButtonClicked)

            add_button_widget = QWidget()
            add_button_widget.setLayout(add_button_layout)
            layout.addWidget(add_button_widget)
        else:
            scenario_buttons_layout = QHBoxLayout()

            generate_button = QPushButton("Generate", self)
            scenario_buttons_layout.addWidget(generate_button)
            generate_button.clicked.connect(self.generateButtonClicked)

            scenario_buttons_widget = QWidget()
            scenario_buttons_widget.setLayout(scenario_buttons_layout)
            layout.addWidget(scenario_buttons_widget)

        tab.setLayout(layout)
        if title == "Subjects":
            table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def addInstructorsButtonClicked(self):
        add_dialog = QDialog(self)
        add_dialog.setFixedSize(self.new_window_size)
        add_dialog.setWindowTitle("Add Instructor")

        layout = QVBoxLayout()
        grid_layout = QGridLayout()
        self.lineEditName = QLineEdit()
        self.lineEditHours = QLineEdit()

        grid_layout.addWidget(QLabel("Name:"), 0, 0)
        grid_layout.addWidget(self.lineEditName, 0, 1)
        grid_layout.addWidget(QLabel("Hours:"), 1, 0)
        grid_layout.addWidget(self.lineEditHours, 1, 1)

        layout.addLayout(grid_layout)

        button_layout = QHBoxLayout()
        btnFinish = QPushButton("Finish")
        btnFinish.clicked.connect(lambda: self.ProcessData("Instructors"))
        button_layout.addWidget(btnFinish)
        btnCancel = QPushButton("Cancel")
        btnCancel.clicked.connect(add_dialog.close)
        button_layout.addWidget(btnCancel)
        layout.addLayout(button_layout)

        add_dialog.setLayout(layout)
        add_dialog.exec_()

    def addClassesButtonClicked(self):
        pass

    def addLabsButtonClicked(self):
        pass

    def addSubjectsButtonClicked(self):
        pass

    def importButtonClicked(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Import CSV", "", "CSV Files (*.csv)")
        if filename:
            try:
                with open(filename, 'r') as file:
                    csv_data = [] # Read the CSV data
                    for line in file:
                        csv_data.append(line.strip().split(','))

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

    def ProcessData(self, type):
        current_tab_index = self.tabs.currentIndex()
        current_tab_title = self.tabs.tabText(current_tab_index)
        current_table = self.tabs.widget(current_tab_index).findChild(QTableWidget)

        if current_tab_title == "Instructors":
            name = self.lineEditName.text()
            hours = self.lineEditHours.text()

            row_position = current_table.rowCount()
            current_table.insertRow(row_position)
            current_table.setItem(row_position, 0, QTableWidgetItem(name))
            current_table.setItem(row_position, 1, QTableWidgetItem(hours))

            edit_button = QPushButton("Edit")
            edit_button.clicked.connect(lambda: self.editEntry(current_table, row_position, current_tab_title))
            current_table.setCellWidget(row_position, 2, edit_button)

            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(lambda: self.deleteEntry(current_table, row_position, current_tab_title))
            current_table.setCellWidget(row_position, 3, delete_button)
        
        elif current_tab_title == "class":
            name = self.class_name_lineEdit.text()
            class_type = "Laboratory" if self.radio_lab.isChecked() else "Lecture"

            row_position = current_table.rowCount()
            current_table.insertRow(row_position)
            current_table.setItem(row_position, 0, QTableWidgetItem(name))
            current_table.setItem(row_position, 1, QTableWidgetItem(class_type))

            edit_button = QPushButton("Edit")
            edit_button.clicked.connect(lambda: self.editEntry(current_table, row_position, current_tab_title))
            current_table.setCellWidget(row_position, 2, edit_button)

            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(lambda: self.deleteEntry(current_table, row_position, current_tab_title))
            current_table.setCellWidget(row_position, 3, delete_button)
        
        elif current_tab_title == "Subjects":
            name = self.lineEditName.text()
            hours = self.lineEditHours.text()
            code = self.lineEditCode.text()
            description = self.lineEditDescription.text()
            subject_type = "Lecture" if self.radioLec.isChecked() else "Laboratory" if self.radioLab.isChecked() else "Both"

            row_position = current_table.rowCount()
            current_table.insertRow(row_position)
            current_table.setItem(row_position, 0, QTableWidgetItem(code))
            current_table.setItem(row_position, 1, QTableWidgetItem(name))
            current_table.setItem(row_position, 2, QTableWidgetItem(subject_type))
            current_table.setItem(row_position, 3, QTableWidgetItem(hours))

            edit_button = QPushButton("Edit")
            edit_button.clicked.connect(lambda: self.editEntry(current_table, row_position, current_tab_title))
            current_table.setCellWidget(row_position, 4, edit_button)

            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(lambda: self.deleteEntry(current_table, row_position, current_tab_title))
            current_table.setCellWidget(row_position, 5, delete_button)

        elif current_tab_title == "Subjects":
            name = self.section_name_lineEdit.text()
            stay_in_class = self.stay_in_class_checkbox.isChecked()

            row_position = current_table.rowCount()
            current_table.insertRow(row_position)
            current_table.setItem(row_position, 0, QTableWidgetItem("Available"))
            current_table.setItem(row_position, 1, QTableWidgetItem(name))
            current_table.setItem(row_position, 2, QTableWidgetItem("Yes" if stay_in_class else "No"))

            edit_button = QPushButton("Edit")
            edit_button.clicked.connect(lambda: self.editEntry(current_table, row_position, current_tab_title))
            current_table.setCellWidget(row_position, 3, edit_button)

            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(lambda: self.deleteEntry(current_table, row_position, current_tab_title))
            current_table.setCellWidget(row_position, 4, delete_button)
        else:
            print("Unknown type:", type)

        self.sender().parent().close() 

    def editEntry(self, table, row, tab_title):
        name_item = table.item(row, 1)
        if name_item is not None:
            name = name_item.text()
            edit_dialog = QDialog(self)
            edit_dialog.setFixedSize(self.new_window_size)
            edit_dialog.setWindowTitle(f"Edit {tab_title[:-1]}")

            layout = QVBoxLayout()
            grid_layout = QGridLayout()
            lineEdits = []

            column_names = [table.horizontalHeaderItem(col).text() for col in range(1, table.columnCount())]
            for col, column_name in enumerate(column_names):
                label = QLabel(column_name + ":")
                lineEdit = QLineEdit(table.item(row, col + 1).text())
                grid_layout.addWidget(label, col, 0)
                grid_layout.addWidget(lineEdit, col, 1)
                lineEdits.append(lineEdit)

            layout.addLayout(grid_layout)

            if tab_title == "Subjects":
                group_type = QGroupBox("Type")
                group_type_layout = QHBoxLayout()
                radioLec = QRadioButton("Lecture")
                radioLab = QRadioButton("Laboratory")
                radioBoth = QRadioButton("Both")

                subject_type = table.item(row, 2).text()
                if subject_type == "Lecture":
                    radioLec.setChecked(True)
                elif subject_type == "Laboratory":
                    radioLab.setChecked(True)
                else:
                    radioBoth.setChecked(True)

                group_type_layout.addWidget(radioLec)
                group_type_layout.addWidget(radioLab)
                group_type_layout.addWidget(radioBoth)
                group_type.setLayout(group_type_layout)
                layout.addWidget(group_type)

            button_layout = QHBoxLayout()
            btnFinish = QPushButton("Finish")
            if tab_title == "Subjects":
                btnFinish.clicked.connect(lambda: self.updateData(table, row, lineEdits, [radioLec.isChecked(), radioLab.isChecked(), radioBoth.isChecked()]))
            else:
                btnFinish.clicked.connect(lambda: self.updateData(table, row, lineEdits))
            button_layout.addWidget(btnFinish)
            btnCancel = QPushButton("Cancel")
            btnCancel.clicked.connect(edit_dialog.close)
            button_layout.addWidget(btnCancel)
            layout.addLayout(button_layout)

            edit_dialog.setLayout(layout)
            edit_dialog.exec_()

    def updateData(self, table, row, lineEdits, radio_states):
        for col, lineEdit in enumerate(lineEdits):
            table.setItem(row, col + 1, QTableWidgetItem(lineEdit.text()))
        subject_type = "Lecture" if radio_states[0] else "Laboratory" if radio_states[1] else "Both"
        table.setItem(row, 2, QTableWidgetItem(subject_type))
        self.sender().parent().close()

    def generateButtonClicked(self):
        print("Generate Button Clicked")

    def create_availability_table(self, days_of_week, hour_labels):
        availability_table = QTableWidget()
        availability_table.setColumnCount(len(days_of_week))
        availability_table.setRowCount(len(hour_labels))
        availability_table.setHorizontalHeaderLabels(days_of_week)
        availability_table.setVerticalHeaderLabels(hour_labels)

        for row in range(len(hour_labels)):
            for col in range(len(days_of_week)):
                item = QTableWidgetItem("Available")
                item.setBackground(QtGui.QColor(0, 255, 0))
                availability_table.setItem(row, col, item)
        availability_table.cellClicked.connect(lambda row, col: self.changeCellColor(row, col))
        return availability_table

    def changeCellColor(self, row, col):
        current_item = self.availability_table.item(row, col)
        current_color = current_item.background().color()

        if current_color == QtGui.QColor(0, 255, 0):
            current_item.setBackground(QtGui.QColor("red"))
            current_item.setText("Unavailable")
        else:
            current_item.setBackground(QtGui.QColor(0, 255, 0))
            current_item.setText("Available")
        self.availability_table.clearSelection()

    def cleanupSectionDialog(self):
        self.availability_table.cellClicked.disconnect()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TimeTableGenerator()
    win.show()
    sys.exit(app.exec_())