import sys
from PyQt5.QtCore import Qt
from UI.Login import *
from UI.register import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from Controller import (
    loginController,
    registerController,
    dashboardController,
)
from app_data import AppData
def add_pages(router):
    # data = AppData
    # data.router = router

    login_page = loginController.LoginController(router)
    router.addWidget(login_page)
    # data.login_page = login_page

    register_page = registerController.RegisterController(router)
    router.addWidget(register_page)
    # data.register_page = register_page

    dashboard_page = dashboardController.DashboardController(router)
    router.addWidget(dashboard_page)
    # data.dashboard_page = dashboard_page

if __name__ == "__main__":
    app = QApplication(sys.argv)
    router = QtWidgets.QStackedWidget()
    add_pages(router)
    router.setGeometry(100, 100, 800, 650)
    router.setCurrentIndex(0)
    router.show()
    sys.exit(app.exec_())