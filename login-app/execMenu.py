import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox
from menu import *

class MenuUi(QMainWindow, Ui_MainWindow2):
    def __init__(self,parent = None):
        super().__init__(parent)
        super().setupUi(self)
        self.returnButton.clicked.connect(self.returnLogin)

    def returnLogin(self):
        self.close()