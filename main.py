import os
import sys

from PyQt5.QtCore import Qt
from UI.Login import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from app_data import AppData
from enums import Pages
from Controller import (
    loginController,
)

def add_pages(router):
    data = AppData
    data.router = router

    loginPage = loginController.LoginController(router)
    router.addWidget(loginPage)
    data.loginPage = loginPage

if __name__ == "__main__":
    app = QApplication(sys.argv)
    router = QtWidgets.QStackedWidget()
    add_pages(router)
    router.setGeometry(100, 100, 996, 700)
    router.setCurrentIndex(Pages.LOGIN.value)
    router.show()
    sys.exit(app.exec_())