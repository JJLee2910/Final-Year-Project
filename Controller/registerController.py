from View.register import Ui_MainWindow
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QStackedWidget,
    QTableWidgetItem,
    QMessageBox,
)
from PyQt5.QtCore import Qt
import pandas as pd
from Database.db import Database

class RegisterController(QMainWindow):
    def __init__(self, router : QStackedWidget):
        super(RegisterController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.router = router

        self.db = Database()

        self.ui.regButton.clicked.connect(self.submit)
        self.ui.backButton.clicked.connect(self.toLogin)

    def clear_input(self):
        self.ui.usernameRegInput.setText("")
        self.ui.passwordRegInput.setText("")
        self.ui.passwordRegInput_2.setText("")

    def submit(self):
        # initialize input values from the form
        username = self.ui.usernameRegInput.text()
        password = self.ui.passwordRegInput.text()
        password2 = self.ui.passwordRegInput_2.text()

        message_box = QMessageBox()

        # validate if all 3 input fields are empty, if empty prompt error message box
        if not username or not password or not password2:
            message_box.setIcon(QMessageBox.Warning)
            message_box.setText("Please fill in all the fields.")
            message_box.exec_()
            return

        # validate if password 1 == password2, if not same prompt error message box
        if password != password2:
            message_box.setIcon(QMessageBox.Warning)
            message_box.setText("Passwords do not match. Please re-enter your password.")
            message_box.exec_()
            return
        # check username exist in csv file, if exist prompt error
        if self.db.find_unique_user(username):
            message_box.setIcon(QMessageBox.Warning)
            message_box.setText("Username already exists. Please choose another username.")
            message_box.exec_()
            return

        # if no error prompt, prompt register success message box and write the username and password into the csv file
        self.db.insert_user(username, password)

        message_box.setIcon(QMessageBox.Information)
        message_box.setText("Registration successful!")
        message_box.exec_()

        self.clear_input()

        self.router.setCurrentIndex(0)

    def toLogin(self):
        self.clear_input()
        self.router.setCurrentIndex(0)