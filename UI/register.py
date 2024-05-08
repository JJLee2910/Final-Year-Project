# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.regPageWidget = QtWidgets.QWidget(self.centralwidget)
        self.regPageWidget.setGeometry(QtCore.QRect(91, 150, 591, 421))
        self.regPageWidget.setObjectName("regPageWidget")
        self.usernameRegInput = QtWidgets.QLineEdit(self.regPageWidget)
        self.usernameRegInput.setGeometry(QtCore.QRect(40, 110, 509, 20))
        self.usernameRegInput.setObjectName("usernameRegInput")
        self.passwordRegInput = QtWidgets.QLineEdit(self.regPageWidget)
        self.passwordRegInput.setGeometry(QtCore.QRect(40, 210, 509, 20))
        self.passwordRegInput.setText("")
        self.passwordRegInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordRegInput.setObjectName("passwordRegInput")
        self.loginPageLabel = QtWidgets.QLabel(self.regPageWidget)
        self.loginPageLabel.setGeometry(QtCore.QRect(40, 17, 509, 67))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.loginPageLabel.setFont(font)
        self.loginPageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loginPageLabel.setObjectName("loginPageLabel")
        self.usernameRegLabel = QtWidgets.QLabel(self.regPageWidget)
        self.usernameRegLabel.setGeometry(QtCore.QRect(40, 70, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.usernameRegLabel.setFont(font)
        self.usernameRegLabel.setObjectName("usernameRegLabel")
        self.passwordRegLabel = QtWidgets.QLabel(self.regPageWidget)
        self.passwordRegLabel.setGeometry(QtCore.QRect(40, 170, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.passwordRegLabel.setFont(font)
        self.passwordRegLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.passwordRegLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.passwordRegLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.passwordRegLabel.setObjectName("passwordRegLabel")
        self.regButton = QtWidgets.QPushButton(self.regPageWidget)
        self.regButton.setGeometry(QtCore.QRect(230, 360, 101, 41))
        self.regButton.setObjectName("regButton")
        self.passwordRegLabel_2 = QtWidgets.QLabel(self.regPageWidget)
        self.passwordRegLabel_2.setGeometry(QtCore.QRect(40, 270, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.passwordRegLabel_2.setFont(font)
        self.passwordRegLabel_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.passwordRegLabel_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.passwordRegLabel_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.passwordRegLabel_2.setObjectName("passwordRegLabel_2")
        self.passwordRegInput_2 = QtWidgets.QLineEdit(self.regPageWidget)
        self.passwordRegInput_2.setGeometry(QtCore.QRect(40, 310, 509, 20))
        self.passwordRegInput_2.setText("")
        self.passwordRegInput_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordRegInput_2.setObjectName("passwordRegInput_2")
        self.loginWidget = QtWidgets.QWidget(self.centralwidget)
        self.loginWidget.setGeometry(QtCore.QRect(90, 10, 641, 131))
        self.loginWidget.setObjectName("loginWidget")
        self.logoLabel = QtWidgets.QLabel(self.loginWidget)
        self.logoLabel.setGeometry(QtCore.QRect(20, 10, 101, 111))
        self.logoLabel.setStyleSheet("border-image: url(:/images/Icons/Logo-APU-200.png);\n"
"")
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        self.titleLabel = QtWidgets.QLabel(self.loginWidget)
        self.titleLabel.setGeometry(QtCore.QRect(130, 20, 491, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setTextFormat(QtCore.Qt.RichText)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginPageLabel.setText(_translate("MainWindow", "REGISTER PAGE"))
        self.usernameRegLabel.setText(_translate("MainWindow", "Username"))
        self.passwordRegLabel.setText(_translate("MainWindow", "Password"))
        self.regButton.setText(_translate("MainWindow", "Register"))
        self.passwordRegLabel_2.setText(_translate("MainWindow", "Confirmed Password"))
        self.titleLabel.setText(_translate("MainWindow", "APU Workspace@Facial Emotion Recognition System"))
from UI import res