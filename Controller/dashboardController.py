from UI.dashboard import Ui_MainWindow
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QStackedWidget,
    QTableWidget,
    QMessageBox,
    QTableWidgetItem,
)
import cv2 as cv
class DashboardController(QMainWindow):
    def __init__(self, router : QStackedWidget):
        super(DashboardController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.router = router

        self.ui.detectButton.clicked.connect(self.startDetection)
        self.ui.logoutButton.clicked.connect(self.logout)
        self.create_table()

        self.video = None

    def startDetection(self):
        print("detection started")
        self.video = cv.VideoCapture(0)

        while(True):
            ret, frame = self.video.read()
            if not ret:
                print("Error: Failed to capture frame")
                break
            
            if frame is not None and frame.shape[0] > 0 and frame.shape[1] > 0:
                cv.imshow("Frame", frame)
            else:
                print("Error: Invalid frame dimensions")
                break

            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        if self.video is not None:
            self.video.release()
            cv.destroyAllWindows()  
    
    def logout(self):
        print("logout")
        if self.video is not None:
            self.video.release()
            cv.destroyAllWindows()
        self.router.setCurrentIndex(0)

    def create_table(self):
        self.ui.tableWidget = QTableWidget()

        self.ui.tableWidget.setRowCount(2)
        self.ui.tableWidget.setColumnCount(8)
        pass
        