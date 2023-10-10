# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_deposit.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
import mysql.connector
from tkinter import messagebox
import resources



class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter

class Ui_MainWindow5(object):
    def connect2db(self):
        self.con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shailesh@123",
        database="loan_management",
        auth_plugin="caching_sha2_password" 
        )
    def search_data(self):
        self.connect2db()
        mycursor = self.con.cursor()
        name = self.lineEdit.text()
        query = "SELECT * FROM all_records WHERE name = %s"
        values = (name,)

        try:
                mycursor.execute(query, values)
                result = mycursor.fetchall()
                
                self.tableWidget.setRowCount(0)
                
                for row_number, row_data in enumerate(result):
                        self.tableWidget.insertRow(row_number)
                        
                        for column_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        

 
                self.tableWidget.itemClicked.connect(self.extract_id)
        except Exception as e:
            messagebox.showerror("Error",f"Error due to {str(e)}")
    def extract_id(self, item):
        try:
            self.id = item.text()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")

    def add_deposit(self):
        try:
            self.connect2db()
            mycursor = self.con.cursor()
            deposit = int(self.lineEdit_2.text())
            query = '''UPDATE all_records
                        SET deposit = IFNULL(deposit, 0) + %s,
                        deposit_date = CURDATE()
                        WHERE user_id = %s;'''
            values = (deposit, self.id)
            mycursor.execute(query, values)
            messagebox.showinfo("Success","Deposit Added Successfully")
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.tableWidget.setRowCount(0)

            self.con.commit()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 892)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/resources/icons/add_deposit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBar = QtWidgets.QFrame(self.centralwidget)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 30))
        self.toolBar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.toolBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.toolBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toolBar.setObjectName("toolBar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.toolBar)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toggleFrame = QtWidgets.QFrame(self.toolBar)
        self.toggleFrame.setMinimumSize(QtCore.QSize(30, 30))
        self.toggleFrame.setMaximumSize(QtCore.QSize(30, 30))
        self.toggleFrame.setStyleSheet("background-color: rgb(59, 65, 71);")
        self.toggleFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.toggleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toggleFrame.setObjectName("toggleFrame")
        self.toggleButton = QtWidgets.QPushButton(self.toggleFrame)
        self.toggleButton.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.toggleButton.setMinimumSize(QtCore.QSize(30, 30))
        self.toggleButton.setMaximumSize(QtCore.QSize(30, 30))
        self.toggleButton.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-left: 3px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-left: 3px solid rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(25, 25, 25);\n"
"}")
        self.toggleButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/icons8_menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toggleButton.setIcon(icon)
        self.toggleButton.setIconSize(QtCore.QSize(30, 30))
        self.toggleButton.setObjectName("toggleButton")
        self.horizontalLayout_2.addWidget(self.toggleFrame)
        self.headerFrame = QtWidgets.QFrame(self.toolBar)
        self.headerFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerFrame.setObjectName("headerFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.headerFrame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(218, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.headerFrame)
        self.label.setStyleSheet("color: rgb(176, 176, 176);")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(58, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.userFrame = QtWidgets.QFrame(self.headerFrame)
        self.userFrame.setMinimumSize(QtCore.QSize(200, 30))
        self.userFrame.setMaximumSize(QtCore.QSize(200, 30))
        self.userFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.userFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userFrame.setObjectName("userFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.userFrame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 20, 0)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3.addWidget(self.userFrame)
        self.horizontalLayout_2.addWidget(self.headerFrame)
        self.verticalLayout.addWidget(self.toolBar)
        self.Body = QtWidgets.QFrame(self.centralwidget)
        self.Body.setStyleSheet("")
        self.Body.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Body.setObjectName("Body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Body)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Container = QtWidgets.QFrame(self.Body)
        self.Container.setStyleSheet("background-color: rgb(34, 34, 34);")
        self.Container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Container.setObjectName("Container")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.Container)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.stackedWidget = QtWidgets.QStackedWidget(self.Container)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setStyleSheet("background-color: rgb(175,175,175);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("border:none;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("border:2px solid black;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setStyleSheet("font: 24pt \"Segoe UI\";\n"
"font: 9pt \"Segoe UI\";\n"
"font: 550 55pt \"Segoe UI\";\n"
"border: none")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setStyleSheet("\n"
"border:none;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setStyleSheet("border:none;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comboBox = QtWidgets.QComboBox(self.frame_6)
        self.comboBox.setMinimumSize(QtCore.QSize(327, 0))
        self.comboBox.setStyleSheet("border:2px solid black;\n"
"font: 15pt \"Segoe UI\";\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setStyleSheet("font: 15pt \"Segoe UI\";")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_6.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setStyleSheet("border:none;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit.setStyleSheet("border:2px solid black;\n"
"font: 16pt \"Segoe UI\";")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_7.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_2.setStyleSheet("border:2px solid black;\n"
"font: 15pt \"Segoe UI\";")
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_7.addWidget(self.lineEdit_2)
        self.horizontalLayout_6.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setStyleSheet("border:none;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_3.setMinimumSize(QtCore.QSize(200, 45))
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border:2px solid black;\n"
"font: 15pt \"Segoe UI\";\n"
"background-color: rgb(3, 53, 127);\n"
"border-radius: 5px")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/icons8_todo_list.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.search_data)
        self.verticalLayout_5.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_4.setMinimumSize(QtCore.QSize(200, 45))
        self.pushButton_4.setMaximumSize(QtCore.QSize(200, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border:2px solid black;\n"
"background-color: rgb(255, 114, 43);\n"
"font: 15pt \"Segoe UI\";\n"
"\n"
"border-radius: 5px")
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.add_deposit)
        self.verticalLayout_5.addWidget(self.pushButton_4)
        self.horizontalLayout_6.addWidget(self.frame_8)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("border:none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setStyleSheet("border:2px solid black;")
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet("QTableWidget {font-size: 30px;}")
        self.tableWidget.verticalHeader().setDefaultAlignment(Qt.AlignCenter)
        ####################################################================
        delegate = AlignDelegate(self.tableWidget)
        self.tableWidget.setItemDelegate(delegate)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(215)
        self.horizontalLayout_8.addWidget(self.tableWidget)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout_6.addWidget(self.frame)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.verticalLayout_18.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.Container)
        self.verticalLayout.addWidget(self.Body)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("QStatusBar {\n"
"    background-color: rgb(10, 11, 12);\n"
"}")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Deposit"))
        self.label.setText(_translate("MainWindow", "Loan Management System"))
        self.label_2.setText(_translate("MainWindow", "Add Deposit"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Search By"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Name"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Biometric"))
        self.label_3.setText(_translate("MainWindow", "Enter Deposit Amount "))
        self.pushButton_3.setText(_translate("MainWindow", "Search Record"))
        self.pushButton_4.setText(_translate("MainWindow", "Add Deposit"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "User id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Amt"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "F. Name"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Location"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Weight"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Deposit"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "    Deposit Date"))
import resources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow5()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
