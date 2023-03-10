# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(409, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
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
        self.menuTitleLabel.setGeometry(QtCore.QRect(140, 50, 111, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.menuTitleLabel.setFont(font)
        self.menuTitleLabel.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.menuTitleLabel.setObjectName("menuTitleLabel")
        self.signinButton = QtWidgets.QPushButton(self.frame)
        self.signinButton.setGeometry(QtCore.QRect(100, 330, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.signinButton.setFont(font)
        self.signinButton.setStyleSheet("QPushButton#signinButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(10, 5, 20, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#signinButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(10, 5, 20, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#signinButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 220)\n"
"}")
        self.signinButton.setObjectName("signinButton")
        self.userLine = QtWidgets.QLineEdit(self.frame)
        self.userLine.setGeometry(QtCore.QRect(100, 150, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userLine.setFont(font)
        self.userLine.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 3px solid rgba(105, 118, 132, 255);\n"
"color: rgba(255, 255, 255, 230);\n"
"padding-bottom: 7px;")
        self.userLine.setObjectName("userLine")
        self.passwordLine = QtWidgets.QLineEdit(self.frame)
        self.passwordLine.setGeometry(QtCore.QRect(100, 230, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwordLine.setFont(font)
        self.passwordLine.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 3px solid rgba(105, 118, 132, 255);\n"
"color: rgba(255, 255, 255, 230);\n"
"padding-bottom: 7px;")
        self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLine.setObjectName("passwordLine")
        self.signupButton = QtWidgets.QPushButton(self.frame)
        self.signupButton.setGeometry(QtCore.QRect(100, 400, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.signupButton.setFont(font)
        self.signupButton.setStyleSheet("QPushButton#signupButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(10, 5, 20, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#signupButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(10, 5, 20, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#signupButton:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 220)\n"
"}")
        self.signupButton.setObjectName("signupButton")
        MainWindow1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 409, 26))
        self.menubar.setObjectName("menubar")
        MainWindow1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow1)
        self.statusbar.setObjectName("statusbar")
        MainWindow1.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "MainWindow"))
        self.menuTitleLabel.setText(_translate("MainWindow1", "LOGIN"))
        self.signinButton.setText(_translate("MainWindow1", "SIGN IN"))
        self.userLine.setPlaceholderText(_translate("MainWindow1", "User"))
        self.passwordLine.setPlaceholderText(_translate("MainWindow1", "Password"))
        self.signupButton.setText(_translate("MainWindow1", "SIGN UP"))
