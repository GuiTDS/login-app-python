# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(409, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 20, 401, 501))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.opacityLabel = QtWidgets.QLabel(self.frame)
        self.opacityLabel.setGeometry(QtCore.QRect(20, 20, 360, 470))
        self.opacityLabel.setStyleSheet("background-color: rgba(0, 0, 0, 165);\n"
"border-radius: 20px;")
        self.opacityLabel.setText("")
        self.opacityLabel.setObjectName("opacityLabel")
        self.menuTitleLabel = QtWidgets.QLabel(self.frame)
        self.menuTitleLabel.setGeometry(QtCore.QRect(150, 50, 101, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.menuTitleLabel.setFont(font)
        self.menuTitleLabel.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.menuTitleLabel.setObjectName("menuTitleLabel")
        self.returnButton = QtWidgets.QPushButton(self.frame)
        self.returnButton.setGeometry(QtCore.QRect(100, 400, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.returnButton.setFont(font)
        self.returnButton.setStyleSheet("QPushButton#returnButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(10, 5, 20, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#returnButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(10, 5, 20, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#returnButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 220)\n"
"}")
        self.returnButton.setObjectName("returnButton")
        self.congratsLabel = QtWidgets.QLabel(self.frame)
        self.congratsLabel.setGeometry(QtCore.QRect(50, 190, 311, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.congratsLabel.setFont(font)
        self.congratsLabel.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.congratsLabel.setObjectName("congratsLabel")
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 409, 26))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "MainWindow"))
        self.menuTitleLabel.setText(_translate("MainWindow2", "MENU"))
        self.returnButton.setText(_translate("MainWindow2", "RETURN"))
        self.congratsLabel.setText(_translate("MainWindow2", "Congratulations!! You\'ve logged in!"))