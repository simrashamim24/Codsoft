
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox

class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set Window Title
        self.setWindowTitle('Arithmetic Calculator')
        # Set Dimensions
        self.setGeometry(100, 100, 400, 300)
        # Set Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        # Set Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.num1_label = QLabel('Number_1:')
        self.num1 = QLineEdit()
        self.num2_label = QLabel('Number_2:')
        self.num2 = QLineEdit()
        self.add_button = QPushButton('Addition')
        self.subtract_button = QPushButton('Subtraction')
        self.multiply_button = QPushButton('Multiplication')
        self.divide_button = QPushButton('Division')
        self.clear_button=QPushButton('Clear')
        self.label=QLabel('Result:')

        layout.addWidget(self.num1_label)
        layout.addWidget(self.num1)
        layout.addWidget(self.num2_label)
        layout.addWidget(self.num2)
        layout.addWidget(self.add_button)
        layout.addWidget(self.subtract_button)
        layout.addWidget(self.multiply_button)
        layout.addWidget(self.divide_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.label)

        self.add_button.clicked.connect(self.add_func)
        self.subtract_button.clicked.connect(self.subtract_func)
        self.multiply_button.clicked.connect(self.multiply_func)
        self.divide_button.clicked.connect(self.divide_func)
        self.clear_button.clicked.connect(self.clear_func)
        self.set_styles()

    def set_styles(self):

        self.setStyleSheet("background-color: #3b3b3b;")

        label_style = "color: #f2f2f2; font-size: 14px;"
        self.num1_label.setStyleSheet(label_style)
        self.num2_label.setStyleSheet(label_style)
        self.label.setStyleSheet(label_style)

        line_edit_style = "background-color: #f2f2f2; color: #000000; font-size: 14px;"
        self.num1.setStyleSheet(line_edit_style)
        self.num2.setStyleSheet(line_edit_style)
        button_style = """
            QPushButton {
                background-color: #8b4513; 
                color: #ffffff; 
                font-size: 14px;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #a0522d;
            }
            QPushButton:pressed {
                background-color: #5f3d26;
            }
        """
        self.add_button.setStyleSheet(button_style)
        self.subtract_button.setStyleSheet(button_style)
        self.multiply_button.setStyleSheet(button_style)
        self.divide_button.setStyleSheet(button_style)
        self.clear_button.setStyleSheet(button_style)

    def add_func(self):

        self.label.setText("Addition : {}".format(int(self.num1.text())+int(self.num2.text())))
        # print(int(self.num1.text())+int(self.num2.text()))
    def subtract_func(self):
        # print(int(self.num1.text())-int(self.num2.text()))
        self.label.setText("Subtraction : {}".format(int(self.num1.text())-int(self.num2.text())))
    def multiply_func(self):
        self.label.setText("Multiplication : {}".format(int(self.num1.text())*int(self.num2.text())))
        # print(int(self.num1.text())*int(self.num2.text()))
    def divide_func(self):
        self.label.setText("Division : {}".format(int(self.num1.text())/int(self.num2.text())))
        # print(int(self.num1.text())/int(self.num2.text()))
        # print(self.num2.text())
        # print(int(self.num1.text())+int(self.num1.text()))
    def clear_func(self):
        self.num1.clear()
        self.num2.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec())