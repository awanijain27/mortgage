import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
import resources
from DashBoard import Ui_MainWindow1

class LoginDialog(QDialog):
    # integrating add record ui
    def DashBoard(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self.window)
        self.window.showFullScreen()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(0, 0, 300, 150)
        self.setFixedSize(300, 150)
        self.setStyleSheet("background-color: #f0f0f0;")

        # Set the window icon (change 'icon.png' to the path of your desired icon file).
        self.setWindowIcon(QIcon(":/resources/resources/icons/download.ico"))

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.password_label = QLineEdit()
        self.password_label.setPlaceholderText("Enter Password")
        self.password_label.setEchoMode(QLineEdit.Password)
        self.password_label.setStyleSheet("padding: 10px; font-size: 14px; background-color: white; border: 1px solid #ccc;")

        self.login_button = QPushButton("Enter")
        self.login_button.setStyleSheet("padding: 10px; background-color: #3498db; color: white; font-weight: bold; font-size: 20px;")

        layout.addWidget(self.password_label)
        layout.addWidget(self.login_button)

        self.login_button.clicked.connect(self.login)

    def login(self):
        password = self.password_label.text()
        #login authentication logic here.
        if password == "khalwa":
            self.DashBoard()
            self.close()
        else:
            self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_dialog = LoginDialog()

    # Center the login dialog on the screen.
    center_point = app.desktop().availableGeometry().center()
    login_dialog.move(center_point - login_dialog.rect().center())

    login_dialog.show()
    sys.exit(app.exec_())
