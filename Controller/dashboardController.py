from UI.dashboard import Ui_MainWindow
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
    QTableWidget,
    QTableWidgetItem,
    QSizePolicy,
    QHeaderView,
    QVBoxLayout,
    QLabel,
    QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPixmap, QImage
import cv2 as cv
import numpy as np
import os
import datetime
from model import create_model

class DashboardController(QMainWindow):
    def __init__(self, router: QStackedWidget):
        super(DashboardController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.router = router

        self.ui.detectButton.clicked.connect(self.startDetection)
        self.ui.logoutButton.clicked.connect(self.logout)
        self.ui.pushButton.clicked.connect(self.saveCaptured)

        self.create_table()
        self.loadModel()

        self.video = None

        # Add QLabel for displaying video frames
        self.video_label = QLabel(self.ui.chart_frame)
        self.video_label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout(self.ui.chart_frame)
        layout.addWidget(self.video_label)

        self.face_cascade = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

        self.current_frame = None
        self.detected_emotion = None

        self.emotional_counts = {emotion:0 for emotion in self.emotional_classes}

    def extractFeatures(self, image):
        feature = np.array(image)
        feature = feature.reshape(1, 48, 48, 1)
        return feature / 255.0
    
    def loadModel(self):
        self.emotional_model = create_model(num_classes=8)
        self.emotional_model.load_weights("Model/Optimized Model 2/model_v3.h5")
        print("Model loaded from disk")

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
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray_frame[y:y+h, x:x+w]
            roi_gray = cv.resize(roi_gray, (48, 48))
            features = self.extractFeatures(roi_gray)
            emotion_prediction = self.emotional_model.predict(features)
            max_index = int(np.argmax(emotion_prediction))
            self.detected_emotion = self.emotional_classes[max_index]
            cv.putText(frame, self.detected_emotion, (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

            self.emotional_counts[self.detected_emotion] += 1
            self.updateTable()

        rgb_image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        qt_img = QPixmap.fromImage(convert_to_Qt_format)

        chart_frame_size = self.ui.chart_frame.size()
        scaled_img = qt_img.scaled(chart_frame_size, Qt.KeepAspectRatio)
        
        self.video_label.setGeometry(0, 0, chart_frame_size.width(), chart_frame_size.height())
        self.video_label.setPixmap(scaled_img)

        self.current_frame = frame

    def updateTable(self):
        for row, emotion in enumerate(self.emotional_classes):
            count = self.emotional_counts[emotion]
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(count)))

    def logout(self):
        print("Logout")
        if self.video is not None:
            self.video.release()
            cv.destroyAllWindows()
        self.router.setCurrentIndex(0)

    def create_table(self):
        self.ui.tableWidget.setRowCount(8)  # 8 emotional classes
        self.ui.tableWidget.setColumnCount(2)  # 2 columns

        # Set the emotional classes in the first column
        self.emotional_classes = ["Angry", "Contempt", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]

        # Store the count of each emotional classes detected from the detector
        for row, emotion in enumerate(self.emotional_classes):
            item = QTableWidgetItem(emotion)
            item.setFlags(item.flags() ^ Qt.ItemIsEditable)
            self.ui.tableWidget.setItem(row, 0, item)

        for row in range(8):
            item = QTableWidgetItem("0")
            item.setFlags(item.flags() ^ Qt.ItemIsEditable)
            self.ui.tableWidget.setItem(row, 1, item)

        # Set size policy to expand horizontally and vertically
        self.ui.tableWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Resize the columns to fit the contents
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def saveCaptured(self):
        # based on the frame display with the emotional classes label, 
        # save the display into the directory of "C:\Users\JJ\OneDrive\Desktop\Final-Year-Project\Images"
        try:
            if self.current_frame is not None and self.detected_emotion is not None:
                save_dir = "C:\\Users\\JJ\\OneDrive\\Desktop\\Final-Year-Project\\Images"
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)
                
                # options = QFileDialog.Options()
                # file_path, _ = QFileDialog.getSaveFileName(self, "Save Captured Image", save_dir, "Images (*.png *.jpg *.jpeg)", options=options)
                # if file_path:
                #     cv.imwrite(file_path, self.current_frame)
                #     print("Image saved")
                # else:
                #     print("No frame saved")

                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                file_name = f"{self.detected_emotion}_{timestamp}.jpg"
                file_path = os.path.join(save_dir, file_name)

                cv.imwrite(file_path, self.current_frame)
                print(f"Image saved to {file_path}")
            else:
                raise ValueError("No frame to save or no emotion detected")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
