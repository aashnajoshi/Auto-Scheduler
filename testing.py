import sys
from PyQt5.QtWidgets import *
from generator import *

data = {
    'Teachers': [{'Name': 'teacher1'}, {'Name': 'teacher2'}, {'Name': 'teacher3'}, {'Name': 'teacher4'}, {'Name': 'teacher5'}],
    'Classes': [{'Name': 'aiml', 'Subjects': 'sub1,sub2,sub3,sub4', 'Lab Subjects': 'lab_sub3,lab_sub2'}, {'Name': 'cse', 'Subjects': 'sub1,sub2,sub4,sub5', 'Lab Subjects': 'lab_sub2,lab_sub5'}, {'Name': 'ece', 'Subjects': 'sub1,sub5,sub6', 'Lab Subjects': 'lab_sub1'}],
    'Labs': [{'Name': 'lab1'}, {'Name': 'lab2'}, {'Name': 'lab3'}, {'Name': 'lab4'}],
    'Relations': [{'Subject': 'sub1', 'Class': 'aiml', 'Name': 'teacher1', 'Lectures': '3'}, {'Subject': 'sub1', 'Class': 'cse', 'Name': 'teacher1', 'Lectures': '3'}, {'Subject': 'sub5', 'Class': 'ece', 'Name': 'teacher1', 'Lectures': '3'}, {'Subject': 'sub2', 'Class': 'aiml', 'Name': 'teacher2', 'Lectures': '3'}, {'Subject': 'sub2', 'Class': 'cse', 'Name': 'teacher2', 'Lectures': '2'}, {'Subject': 'sub1', 'Class': 'ece', 'Name': 'teacher2', 'Lectures': '3'}, {'Subject': 'lab_sub2', 'Class': 'aiml', 'Name': 'teacher2', 'Lectures': '1'}, {'Subject': 'lab_sub2', 'Class': 'cse', 'Name': 'teacher2', 'Lectures': '1'}, {'Subject': 'sub3', 'Class': 'aiml', 'Name': 'teacher3', 'Lectures': '2'}, {'Subject': 'lab_sub3', 'Class': 'aiml', 'Name': 'teacher3', 'Lectures': '1'}, {'Subject': 'lab_sub1', 'Class': 'ece', 'Name': 'teacher3', 'Lectures': '1'}, {'Subject': 'sub4', 'Class': 'aiml', 'Name': 'teacher4', 'Lectures': '4'}, {'Subject': 'sub4', 'Class': 'cse', 'Name': 'teacher4', 'Lectures': '2'}, {'Subject': 'sub5', 'Class': 'cse', 'Name': 'teacher5', 'Lectures': '4'}, {'Subject': 'sub6', 'Class': 'ece', 'Name': 'teacher5', 'Lectures': '3'}, {'Subject': 'lab_sub5', 'Class': 'cse', 'Name': 'teacher5', 'Lectures': '1'}, ]}

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Timetable Viewer")
        self.setGeometry(100, 100, 800, 600)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)

        # Dropdown for selecting class & teacher's timetable
        self.class_dropdown = QComboBox()
        self.class_dropdown.addItem("Select Class Timetable")
        for cls in classes.keys():
            self.class_dropdown.addItem(f"Class Timetable ({cls})")

        self.class_dropdown.currentIndexChanged.connect(self.show_class_timetable)
        self.class_dropdown.hide()  # Initially hide
        grid_layout.addWidget(self.class_dropdown, 0, 0)

        self.teacher_dropdown = QComboBox()
        self.teacher_dropdown.addItem("Select Teacher's Timetable")
        for teacher in teachers.keys():
            self.teacher_dropdown.addItem(f"Teacher's Timetable ({teacher})")

        self.teacher_dropdown.currentIndexChanged.connect(self.show_teacher_timetable)
        self.teacher_dropdown.hide()  # Initially hide
        grid_layout.addWidget(self.teacher_dropdown, 0, 1)

        self.timetable_label = QLabel("")
        layout.addWidget(self.timetable_label)
        self.timetable_label.hide()
        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

        self.generate_button = QPushButton("Generate") # Generate button
        self.generate_button.clicked.connect(self.show_dropdowns)
        layout.addWidget(self.generate_button)

    def show_class_timetable(self, index):
        if index != 0:
            cls = list(classes.keys())[index - 1]
            self.timetable_label.setText(f"Class Timetable ({cls})")
            self.timetable_label.show()
            self.populate_table(ctt[cls])
            self.class_dropdown.setCurrentIndex(0)  # Reset dropdown

    def show_teacher_timetable(self, index):
        if index != 0:
            teacher = list(teachers.keys())[index - 1]
            self.timetable_label.setText(f"Teacher's Timetable ({teacher})")
            self.timetable_label.show()
            self.populate_table(ttt[teacher])
            self.teacher_dropdown.setCurrentIndex(0)  # Reset dropdown

    def populate_table(self, data):
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        hour_labels = ["9:00", "9:50", "10:40", "11:30", "12:30", "1:30", "2:20", "3:10", "4:00"]

        self.table_widget.clear()
        self.table_widget.setRowCount(5)
        self.table_widget.setColumnCount(7)
        self.table_widget.setVerticalHeaderLabels(days_of_week)
        self.table_widget.setHorizontalHeaderLabels(hour_labels)

        for r, row in enumerate(data):
            for c, cell in enumerate(row):
                item = QTableWidgetItem(str(cell))
                self.table_widget.setItem(r, c, item)

    def show_dropdowns(self):
        self.class_dropdown.show()
        self.teacher_dropdown.show()

if __name__ == "__main__":
    initialize(data)
    T_T_G(classes.keys())
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())