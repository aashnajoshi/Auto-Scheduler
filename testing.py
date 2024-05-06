import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QTableWidget, QTableWidgetItem
from generator import *
data={
        'Teachers': [{'Name': 'teacher1'}, {'Name': 'teacher2'}, {'Name': 'teacher3'}, {'Name': 'teacher4'}, {'Name': 'teacher5'}],
        'Classes': [{'Name': 'aiml', 'Subjects': 'sub1,sub2,sub3,sub4', 'Lab Subjects': 'lab_sub3,lab_sub2'}, {'Name': 'cse', 'Subjects': 'sub1,sub2,sub4,sub5', 'Lab Subjects': 'lab_sub2,lab_sub5'}, {'Name': 'ece', 'Subjects': 'sub1,sub5,sub6', 'Lab Subjects': 'lab_sub1'}], 
        'Labs': [{'Name': 'lab1'}, {'Name': 'lab2'}, {'Name': 'lab3'}, {'Name': 'lab4'}],
        'Relations': [{'Subject': 'sub1', 'Class': 'aiml', 'Name': 'teacher1', 'Lectures': '3'}, {'Subject': 'sub1', 'Class': 'cse', 'Name': 'teacher1', 'Lectures': '3'}, {'Subject': 'sub5', 'Class': 'ece', 'Name': 'teacher1', 'Lectures': '3'}, {'Subject': 'sub2', 'Class': 'aiml', 'Name': 'teacher2', 'Lectures': '3'}, {'Subject': 'sub2', 'Class': 'cse', 'Name': 'teacher2', 'Lectures': '2'}, {'Subject': 'sub1', 'Class': 'ece', 'Name': 'teacher2', 'Lectures': '3'}, {'Subject': 'lab_sub2', 'Class': 'aiml', 'Name': 'teacher2', 'Lectures': '1'}, {'Subject': 'lab_sub2', 'Class': 'cse', 'Name': 'teacher2', 'Lectures': '1'}, {'Subject': 'sub3', 'Class': 'aiml', 'Name': 'teacher3', 'Lectures': '2'}, {'Subject': 'lab_sub3', 'Class': 'aiml', 'Name': 'teacher3', 'Lectures': '1'}, {'Subject': 'lab_sub1', 'Class': 'ece', 'Name': 'teacher3', 'Lectures': '1'}, {'Subject': 'sub4', 'Class': 'aiml', 'Name': 'teacher4', 'Lectures': '4'}, {'Subject': 'sub4', 'Class': 'cse', 'Name': 'teacher4', 'Lectures': '2'}, {'Subject': 'sub5', 'Class': 'cse', 'Name': 'teacher5', 'Lectures': '4'}, {'Subject': 'sub6', 'Class': 'ece', 'Name': 'teacher5', 'Lectures': '3'}, {'Subject': 'lab_sub5', 'Class': 'cse', 'Name': 'teacher5', 'Lectures': '1'},]}

            
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Divided Layout Example")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # QPlainTextEdit
        text_edit = QPlainTextEdit()
        layout.addWidget(text_edit)
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        hour_labels = ["9:00", "9:50", "10:40", "11:30", "12:30", "1:30", "2:20", "3:10", "4:00"]

        # QTableWidget 1
        for cls in classes.keys():
            table_widget1 = QTableWidget()
            table_widget1.setRowCount(5)
            table_widget1.setColumnCount(7)
            table_widget1.setVerticalHeaderLabels(days_of_week)
            table_widget1.setHorizontalHeaderLabels(hour_labels)
            layout.addWidget(table_widget1)
            for r in range(5):
                for c in range(7):
                    cell=QTableWidgetItem(str(ctt[cls][r][c]))
                    table_widget1.setItem(r,c,cell)
        # for teacher in teachers.keys():
        #     table_widget1 = QTableWidget()
        #     table_widget1.setRowCount(5)
        #     table_widget1.setColumnCount(7)
        #     table_widget1.setVerticalHeaderLabels(days_of_week)
        #     table_widget1.setHorizontalHeaderLabels(hour_labels)
        #     layout.addWidget(table_widget1)
        #     for r in range(5):
        #         for c in range(7):
        #             cell=QTableWidgetItem(str(ttt[teacher][r][c]))
        #             table_widget1.setItem(r,c,cell)
if __name__ == "__main__":
    initialize(data)
    T_T_G(classes.keys())
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())