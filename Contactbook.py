import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox

class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set Window Title
        self.setWindowTitle('Main Form')
        # Set Dimensions
        self.setGeometry(100, 100, 400, 300)
        # Set Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        # Set Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # ID Label & Input
        self.name_label = QLabel('Name:')
        self.name_input = QLineEdit()
        self.phone_label = QLabel('Phone Number:')
        self.phone_input = QLineEdit()
        self.email_label = QLabel('Email:')
        self.email_input = QLineEdit()
        self.address_label = QLabel('Address:')
        self.address_input = QLineEdit()
        self.add_button = QPushButton('Add Contact')
        self.view_button = QPushButton('View Contacts')
        self.update_button = QPushButton('Update Contact')
        self.delete_button = QPushButton('Delete Contact')
        self.search_button = QPushButton('Search Contact')
        
        # Add Widgets to Layout
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.view_button)
        layout.addWidget(self.update_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.search_button)
        
        # Connect Buttons to Event Handling Code
        self.add_button.clicked.connect(self.add_contact)
        self.view_button.clicked.connect(self.open_view_form)
        self.update_button.clicked.connect(self.update_contact)
        self.delete_button.clicked.connect(self.delete_contact)
        self.search_button.clicked.connect(self.search_contact)

        # Initialize contacts list
        self.contacts = []

    def add_contact(self):
        name = self.name_input.text()
        number = self.phone_input.text()
        email = self.email_input.text()
        address = self.address_input.text()
        
        if name != "" and number != "" and email != "" and address != "":
            if not name.isalpha():
                self.name_error = NameError()
                self.name_error.show()
            elif len(number) != 11 or not number.isdigit():
                self.number_error = NumberError()
                self.number_error.show()
            elif '@' not in email or '.com' not in email:
                self.email_error = EmailError()
                self.email_error.show()
            else:
                self.contacts.append([name, number, email, address])
                self.default_form = Defaultform(self.contacts)
                self.default_form.show()
        else:
            self.empty_error = EmptyError()
            self.empty_error.show()
        
        # Clear the input fields after adding contact
        self.name_input.clear()
        self.phone_input.clear()
        self.email_input.clear()
        self.address_input.clear()

    def open_view_form(self):
        self.view_form = ViewForm(self.contacts)
        self.view_form.show()

    def search_contact(self):
        search_name = self.name_input.text()
        if search_name:
            for contact in self.contacts:
                if contact[0] == search_name:
                    # self.phone_input.setText(contact[1])
                    # self.email_input.setText(contact[2])
                    # self.address_input.setText(contact[3])
                    
                    # Show the contact in the table
                    self.view_form = ViewForm([contact])
                    self.view_form.show()
                    return
        else:
            self.empty_error = EmptyError()
            self.empty_error.show()

    def update_contact(self):
        search_name = self.name_input.text()
        if search_name:
            for contact in self.contacts:
                if contact[0] == search_name:
                    contact[1] = self.phone_input.text()
                    contact[2] = self.email_input.text()
                    contact[3] = self.address_input.text()
                    
        else:
            self.empty_error = EmptyError()
            self.empty_error.show()

    def delete_contact(self):
        search_name = self.name_input.text()
        if search_name:
            for contact in self.contacts:
                if contact[0] == search_name:
                    self.contacts.remove(contact)
                    print("done")
        else:
            self.empty_error = EmptyError()
            self.empty_error.show()

class ViewForm(QMainWindow):
    def __init__(self, contacts):
        super().__init__()
        self.setWindowTitle('View Contacts')
        self.setGeometry(100, 100, 600, 400)
        self.contacts = contacts  # Set contacts attribute
        
        # Set central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create table widget
        self.table = QTableWidget()
        self.table.setRowCount(len(contacts))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Name", "Phone Number", "Email Address", "Address"])

        # Add contacts to the table
        row_num = 0
        for contact in contacts:
            self.table.setItem(row_num, 0, QTableWidgetItem(contact[0]))
            self.table.setItem(row_num, 1, QTableWidgetItem(contact[1]))
            self.table.setItem(row_num, 2, QTableWidgetItem(contact[2]))
            self.table.setItem(row_num, 3, QTableWidgetItem(contact[3]))
            row_num += 1

        layout.addWidget(self.table)


class Defaultform(QMainWindow):
    def __init__(self, contacts):
        super().__init__()
        self.setWindowTitle('Add Contacts')
        self.setGeometry(100, 100, 300, 200)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.message = QLabel('This contact has successfully been added to your contact book.')
        layout.addWidget(self.message)


class NameError(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Error message')
        self.setGeometry(100, 100, 300, 200)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.message = QLabel('Name cannot contain numbers or special characters.')
        layout.addWidget(self.message)


class NumberError(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Error message')
        self.setGeometry(100, 100, 300, 200)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.message = QLabel('Phone number should be 11 digits and contain only numbers.')
        layout.addWidget(self.message)


class EmailError(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Error message')
        self.setGeometry(100, 100, 300, 200)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.message = QLabel('Invalid email address.')
        layout.addWidget(self.message)


class EmptyError(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Error message')
        self.setGeometry(100, 100, 300, 200)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.message = QLabel('Contact was not added due to one or more missing fields.')
        layout.addWidget(self.message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec())
