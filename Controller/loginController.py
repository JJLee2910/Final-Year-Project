from UI.Login import *
from UI.register import *
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QStackedWidget,
    QTableWidgetItem,
    QMessageBox,
)
from PyQt5.QtCore import QObject, pyqtSignal
from app_data import AppData
from enums import Pages
import pandas as pd

class userDAO:
    def __init__(self,csv_path='Database\\user.csv'):
        self.csv_path = csv_path
    
    def get_data(self):
        return pd.read_csv(self.csv_path)

class LoginController(QWidget):
    def __init__(self, router):
        self.ui = Ui_loginForm()
        super().__init__(parent=None)
        self.ui.setupUi(self)

        self.userDao = userDAO()
        self.data = self.userDao.get_data()

        self.ui.loginButton.clicked.connect(self.login)
        self.ui.registerButton.clicked.connect(self.go_register)

        self.reg_Ui = Ui_registerForm()
        self.regPage = QWidget()

    def login(self):
        # Get the input values from the login form  
        username = self.ui.usernameInput.text()
        password = self.ui.passwordInput.text()

        # Create QMessageBox instance for showing messages
        message_box = QtWidgets.QMessageBox()

        # Validate if input fields are empty
        if not username or not password:
            message_box.setIcon(QtWidgets.QMessageBox.Warning)
            message_box.setText("Please enter both username and password.")
            message_box.exec_()
            return

        # Check if the input data matches the data in the CSV file
        user_data = self.data.loc[
            (self.data["Username"] == username)
            & (self.data["Password"] == password)
        ]

        if not user_data.empty:
            # Login successful
            message_box.setIcon(QtWidgets.QMessageBox.Information)
            message_box.setText("Login successful!")
            message_box.exec_()
            # Perform any additional actions after successful login
            # For example, navigate to the main window or perform other operations
            # self.router.navigate(Pages.MAIN_WINDOW)
        else:
            # Login failed
            message_box.setIcon(QtWidgets.QMessageBox.Warning)
            message_box.setText("Invalid username or password.")
            message_box.exec_()
    
    def go_register(self):
        self.reg_Ui.setupUi(self.regPage)
        print("1")
