from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QStackedWidget,
    QTableWidgetItem,
)
from PyQt5.QtCore import Qt
from app_data import AppData
from enums import Pages

class MyMainWindow(QMainWindow):
    def __init__(self, ui, router):
        super(MyMainWindow, self).__init__()
        self.ui = ui
        self.ui.setupUi(self)
        self.router = router

        # setup event listeners

    def go_dashboard(self):
        self.router.setCurrentIndex(Pages.DASHBOARD.value)