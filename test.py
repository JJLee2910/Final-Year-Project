import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QImage, QPixmap

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def run(self):
        # Capture video from the webcam
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
            else:
                break
        cap.release()

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Camera Interface")
        self.disply_width = 600  # UI frame width
        self.display_height = 600  # UI frame height
        self.video_width = 48  # Video feed width
        self.video_height = 48  # Video feed height
        self.initUI()

    def initUI(self):
        # Create a vertical box layout and add the label and button
        vbox = QVBoxLayout()

        # Add a QLabel to display the video feed
        self.image_label = QLabel(self)
        self.image_label.resize(self.video_width, self.video_height)
        vbox.addWidget(self.image_label)

        # Add a button to start the video feed
        self.start_button = QPushButton("Start Detection")
        self.start_button.clicked.connect(self.start_detection)
        vbox.addWidget(self.start_button)

        self.setLayout(vbox)

    def start_detection(self):
        # Create the video capture thread
        self.thread = VideoThread()
        self.thread.change_pixmap_signal.connect(self.display_video_stream)
        self.thread.start()
        self.start_button.setEnabled(False)

    def display_video_stream(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        resized_image = cv2.resize(rgb_image, (48, 48))
        h, w, ch = resized_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(resized_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        return QPixmap.fromImage(convert_to_Qt_format)

def main():
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
