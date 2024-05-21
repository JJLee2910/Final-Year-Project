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
    QVBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis
from PyQt5.QtGui import QPainter
import cv2 as cv
import random

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
        self.emotional_classes = ["Angry", "Happy", "Sad", "Surprised", "Disgusted", "Fearful", "Neutral"]

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

    def load_chart(self):
        # emotional monthly count chart
        self.chart = QChart()

        # get each emotion class count of the month
        self.series = QBarSeries()
        self.bar_set = QBarSet("Emotions")

        # Initialize the bar set with zero values
        self.bar_set.append([0] * len(self.emotional_classes))
        self.series.append(self.bar_set)
        self.chart.addSeries(self.series)

        # add emotions categories to the bar set
        axis_x = QBarCategoryAxis()
        axis_x.append(self.emotional_classes)
        self.chart.addAxis(axis_x, Qt.AlignBottom)
        self.series.attachAxis(axis_x)

        # Create the chart view and add the chart to it
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        # Find the layout within the chart_widget
        chart_layout = self.ui.chart_widget.findChild(QVBoxLayout)
        if chart_layout is not None:
            # Remove any existing widgets from the layout
            while chart_layout.count():
                item = chart_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

            # Set the size policy of the chart view to expand
            self.chart_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            # Add the chart view to the layout
            chart_layout.addWidget(self.chart_view)
        else:
            print("Could not find the layout within the chart_widget")

        self.update_chart()

    def update_chart(self):
        # Generate some random data for the chart
        counts = [random.randint(0, 100) for _ in self.emotional_classes]

        # Update the table with the new data
        for row, count in enumerate(counts):
            self.ui.tableWidget.item(row, 1).setText(str(count))

        # Update the bar set with the new data
        for i, count in enumerate(counts):
            self.bar_set.replace(i, count)

        # Refresh the chart
        self.chart_view.repaint()