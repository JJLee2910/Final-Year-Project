# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1367, 850)
        Form.setAutoFillBackground(True)
        self.gridLayout_5 = QtWidgets.QGridLayout(Form)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setMaximumSize(QtCore.QSize(300, 52))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_add_rectangle = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_rectangle.sizePolicy().hasHeightForWidth())
        self.btn_add_rectangle.setSizePolicy(sizePolicy)
        self.btn_add_rectangle.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_add_rectangle.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_add_rectangle.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/rectangle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_rectangle.setIcon(icon)
        self.btn_add_rectangle.setIconSize(QtCore.QSize(50, 50))
        self.btn_add_rectangle.setObjectName("btn_add_rectangle")
        self.gridLayout_2.addWidget(self.btn_add_rectangle, 0, 0, 1, 3)
        self.btn_prev = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_prev.sizePolicy().hasHeightForWidth())
        self.btn_prev.setSizePolicy(sizePolicy)
        self.btn_prev.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_prev.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_prev.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_prev.setIcon(icon1)
        self.btn_prev.setIconSize(QtCore.QSize(50, 50))
        self.btn_prev.setObjectName("btn_prev")
        self.gridLayout_2.addWidget(self.btn_prev, 1, 0, 1, 1)
        self.btn_deleterectangle = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_deleterectangle.sizePolicy().hasHeightForWidth())
        self.btn_deleterectangle.setSizePolicy(sizePolicy)
        self.btn_deleterectangle.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_deleterectangle.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_deleterectangle.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_deleterectangle.setIcon(icon2)
        self.btn_deleterectangle.setIconSize(QtCore.QSize(50, 50))
        self.btn_deleterectangle.setObjectName("btn_deleterectangle")
        self.gridLayout_2.addWidget(self.btn_deleterectangle, 2, 0, 1, 3)
        self.btn_next = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_next.sizePolicy().hasHeightForWidth())
        self.btn_next.setSizePolicy(sizePolicy)
        self.btn_next.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_next.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_next.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_next.setIcon(icon3)
        self.btn_next.setIconSize(QtCore.QSize(50, 50))
        self.btn_next.setObjectName("btn_next")
        self.gridLayout_2.addWidget(self.btn_next, 1, 1, 1, 2)
        self.gridLayout_5.addWidget(self.groupBox, 6, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setMinimumSize(QtCore.QSize(850, 650))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setAutoFillBackground(True)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.graphicsView = PhotoViewer(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(800, 630))
        self.graphicsView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.graphicsView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.graphicsView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_4.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame, 0, 1, 7, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidget_rectangles = QtWidgets.QListWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_rectangles.sizePolicy().hasHeightForWidth())
        self.listWidget_rectangles.setSizePolicy(sizePolicy)
        self.listWidget_rectangles.setMinimumSize(QtCore.QSize(200, 130))
        self.listWidget_rectangles.setMaximumSize(QtCore.QSize(300, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_rectangles.setFont(font)
        self.listWidget_rectangles.setObjectName("listWidget_rectangles")
        self.gridLayout_3.addWidget(self.listWidget_rectangles, 1, 0, 1, 1)
        self.btn_save = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QtCore.QSize(130, 30))
        self.btn_save.setMaximumSize(QtCore.QSize(300, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_save.setFont(font)
        self.btn_save.setObjectName("btn_save")
        self.gridLayout_3.addWidget(self.btn_save, 8, 0, 1, 1)
        self.listWidget_classes = QtWidgets.QListWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_classes.sizePolicy().hasHeightForWidth())
        self.listWidget_classes.setSizePolicy(sizePolicy)
        self.listWidget_classes.setMinimumSize(QtCore.QSize(200, 250))
        self.listWidget_classes.setMaximumSize(QtCore.QSize(300, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_classes.setFont(font)
        self.listWidget_classes.setObjectName("listWidget_classes")
        self.gridLayout_3.addWidget(self.listWidget_classes, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 3, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_3.addWidget(self.listWidget, 7, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.comboBox = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_3.addWidget(self.comboBox, 6, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 1, 2, 6, 1)
        self.btn_open_classes = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_open_classes.sizePolicy().hasHeightForWidth())
        self.btn_open_classes.setSizePolicy(sizePolicy)
        self.btn_open_classes.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_open_classes.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/pen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_open_classes.setIcon(icon4)
        self.btn_open_classes.setIconSize(QtCore.QSize(50, 50))
        self.btn_open_classes.setObjectName("btn_open_classes")
        self.gridLayout_5.addWidget(self.btn_open_classes, 3, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setMinimumSize(QtCore.QSize(270, 450))
        self.tableWidget.setMaximumSize(QtCore.QSize(300, 800))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_5.addWidget(self.tableWidget, 5, 0, 1, 1)
        self.btn_open_folder = QtWidgets.QPushButton(Form)
        self.btn_open_folder.setMinimumSize(QtCore.QSize(200, 50))
        self.btn_open_folder.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_open_folder.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_open_folder.setIcon(icon5)
        self.btn_open_folder.setIconSize(QtCore.QSize(50, 50))
        self.btn_open_folder.setObjectName("btn_open_folder")
        self.gridLayout_5.addWidget(self.btn_open_folder, 4, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Labelling Software"))
        self.label_25.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Image Labelling</span></p></body></html>"))
        self.groupBox.setTitle(_translate("Form", "Controls"))
        self.btn_add_rectangle.setText(_translate("Form", "Add Rectangle"))
        self.btn_prev.setText(_translate("Form", "Previous"))
        self.btn_deleterectangle.setText(_translate("Form", "Delete Rectangles"))
        self.btn_next.setText(_translate("Form", "Next "))
        self.btn_save.setText(_translate("Form", "Save"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Labels</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Select Classes</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "Classes Filter:"))
        self.btn_open_classes.setText(_translate("Form", "Open Classes.txt"))
        self.btn_open_folder.setText(_translate("Form", "Open Folder"))
from photoviewer import PhotoViewer
