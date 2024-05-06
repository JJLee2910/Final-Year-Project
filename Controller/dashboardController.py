from UI.dashboard import Ui_MainWindow
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QStackedWidget,
    QTableWidgetItem,
    QMessageBox,
)

class DashboardController(QMainWindow):
    def __init__(self, router : QStackedWidget):
        super(DashboardController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.router = router

        self.ui.detectButton.clicked.connect(self.startDetection)
        self.ui.logoutButton.clicked.connect(self.logout)

    def startDetection(self):
        print("detection started")
    
    def logout(self):
        print("logout")
        self.router.setCurrentIndex(0)