import sys
from PyQt5.QtCore import Qt
from UI.Login import *
from UI.register import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from Controller import (
    loginController,
    registerController,
)
from app_data import AppData
from enums import Pages

def add_pages(router):
    data = AppData()
    data.router = router

    login_page = loginController.LoginController(router)
    router.addWidget(login_page)
    data.login_page = login_page

    register_page = registerController.RegisterController(router)
    router.addWidget(register_page)
    data.register_page = register_page



if __name__ == "__main__":
    app = QApplication(sys.argv)
    router = QtWidgets.QStackedWidget()
    add_pages(router)
    router.setGeometry(100, 100, 996, 700)
    router.setCurrentIndex(Pages.LOGIN.value)
    router.show()
    sys.exit(app.exec_())