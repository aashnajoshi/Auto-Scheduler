from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QAction, QMenuBar, QFileDialog, QTabWidget, QVBoxLayout, QWidget, QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox
from PyQt5.QtGui import QIcon
import sys
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

class TimeTableGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

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
        main_window_size = self.size()
        new_window_width = main_window_size.width() * 0.8
        new_window_height = main_window_size.height() * 0.8

        self.new_window = QMainWindow()
        self.new_window.setWindowTitle(title)
        self.new_window.setGeometry(self.geometry().center().x() - new_window_width / 2, self.geometry().center().y() - new_window_height / 2, new_window_width, new_window_height)
        self.new_window.show()

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