from UI.dashboard import Ui_MainWindow
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QStackedWidget,
    QTableWidget,
    QMessageBox,
    QTableWidgetItem,
    QSizePolicy,
    QHeaderView,
)
from PyQt5.QtCore import Qt
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
        self.load_chart()

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
        self.ui.tableWidget.setRowCount(7)  # 7 emotional classes
        self.ui.tableWidget.setColumnCount(2)  # 2 columns

        # Set the emotional classes in the first column
        emotional_classes = ["Angry", "Happy", "Sad", "Surprised", "Disgusted", "Fearful", "Neutral"]
        for row, emotion in enumerate(emotional_classes):
            item = QTableWidgetItem(emotion)
            item.setFlags(
                item.flags() ^ Qt.ItemIsEditable 
            )
            self.ui.tableWidget.setItem(row, 0, item)

        emotions_count = []
        for row in range(7):
            item = QTableWidgetItem(emotions_count)
            item.setFlags(
                item.flags() ^ Qt.ItemIsEditable 
            )
            self.ui.tableWidget.setItem(row, 1, item)
        # Set size policy to expand horizontally and vertically
        self.ui.tableWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Resize the columns to fit the contents
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def load_chart(self):
        pass
        