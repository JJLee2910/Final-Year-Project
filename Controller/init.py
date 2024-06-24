from View.register import Reg_Ui_MainWindow
from View.Login import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow

class init:
    def __init__(self):
        self.login_window = QMainWindow()
        self.reg_window = QMainWindow()

        self.login_ui = Ui_MainWindow()
        self.login_ui.setupUi(self.login_window)

        self.reg_ui = Reg_Ui_MainWindow()
        self.reg_ui.setupUi(self.reg_window)

    def clear_login_field(self):
        self.login_ui.usernameInput.setText("")
        self.login_ui.passwordInput.setText("")


    def clear_reg_field(self):
        self.reg_ui.usernameRegInput.setText("")
        self.reg_ui.passwordRegInput.setText("")
        self.reg_ui.passwordRegInput_2.setText("")