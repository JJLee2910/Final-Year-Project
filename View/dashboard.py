from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 190, 261, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.loginWidget = QtWidgets.QWidget(self.centralwidget)
        self.loginWidget.setGeometry(QtCore.QRect(10, 10, 671, 131))
        self.loginWidget.setObjectName("loginWidget")
        self.logoLabel = QtWidgets.QLabel(self.loginWidget)
        self.logoLabel.setGeometry(QtCore.QRect(20, 10, 101, 111))
        self.logoLabel.setStyleSheet("border-image: url(:/images/Icons/Logo-APU-200.png);\n"
                                     "")
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        self.titleLabel = QtWidgets.QLabel(self.loginWidget)
        self.titleLabel.setGeometry(QtCore.QRect(130, 20, 501, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setTextFormat(QtCore.Qt.RichText)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 150, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.chart_frame = QtWidgets.QFrame(self.centralwidget)
        self.chart_frame.setGeometry(QtCore.QRect(280, 160, 401, 351))
        self.chart_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chart_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chart_frame.setObjectName("chart_frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.chart_frame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.chart_widget = QtWidgets.QStackedWidget(self.chart_frame)
        self.chart_widget.setObjectName("chart_widget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.defect_chart_frame = QtWidgets.QFrame(self.page)
        self.defect_chart_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.defect_chart_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.defect_chart_frame.setObjectName("defect_chart_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.defect_chart_frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6.addWidget(self.defect_chart_frame, 0, QtCore.Qt.AlignTop)
        self.chart = QtWidgets.QFrame(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart.sizePolicy().hasHeightForWidth())
        self.chart.setSizePolicy(sizePolicy)
        self.chart.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chart.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chart.setObjectName("chart")
        self.gridLayout = QtWidgets.QGridLayout(self.chart)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_6.addWidget(self.chart)
        self.chart_widget.addWidget(self.page)
        self.horizontalLayout_7.addWidget(self.chart_widget)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(280, 520, 401, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logoutButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.logoutButton.setObjectName("logoutButton")
        self.horizontalLayout.addWidget(self.logoutButton)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.detectButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.detectButton.setObjectName("detectButton")
        self.horizontalLayout.addWidget(self.detectButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.chart_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Apply styles to buttons
        self.apply_button_styles()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Emotions Classes"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Counts"))
        self.titleLabel.setText(_translate("MainWindow", "APU Workspace@Facial Emotion Recognition System"))
        self.label.setText(_translate("MainWindow", "Workplace Emotional Count"))
        self.logoutButton.setText(_translate("MainWindow", "Logout"))
        self.pushButton.setText(_translate("MainWindow", "Save Captured"))
        self.detectButton.setText(_translate("MainWindow", "Start Detection"))

    def apply_button_styles(self):
        logout_button_style = """
            QPushButton {
                background-color: #f44336; /* Red background */
                color: white; /* White text */
                border: none; /* No border */
                padding: 10px 20px; /* Padding */
                font-size: 16px; /* Font size */
                border-radius: 5px; /* Rounded corners */
            }
            QPushButton:hover {
                background-color: #e57373; /* Lighter red on hover */
            }
            QPushButton:pressed {
                background-color: #d32f2f; /* Darker red on press */
            }
        """

        save_button_style = """
            QPushButton {
                background-color: #2196F3; /* Blue background */
                color: white; /* White text */
                border: none; /* No border */
                padding: 10px 20px; /* Padding */
                font-size: 16px; /* Font size */
                border-radius: 5px; /* Rounded corners */
            }
            QPushButton:hover {
                background-color: #64B5F6; /* Lighter blue on hover */
            }
            QPushButton:pressed {
                background-color: #1976D2; /* Darker blue on press */
            }
        """

        detect_button_style = """
            QPushButton {
                background-color: #4CAF50; /* Green background */
                color: white; /* White text */
                border: none; /* No border */
                padding: 10px 20px; /* Padding */
                font-size: 16px; /* Font size */
                border-radius: 5px; /* Rounded corners */
            }
            QPushButton:hover {
                background-color: #45a049; /* Darker green on hover */
            }
            QPushButton:pressed {
                background-color: #3e8e41; /* Even darker green on press */
            }
        """
        self.logoutButton.setStyleSheet(logout_button_style)
        self.pushButton.setStyleSheet(save_button_style)
        self.detectButton.setStyleSheet(detect_button_style)


from View import res