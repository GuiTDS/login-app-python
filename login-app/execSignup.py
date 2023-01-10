import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox
from signup import *
import psycopg2



class SignupUi(QMainWindow, Ui_MainWindow3):
    def __init__(self,parent = None):
        super().__init__(parent)
        super().setupUi(self)
        self.signupButton.clicked.connect(self.register)

    def register(self):
        # validation
        if self.nameLine.text() == "" or self.userLine.text() == "" or self.passwordLine.text() == "":
            message = QMessageBox()
            message.setText("Please fill in all fields")
            message.exec_()
        else:
            name = self.nameLine.text()
            user_name = self.userLine.text()
            password = self.passwordLine.text()

            try:
                bd = psycopg2.connect(host = "localhost",
                                        database = "login-app",
                                        user = "postgres",
                                        password = "12345") #DB password here
                cursor = bd.cursor()
                cursor.execute(f"INSERT INTO users (name, username, password) VALUES ('{name}', '{user_name}', '{password}');")
                bd.commit()
                mensagem = QMessageBox()
                mensagem.setText("successful registration")
                mensagem.exec_()
                self.close()
            except Exception as e:
                print("Database connection error", e)
            
            finally:
                if bd is not None:
                    bd.close()

        


