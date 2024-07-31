from View.Login import Ui_MainWindow
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QStackedWidget,
    QTableWidgetItem,
    QMessageBox,
)
import pandas as pd
from Database.db import Database

class LoginController(QMainWindow):
    def __init__(self, router : QStackedWidget):
        super(LoginController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.router = router

        self.db = Database()

        self.ui.loginButton.clicked.connect(self.login)
        self.ui.registerButton.clicked.connect(self.go_register)

        # print("Is self.router initialized?", self.router is not None)
        # print("Index of login page:", self.router.indexOf(self.ui.loginPageWidget))

    def clear_input(self):
        self.ui.usernameInput.setText("")
        self.ui.passwordInput.setText("")

    def login(self):
        # Get the input values from the login form  
        username = self.ui.usernameInput.text()
        password = self.ui.passwordInput.text()

        # Create QMessageBox instance for showing messages
        message_box = QMessageBox()

        # Validate if input fields are empty
        if not username or not password:
            message_box.setIcon(QMessageBox.Warning)
            message_box.setText("Please enter both username and password.")
            message_box.exec_()
            return

        # Check if the input data matches the data in the CSV file
        user_data = self.db.find_user(username, password)

        if user_data:
            # Login successful
            message_box.setIcon(QMessageBox.Information)
            message_box.setText("Login successful!")
            message_box.exec_()

            # initialize the input field to empty
            self.clear_input()

            # Perform any additional actions after successful login
            print("2")
            self.router.setCurrentIndex(2)
        else:
            # Login failed
            message_box.setIcon(QMessageBox.Warning)
            message_box.setText("Invalid username or password.")
            message_box.exec_()
    
    def go_register(self):
        self.clear_input()
        self.router.setCurrentIndex(1)
