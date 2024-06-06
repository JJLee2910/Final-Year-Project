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
    QVBoxLayout,
    QLabel
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPixmap, QImage
import cv2 as cv
import random
import numpy as np
from model import create_model
from keras.models import load_model

class DashboardController(QMainWindow):
    def __init__(self, router: QStackedWidget):
        super(DashboardController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.router = router

        self.ui.detectButton.clicked.connect(self.startDetection)
        self.ui.logoutButton.clicked.connect(self.logout)

        self.create_table()
        self.loadModel()

        self.video = None

        # Add QLabel for displaying video frames
        self.video_label = QLabel(self.ui.chart_frame)
        self.video_label.setAlignment(Qt.AlignCenter)

        self.faca_cascade = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

    def extractFeatures(self):
        self.feature = np.array(self.image)
        self.feature = self.feature.reshape(1, 48, 48, 1)
        return self.feature / 255.0
    
    def loadModel(self):
        self.emotional_model = create_model(num_classes=8)
        self.emotional_model.load_weights("Model/Optimized Model 2/model_v3.h5")
        print("Model loading from disk")

    def startDetection(self):
        print("detection started")
        self.video = cv.VideoCapture(0)

        while True:
            ret, frame = self.video.read()
            if not ret:
                print("Error: Failed to capture frame")
                break

            if frame is not None and frame.shape[0] > 0 and frame.shape[1] > 0:
                self.display_frame(frame)
            else:
                print("Error: Invalid frame dimensions")
                break

            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        if self.video is not None:
            self.video.release()
            cv.destroyAllWindows()

    def display_frame(self, frame):
        """Display frame in the QLabel"""
        rgb_image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        qt_img = QPixmap.fromImage(convert_to_Qt_format)

        chart_frame_size = self.ui.chart_frame.size()
        scaled_img = qt_img.scaled(chart_frame_size, Qt.KeepAspectRatio)
        
        self.video_label.setGeometry(0, 0, chart_frame_size.width(), chart_frame_size.height())
        self.video_label.setPixmap(scaled_img)

    def logout(self):
        print("logout")
        if self.video is not None:
            self.video.release()
            cv.destroyAllWindows()
        self.router.setCurrentIndex(0)

    def create_table(self):
        self.ui.tableWidget.setRowCount(8)  # 7 emotional classes
        self.ui.tableWidget.setColumnCount(2)  # 2 columns

        # Set the emotional classes in the first column
        self.emotional_classes = ["Angry", "Contempt", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]

        # Store the count of each emotional classes detected from the detector

        for row, emotion in enumerate(self.emotional_classes):
            item = QTableWidgetItem(emotion)
            item.setFlags(
                item.flags() ^ Qt.ItemIsEditable 
            )
            self.ui.tableWidget.setItem(row, 0, item)

        # emotions_count = []
        for row in range(7):
            item = QTableWidgetItem("")
            item.setFlags(
                item.flags() ^ Qt.ItemIsEditable 
            )
            self.ui.tableWidget.setItem(row, 1, item)
        # Set size policy to expand horizontally and vertically
        self.ui.tableWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Resize the columns to fit the contents
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)