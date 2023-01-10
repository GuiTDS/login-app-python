import sys
from execLogin import *
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox

if __name__ == "__main__":
    qt = QApplication(sys.argv)
    loadUi = LoginUi()
    loadUi.show()
    qt.exec_()