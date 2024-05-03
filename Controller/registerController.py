from UI.register import Ui_registerForm
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QStackedWidget,
    QTableWidgetItem,
    QMessageBox,
)
from PyQt5.QtCore import Qt
from app_data import AppData
from enums import Pages
import pandas as pd
from Controller.loginController import userDAO

class RegisterController(QWidget):
    def __init__(self, router):
        self.ui = Ui_registerForm()
        super().__init__(parent=None)
        self.ui.setupUi(self)

        self.userDao = userDAO()
        self.data = self.userDao.get_data()

        self.ui.regButton.clicked.connect(self.submit)

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
        if username in self.data["Username"].values:
            message_box.setIcon(QMessageBox.Warning)
            message_box.setText("Username already exists. Please choose another username.")
            message_box.exec_()
            return

        # if no error prompt, prompt register success message box and write the username and password into the csv file
        new_user = pd.DataFrame({"Username": [username], "Password": [password]})
        self.data = pd.concat([self.data, new_user], ignore_index=True)
        self.data.to_csv(self.userDao.csv_path, index=False)

        message_box.setIcon(QMessageBox.Information)
        message_box.setText("Registration successful!")
        message_box.exec_()

        self.router.navigate(Pages.LOGIN)