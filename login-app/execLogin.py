import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox
from login import *
from execSignup import *
from execMenu import *
import psycopg2



class LoginUi(QMainWindow, Ui_MainWindow1):
    def __init__(self,parent = None):
        super().__init__(parent)
        super().setupUi(self)
        self.signupButton.clicked.connect(self.open_signup)
        self.signinButton.clicked.connect(self.try_login)
        

    def try_login(self):
        if self.userLine.text() == "" or self.passwordLine.text() == "":
            message = QMessageBox()
            message.setText("Please fill in all fields")
            message.exec_()
        else:
            user = self.userLine.text()
            password = self.passwordLine.text()

            try:
                bd = psycopg2.connect(host = "localhost",
                                        database = "login-app",
                                        user = "postgres",
                                        password = "12345") #DB password here
                cursor = bd.cursor()
                cursor.execute(f"SELECT password from users WHERE username = '{user}'")
                result = cursor.fetchall()
                if len(result) == 0:
                    message = QMessageBox()
                    message.setText("User not found!")
                    message.exec_()
                else:
                    if result[0][0] == password:
                        message = QMessageBox()
                        message.setText("login successfully!")
                        message.exec_()
                        window = MenuUi(self)
                        window.show()
                    else:
                        message = QMessageBox()
                        message.setText("Incorrect password!")
                        message.exec_()

            except Exception as e:
                print("Database connection error", e)
            
            finally:
                if bd is not None:
                    bd.close()

    def open_signup(self):
        window = SignupUi(self)
        window.show()

