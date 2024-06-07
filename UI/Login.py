# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginPageWidget = QtWidgets.QWidget(self.centralwidget)
        self.loginPageWidget.setGeometry(QtCore.QRect(41, 160, 591, 381))
        self.loginPageWidget.setObjectName("loginPageWidget")
        self.usernameInput = QtWidgets.QLineEdit(self.loginPageWidget)
        self.usernameInput.setGeometry(QtCore.QRect(40, 110, 509, 20))
        self.usernameInput.setObjectName("usernameInput")
        self.passwordInput = QtWidgets.QLineEdit(self.loginPageWidget)
        self.passwordInput.setGeometry(QtCore.QRect(40, 230, 509, 20))
        self.passwordInput.setText("")
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.loginPageLabel = QtWidgets.QLabel(self.loginPageWidget)
        self.loginPageLabel.setGeometry(QtCore.QRect(40, 17, 509, 67))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.loginPageLabel.setFont(font)
        self.loginPageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loginPageLabel.setObjectName("loginPageLabel")
        self.usernameLabel = QtWidgets.QLabel(self.loginPageWidget)
        self.usernameLabel.setGeometry(QtCore.QRect(40, 70, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(self.loginPageWidget)
        self.passwordLabel.setGeometry(QtCore.QRect(40, 190, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.passwordLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.passwordLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.passwordLabel.setObjectName("passwordLabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.loginPageWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 299, 561, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.buttonLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.setObjectName("buttonLayout")
        self.registerButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.registerButton.setObjectName("registerButton")
        self.buttonLayout.addWidget(self.registerButton)
        self.loginButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.loginButton.setObjectName("loginButton")
        self.buttonLayout.addWidget(self.loginButton)
        self.loginWidget = QtWidgets.QWidget(self.centralwidget)
        self.loginWidget.setGeometry(QtCore.QRect(40, 20, 651, 131))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginPageLabel.setText(_translate("MainWindow", "LOGIN PAGE"))
        self.usernameLabel.setText(_translate("MainWindow", "Username"))
        self.passwordLabel.setText(_translate("MainWindow", "Password"))
        self.registerButton.setText(_translate("MainWindow", "Register"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.titleLabel.setText(_translate("MainWindow", "APU Workspace@Facial Emotion Recognition System"))

from UI import res
