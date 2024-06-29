
from PyQt6 import QtWidgets, QtCore, uic
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
import sys

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(UI, self).__init__()
        # Load the .ui file
        uic.loadUi('Todolist.ui', self)
        self.setGeometry(100, 100, 400, 400)
        self.add.clicked.connect(self.add_task)
        self.delete_2.clicked.connect(self.delete_task)
        self.create.clicked.connect(self.create_list)
        self.update.clicked.connect(self.update_list)
    def add_task(self):
        # to type item in LineEdit
        item = self.lineEdit.text()
        # item added in list widget
        self.listWidget.addItem(item)
        # clear item from lineEdit
        self.lineEdit.setText("")

    def create_list(self):
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            item.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            item.setCheckState(Qt.CheckState.Unchecked)

    def delete_task(self):
        current=self.listWidget.currentRow()
        self.listWidget.takeItem(current)
    def update_list(self):
        self.listWidget.clear() 

app = QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
Todolist = UI()  # Create an instance of our UI class
Todolist.show()
app.exec()  # Start the application
