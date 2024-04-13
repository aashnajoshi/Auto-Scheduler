import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QAction, QMenuBar, QFileDialog, QTabWidget, QVBoxLayout, QWidget, QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import QIcon
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
            add_button.clicked.connect(self.addButtonClicked)
            add_button_layout.addWidget(add_button)

            import_button = QPushButton("Import from CSV", self)
            import_button.clicked.connect(self.importButtonClicked)
            add_button_layout.addWidget(import_button)

            add_button_widget = QWidget()
            add_button_widget.setLayout(add_button_layout)
            layout.addWidget(add_button_widget)

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

    def addButtonClicked(self):
        current_tab_title = self.tabs.tabText(self.tabs.currentIndex())
        print(f"Add {current_tab_title[:-1]} Button Clicked")

    def importButtonClicked(self):
        print("Import Button Clicked")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TimeTableGenerator()
    window.show()
    sys.exit(app.exec_())