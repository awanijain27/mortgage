# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'removed_record.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from tkinter import messagebox
import mysql.connector
import resources

class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter

class Ui_MainWindow2(object):
    def connect2db(self):
        self.con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shailesh@123",
        database="loan_management",
        auth_plugin="caching_sha2_password" 
        )
    def search_data(self):
        current = self.comboBox_removed.currentText()
        if current == "Search By":
              messagebox.showerror("Error","PLease choose either name,location or date")
        elif current == "By Location":
              try:
                        self.connect2db()
                        mycursor = self.con.cursor()
                        if self.lineEdit_removed.text() == "":
                              messagebox.showerror("Error","Please enter location")
                        else:
                                location = self.lineEdit_removed.text()
                                query = "SELECT * FROM removed_records WHERE location = %s"
                                values = (location,)
                                mycursor.execute(query, values)

                        
                                result = mycursor.fetchall()
                        
                                self.tableWidget_removed.setRowCount(0)
                        
                                for row_number, row_data in enumerate(result):
                                        self.tableWidget_removed.insertRow(row_number)
                        
                                        for column_number, data in enumerate(row_data):
                                                self.tableWidget_removed.setItem(row_number,
                                                        column_number, QTableWidgetItem(str(data)))
                
              except Exception as e:
                        messagebox.showerror("Error",f"Error due to {str(e)}")
        elif current == "By Date":
              try:
                        self.connect2db()
                        mycursor = self.con.cursor()
                        if self.lineEdit_removed.text() == "":
                              messagebox.showerror("Error","Please enter date")
                        else:
                                date = self.lineEdit_removed.text()
                                query = "SELECT * FROM removed_records WHERE date = %s"
                                values = (date,)
                                mycursor.execute(query, values)

                        
                                result = mycursor.fetchall()
                        
                                self.tableWidget_removed.setRowCount(0)
                        
                                for row_number, row_data in enumerate(result):
                                        self.tableWidget_removed.insertRow(row_number)
                        
                                        for column_number, data in enumerate(row_data):
                                                self.tableWidget_removed.setItem(row_number,
                                                        column_number, QTableWidgetItem(str(data)))
                
              except Exception as e:
                        messagebox.showerror("Error",f"Error due to {str(e)}")
        elif current == "By Name": 
                try:
                        self.connect2db()
                        mycursor = self.con.cursor()
                        if self.lineEdit_removed.text() == "":
                              messagebox.showerror("Error","Please enter Name")
                        else:
                                name = self.lineEdit_removed.text()
                                query = "SELECT * FROM removed_records WHERE name = %s"
                                values = (name,)
                                mycursor.execute(query, values)

                        
                                result = mycursor.fetchall()
                        
                                self.tableWidget_removed.setRowCount(0)
                        
                                for row_number, row_data in enumerate(result):
                                        self.tableWidget_removed.insertRow(row_number)
                        
                                        for column_number, data in enumerate(row_data):
                                                self.tableWidget_removed.setItem(row_number,
                                                        column_number, QTableWidgetItem(str(data)))
                
                except Exception as e:
                        messagebox.showerror("Error",f"Error due to {str(e)}")
        else:
              messagebox.showerror("Error","Something Unexpected Occur")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 892)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/resources/icons/removed_record.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_9 = QtWidgets.QFrame(self.page_2)
        self.frame_9.setStyleSheet("background-color: rgb(175,175,175);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setStyleSheet("border:none;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_11 = QtWidgets.QFrame(self.frame_10)
        self.frame_11.setStyleSheet("border:none;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.frame_11)
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setStyleSheet("font: 24pt \"Segoe UI\";\n"
"font: 9pt \"Segoe UI\";\n"
"font: 550 48pt \"Segoe UI\";\n"
"border: 2px solid black;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        self.verticalLayout_8.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_10)
        self.frame_12.setStyleSheet("\n"
"border:none;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        self.frame_13.setStyleSheet("border:none;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.comboBox_removed = QtWidgets.QComboBox(self.frame_13)
        self.comboBox_removed.setMinimumSize(QtCore.QSize(327, 0))
        self.comboBox_removed.setStyleSheet("border: 2px solid black;\n"
"font: 15pt \"Segoe UI\";\n"
"")
        self.comboBox_removed.setObjectName("comboBox_removed")
        self.comboBox_removed.addItem("")
        self.comboBox_removed.addItem("")
        self.comboBox_removed.addItem("")
        self.comboBox_removed.addItem("")
        self.verticalLayout_9.addWidget(self.comboBox_removed, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_10.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_12)
        self.frame_14.setStyleSheet("border:none;")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lineEdit_removed = QtWidgets.QLineEdit(self.frame_14)
        self.lineEdit_removed.setStyleSheet("border: 2px solid black;\n"
"font: 16pt \"Segoe UI\";")
        self.lineEdit_removed.setObjectName("lineEdit_removed")
        self.horizontalLayout_11.addWidget(self.lineEdit_removed)
        self.horizontalLayout_10.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_12)
        self.frame_15.setStyleSheet("border:none;")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_removed = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_removed.setMinimumSize(QtCore.QSize(200, 45))
        self.pushButton_removed.setMaximumSize(QtCore.QSize(200, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_removed.setFont(font)
        self.pushButton_removed.setStyleSheet("border: 2px solid black;\n"
"font: 15pt \"Segoe UI\";\n"
"background-color: rgb(3, 53, 127);\n"
"border-radius: 5px")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/icons8_todo_list.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_removed.setIcon(icon2)
        self.pushButton_removed.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_removed.setObjectName("pushButton_removed")
        self.verticalLayout_10.addWidget(self.pushButton_removed)
        self.pushButton_removed.clicked.connect(self.search_data)
        self.horizontalLayout_10.addWidget(self.frame_15)
        self.verticalLayout_8.addWidget(self.frame_12)
        self.verticalLayout_7.addWidget(self.frame_10)
        self.frame_16 = QtWidgets.QFrame(self.frame_9)
        self.frame_16.setStyleSheet("border:none;")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.tableWidget_removed = QtWidgets.QTableWidget(self.frame_16)
        self.tableWidget_removed.setStyleSheet("border: 2px solid black;")
        self.tableWidget_removed.setObjectName("tableWidget_removed")
        self.tableWidget_removed.setStyleSheet("QTableWidget {font-size: 30px;}")
        self.tableWidget_removed.verticalHeader().setDefaultAlignment(Qt.AlignCenter)
        ####################################################================
        delegate = AlignDelegate(self.tableWidget_removed)
        self.tableWidget_removed.setItemDelegate(delegate)
        ###################################################============================
        self.tableWidget_removed.setColumnCount(10)
        self.tableWidget_removed.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_removed.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_removed.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_removed.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_removed.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_removed.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_removed.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_removed.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_removed.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_removed.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_removed.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_removed.setHorizontalHeaderItem(10, item)
        self.tableWidget_removed.horizontalHeader().setDefaultSectionSize(218)
        self.horizontalLayout_12.addWidget(self.tableWidget_removed)
        self.verticalLayout_7.addWidget(self.frame_16)
        self.horizontalLayout_5.addWidget(self.frame_9)
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
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "View Removed Records"))
        self.label.setText(_translate("MainWindow", "Loan Management System"))
        self.label_3.setText(_translate("MainWindow", "View Removed Record"))
        self.comboBox_removed.setItemText(0, _translate("MainWindow", "Search By"))
        self.comboBox_removed.setItemText(1, _translate("MainWindow", "By Name"))
        self.comboBox_removed.setItemText(2, _translate("MainWindow", "By Date"))
        self.comboBox_removed.setItemText(3, _translate("MainWindow", "By Location"))
        self.pushButton_removed.setText(_translate("MainWindow", "Search Record"))
        item = self.tableWidget_removed.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "User_id"))
        item = self.tableWidget_removed.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Amt"))
        item = self.tableWidget_removed.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_removed.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "F.Name"))
        item = self.tableWidget_removed.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Location"))
        item = self.tableWidget_removed.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget_removed.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Removed Date"))
        item = self.tableWidget_removed.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tableWidget_removed.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Weight"))
        item = self.tableWidget_removed.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Interest"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
