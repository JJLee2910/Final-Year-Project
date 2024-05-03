import os
import sys

from PyQt5.QtCore import Qt
from UI.Login import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from app_data import AppData
from enums import Pages

class MyMainWindow(QWidget):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.ui = Ui_loginForm()
        self.ui.setupUi(self)

        # create instance of the UI form

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())