import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Account Registration")
        self.setGeometry(500, 200, 350, 350)
        self.setWindowIcon(QIcon('pythonico.ico'))
        self.setStyleSheet("background-color: #0db9db;")

        labels = ["First Name:", "Last Name:", "Username:", "Password:", "Email:", "Contact Number:"]
        self.txtFields = []
        y = 40

        for lblText in labels:
            label = QLabel(lblText, self)
            label.move(50, y)
            label.setFont(QFont('Arial', 10))

            txtField = QLineEdit(self)
            txtField.move(180, y)
            txtField.setStyleSheet("border: 1px solid black;")
            txtField.setStyleSheet("background-color: white;")
            self.txtFields.append(txtField)

            y += 40

        self.submitBtn = QPushButton("Submit", self)
        self.submitBtn.move(75, y)
        self.submitBtn.clicked.connect(self.submit)
        self.submitBtn.setStyleSheet("background-color : #04cf7f")

        self.clrBtn = QPushButton("Clear", self)
        self.clrBtn.move(185, y)
        self.clrBtn.clicked.connect(self.clrFields)
        self.clrBtn.setStyleSheet("background-color: #ff4956")

        self.show()

    def submit(self):
        print("Form Submitted!")

    def clrFields(self):
        for field in self.txtFields:
            field.clear()
