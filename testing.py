import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QTableWidget, QTableWidgetItem


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

        # Days of week and hour labels
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        hour_labels = ["9:00", "9:50", "10:40", "11:30", "12:30", "1:30", "2:20", "3:10", "4:00"]

        # QTableWidget 1
        table_widget1 = QTableWidget()
        table_widget1.setRowCount(len(days_of_week))
        table_widget1.setColumnCount(len(hour_labels))
        table_widget1.setVerticalHeaderLabels(days_of_week)
        table_widget1.setHorizontalHeaderLabels(hour_labels)
        layout.addWidget(table_widget1)

        # QTableWidget 2
        table_widget2 = QTableWidget()
        table_widget2.setRowCount(len(days_of_week))
        table_widget2.setColumnCount(len(hour_labels))
        table_widget2.setVerticalHeaderLabels(days_of_week)
        table_widget2.setHorizontalHeaderLabels(hour_labels)
        layout.addWidget(table_widget2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())