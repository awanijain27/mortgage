# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DashBoard.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox
from PyQt5.QtGui import QIcon
from add_record import Ui_MainWindow
from removed_record import Ui_MainWindow2
from remove_record import Ui_MainWindow3
from view_record import Ui_MainWindow4
from add_deposit import Ui_MainWindow5
from datetime import date, timedelta
import mysql.connector
import resources


class Ui_MainWindow1(object):
    
    # function to connect to a database
    def connect2db(self):
        self.con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shailesh@123",
        database="loan_management",
        auth_plugin="caching_sha2_password" 
        )

    # function to create a list of dates of past 10 days
    def get_past_10_dates(self):
        # Get the current date
        current_date = date.today()

        # Create a list to store the dates
        date_list = []

        # Loop to generate the past 10 dates
        for i in range(10):
                # Subtract 'i' days from the current date
                past_date = current_date - timedelta(days=i)
                # Append the date part as a string to the list
                date_list.append(past_date.strftime("%d-%m"))

        return date_list
    
    # function to extract interest for past 10 days on daily basis
    def sum_amount(self):
        self.connect2db()
        # Create a cursor to execute SQL queries
        cursor = self.con.cursor()

        # Construct the query to sum amounts grouped by date for the past 10 days
        query = """
                SELECT
    IFNULL(SUM(removed_records.interest), 0) AS total_interest
FROM
    (
        SELECT CURDATE() AS date
        UNION ALL
        SELECT CURDATE() - INTERVAL 1 DAY
        UNION ALL
        SELECT CURDATE() - INTERVAL 2 DAY
        UNION ALL
        SELECT CURDATE() - INTERVAL 3 DAY
        UNION ALL
        SELECT CURDATE() - INTERVAL 4 DAY
        UNION ALL
        SELECT CURDATE() - INTERVAL 5 DAY
        UNION ALL
        SELECT CURDATE() - INTERVAL 6 DAY
        UNION ALL
        SELECT CURDATE() - INTERVAL 7 DAY
        UNION ALL
        SELECT CURDATE() - INTERVAL 8 DAY
        UNION ALL
        SELECT CURDATE() - INTERVAL 9 DAY
    ) AS calendar
LEFT JOIN
    removed_records ON calendar.date = DATE(removed_records.removed_date)
GROUP BY
    calendar.date;

        """

        # Execute the query
        cursor.execute(query)

        # Fetch all the results
        results = cursor.fetchall()

        # Get the sum amounts as a list
        sum_amounts = [row[0] for row in results]

        # Close the cursor and the database connection
        cursor.close()
        self.con.close()

        return sum_amounts
    
    # function for refreshing dashboard
    def refresh_dashboard(self):
        self.plotoncanvas()
        self.statistics()
    # function to close dashboard
    def close(self):
        self.close()
    # integrating add record ui
    def add_record(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.destroyed.connect(self.refresh_dashboard)
        self.window.show()

    # integrating removed record ui
    def removed_record(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self.window)
        self.window.show()

    # integrating remove record ui
    def remove_record(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self.window)
        self.window.show()

    # integrating view record ui
    def view_record(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow4()
        self.ui.setupUi(self.window)
        self.window.show()

    # integrating add deposit ui
    def add_deposit(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow5()
        self.ui.setupUi(self.window)
        self.window.show()

    ### creating statistics function to extract realtime data
    def statistics(self):
        self.connect2db()
        mycursor = self.con.cursor()
        #executing query for total investment
        query = "select sum(amount) from all_records"
        mycursor.execute(query)
        total_i = mycursor.fetchone()
        total_i = str(total_i[0])
        self.total_investment.setText(f"[ {total_i}]")
        #executing query for todays investment
        query = "select sum(amount) from all_records where date = curdate()"
        mycursor.execute(query)
        total_i = mycursor.fetchone()
        total_i = str(total_i[0])
        if total_i == "None":
            self.todays_investment.setText(f"[ {str(0)} ]")
        else:
                self.todays_investment.setText(f"[ {total_i} ]")
        #executing query for todays return including interest
        query = " select sum(amount+interest) from removed_records where removed_date = curdate();"
        mycursor.execute(query)
        total_i = mycursor.fetchone()
        total_i = str(total_i[0])
        if total_i == "None":
            self.todays_return.setText(f"[ {str(0)} ]")
        else:
                self.todays_return.setText(f"[ {total_i} ]")
        #executing query for todays interest
        query = " select sum(interest) from removed_records where removed_date = curdate();"
        mycursor.execute(query)
        total_i = mycursor.fetchone()
        total_i = str(total_i[0])
        if total_i == "None":
            self.todays_earnings.setText(f"[ {str(0)} ]")
        else:
                self.todays_earnings.setText(f"[ {total_i} ]")
        
    # function to create a graph 
    def plotoncanvas(self):
        self.figure.clear()
        self.figure.patch.set_facecolor("grey")
        #creating dates and amount data series
        dates = self.get_past_10_dates()
        dates = dates[::-1]
        amounts = self.sum_amount()
        amount = [int(amount) for amount in amounts]
        amount = amount[::-1]
        #create the bar plot
        plt.bar(dates,amount, color="black")
        
        plt.xlabel("Past 10 Days")
        plt.ylabel("Amount")
        plt.title("Total Earnings of Past 10 Days")
        
        #refresh canvas
        self.canvas.draw()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1907, 950)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/resources/icons/download.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.label.setStyleSheet("color: rgb(176, 176, 176);\n"
                                 "font: 11pt")
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
        self.toggleButton_7 = QtWidgets.QPushButton(self.userFrame)
        self.toggleButton_7.setMinimumSize(QtCore.QSize(90, 26))
        self.toggleButton_7.setMaximumSize(QtCore.QSize(90, 26))
        font = QtGui.QFont()
        font.setBold(True)
        self.toggleButton_7.setFont(font)
        self.toggleButton_7.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgb(30, 30, 30);\n"
"    border-left: 3px solid rgb(30, 30, 30);\n"
"    border-right: 3px solid rgb(30, 30, 30);\n"
"    color: rgb(255, 85, 0);\n"
"    border-radius: 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-left: 3px solid rgb(255, 85, 0);\n"
"    border-right: 3px solid rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(25, 25, 25);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("::/resources/resources/icons/refresh.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toggleButton_7.setIcon(icon1)
        self.toggleButton_7.setIconSize(QtCore.QSize(25, 25))
        self.toggleButton_7.setObjectName("toggleButton_7")
        self.toggleButton_7.clicked.connect(self.refresh_dashboard)
        self.horizontalLayout_4.addWidget(self.toggleButton_7)
        self.toggleButton_81 = QtWidgets.QPushButton(self.userFrame)
        self.toggleButton_81.setMinimumSize(QtCore.QSize(90, 26))
        self.toggleButton_81.setMaximumSize(QtCore.QSize(90, 26))
        font = QtGui.QFont()
        font.setBold(True)
        self.toggleButton_81.setFont(font)
        self.toggleButton_81.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgb(30, 30, 30);\n"
"    border-left: 3px solid rgb(30, 30, 30);\n"
"    border-right: 3px solid rgb(30, 30, 30);\n"
"    color: rgb(255, 85, 0);\n"
"    border-radius: 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-left: 3px solid rgb(255, 85, 0);\n"
"    border-right: 3px solid rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(25, 25, 25);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("::/resources/resources/icons/refresh.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toggleButton_81.setIcon(icon1)
        self.toggleButton_81.setIconSize(QtCore.QSize(25, 25))
        self.toggleButton_81.setObjectName("toggleButton_7")
        self.toggleButton_81.clicked.connect(self.close)
        self.horizontalLayout_4.addWidget(self.toggleButton_81)
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
        self.leftMenu = QtWidgets.QFrame(self.Body)
        self.leftMenu.setMinimumSize(QtCore.QSize(43, 0))
        self.leftMenu.setMaximumSize(QtCore.QSize(200, 16777215))
        self.leftMenu.setStyleSheet("background-color: rgb(100,100,120);")
        self.leftMenu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.leftMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftMenu.setObjectName("leftMenu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftMenu)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.leftMenu)
        self.frame_5.setStyleSheet("image: url(:/resources/resources/images/loanmate1.png);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2.addWidget(self.frame_5)
        self.aframe = QtWidgets.QFrame(self.leftMenu)
        self.aframe.setMinimumSize(QtCore.QSize(200, 225))
        self.aframe.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.aframe.setObjectName("aframe")
        self.pushButton_removed = QtWidgets.QPushButton(self.aframe)
        self.pushButton_removed.setGeometry(QtCore.QRect(0, 210, 200, 45))
        self.pushButton_removed.setMinimumSize(QtCore.QSize(200, 45))
        self.pushButton_removed.setMaximumSize(QtCore.QSize(200, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_removed.setFont(font)
        self.pushButton_removed.setStyleSheet("QPushButton {\n"
"    font: 13pt \"Segoe UI\";\n"
"    background-color: rgb(25, 25, 25);\n"
"    color: rgb(154, 154, 149);\n"
"    border: 1px solid black;\n"
"    border-left: 3px solid rgb(25, 25, 25);\n"
"    text-align: left;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-left: 3px solid rgb(255, 85, 0);\n"
"    background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.pushButton_removed.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_removed.setObjectName("pushButton_removed")
        self.pushButton_removed.clicked.connect(self.removed_record)
        self.pushButton_view = QtWidgets.QPushButton(self.aframe)
        self.pushButton_view.setGeometry(QtCore.QRect(0, 140, 200, 45))
        self.pushButton_view.setMinimumSize(QtCore.QSize(200, 45))
        self.pushButton_view.setMaximumSize(QtCore.QSize(200, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_view.setFont(font)
        self.pushButton_view.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Segoe UI\";\n"
"    background-color: rgb(25, 25, 25);\n"
"    color: rgb(154, 154, 149);\n"
"    border: 1px solid black;\n"
"    border-left: 3px solid rgb(25, 25, 25);\n"
"    text-align: left;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-left: 3px solid rgb(255, 85, 0);\n"
"    background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/icons8_mastercard_credit_card.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_view.setIcon(icon3)
        self.pushButton_view.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_view.setObjectName("pushButton_view")
        self.pushButton_view.clicked.connect(self.view_record)
        self.pushButton_remove = QtWidgets.QPushButton(self.aframe)
        self.pushButton_remove.setGeometry(QtCore.QRect(0, 70, 200, 45))
        self.pushButton_remove.setMinimumSize(QtCore.QSize(200, 45))
        self.pushButton_remove.setMaximumSize(QtCore.QSize(200, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_remove.setFont(font)
        self.pushButton_remove.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Segoe UI\";\n"
"    background-color: rgb(25, 25, 25);\n"
"    color: rgb(154, 154, 149);\n"
"    border: 1px solid black;\n"
"    border-left: 3px solid rgb(25, 25, 25);\n"
"    text-align: left;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-left: 3px solid rgb(255, 85, 0);\n"
"    background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/icons8_secured_letter.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_remove.setIcon(icon4)
        self.pushButton_remove.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.pushButton_remove.clicked.connect(self.remove_record)
        self.pushButton_add = QtWidgets.QPushButton(self.aframe)
        self.pushButton_add.setGeometry(QtCore.QRect(0, 0, 200, 45))
        self.pushButton_add.setMinimumSize(QtCore.QSize(200, 45))
        self.pushButton_add.setMaximumSize(QtCore.QSize(200, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setStyleSheet("QPushButton {\n"
"    font: 13pt \"Segoe UI\";\n"
"    background-color: rgb(25, 25, 25);\n"
"    color: rgb(154, 154, 149);\n"
"    border: 1px solid black;\n"
"    border-left: 3px solid rgb(25, 25, 25);\n"
"    text-align: left;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-left: 3px solid rgb(255, 85, 0);\n"
"    background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.pushButton_add.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_add.clicked.connect(self.add_record)
        self.pushButton_deposit = QtWidgets.QPushButton(self.aframe)
        self.pushButton_deposit.setGeometry(QtCore.QRect(0, 280, 200, 45))
        self.pushButton_deposit.setMinimumSize(QtCore.QSize(200, 45))
        self.pushButton_deposit.setMaximumSize(QtCore.QSize(200, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_deposit.setFont(font)
        self.pushButton_deposit.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Segoe UI\";\n"
"    background-color: rgb(25, 25, 25);\n"
"    color: rgb(154, 154, 149);\n"
"    border: 1px solid black;\n"
"    border-left: 3px solid rgb(25, 25, 25);\n"
"    text-align: left;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-left: 3px solid rgb(255, 85, 0);\n"
"    background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.pushButton_deposit.setIcon(icon3)
        self.pushButton_deposit.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_deposit.setObjectName("pushButton_deposit")
        self.pushButton_deposit.clicked.connect(self.add_deposit)
        self.verticalLayout_2.addWidget(self.aframe)
        self.frame_2 = QtWidgets.QFrame(self.leftMenu)
        self.frame_2.setStyleSheet("border: none;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 3)
        self.horizontalLayout.addWidget(self.leftMenu)
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
        self.frame.setStyleSheet("background-color: rgb(150,150,150);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("border: none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setStyleSheet("border: none;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_12 = QtWidgets.QFrame(self.frame_7)
        self.frame_12.setStyleSheet("QFrame {\n"
"    background-color: rgb(25, 25, 25);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border: 1px solid rgb(255, 85, 0);\n"
"}")
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_10.setContentsMargins(0, 20, 0, 20)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_14 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("QLabel {\n"
"    font: 20pt \"Segoe UI\";\n"
"    color: rgb(152, 152, 152);\n"
"    border: none;\n"
"}")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_10.addWidget(self.label_14)
        self.total_investment = QtWidgets.QLineEdit(self.frame_12)
        self.total_investment.setStyleSheet("font: 20pt \"Segoe UI\";\n"
"background-color: rgb(25, 25, 25);\n"
"color: rgb(255,255,255)")
        self.total_investment.setAlignment(QtCore.Qt.AlignCenter)
        self.total_investment.setObjectName("total_investment")
        self.verticalLayout_10.addWidget(self.total_investment, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_6.addWidget(self.frame_12)
        self.horizontalLayout_5.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setStyleSheet("border: none;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_13 = QtWidgets.QFrame(self.frame_8)
        self.frame_13.setStyleSheet("QFrame {\n"
"    background-color: rgb(25, 25, 25);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border: 1px solid rgb(255, 85, 0);\n"
"}")
        self.frame_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_12.setContentsMargins(0, 20, 0, 20)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_22 = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("QLabel {\n"
"    font: 20pt \"Segoe UI\";\n"
"    color: rgb(152, 152, 152);\n"
"    border: none;\n"
"}")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_12.addWidget(self.label_22)
        self.todays_investment = QtWidgets.QLineEdit(self.frame_13)
        self.todays_investment.setStyleSheet("font: 20pt \"Segoe UI\";\n"
"background-color: rgb(25, 25, 25);\n"
"color: rgb(255,255,255)")
        self.todays_investment.setAlignment(QtCore.Qt.AlignCenter)
        self.todays_investment.setObjectName("todays_investment")
        self.verticalLayout_12.addWidget(self.todays_investment, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_4.addWidget(self.frame_13)
        self.horizontalLayout_5.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_3)
        self.frame_9.setStyleSheet("border: none;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_14 = QtWidgets.QFrame(self.frame_9)
        self.frame_14.setStyleSheet("QFrame {\n"
"    background-color: rgb(25, 25, 25);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border: 1px solid rgb(255, 85, 0);\n"
"}")
        self.frame_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_13.setContentsMargins(0, 20, 0, 20)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_26 = QtWidgets.QLabel(self.frame_14)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("QLabel {\n"
"    font: 20pt \"Segoe UI\";\n"
"    color: rgb(152, 152, 152);\n"
"    border: none;\n"
"}")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_13.addWidget(self.label_26)
        self.todays_return = QtWidgets.QLineEdit(self.frame_14)
        self.todays_return.setStyleSheet("font: 20pt \"Segoe UI\";\n"
"background-color: rgb(25, 25, 25);\n"
"color: rgb(255,255,255)")
        self.todays_return.setAlignment(QtCore.Qt.AlignCenter)
        self.todays_return.setObjectName("todays_return")
        self.verticalLayout_13.addWidget(self.todays_return, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_5.addWidget(self.frame_14)
        self.horizontalLayout_5.addWidget(self.frame_9)
        self.frame_11 = QtWidgets.QFrame(self.frame_3)
        self.frame_11.setStyleSheet("border: none;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_15 = QtWidgets.QFrame(self.frame_11)
        self.frame_15.setStyleSheet("QFrame {\n"
"    background-color: rgb(25, 25, 25);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border: 1px solid rgb(255, 85, 0);\n"
"}")
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_14.setContentsMargins(0, 20, 0, 20)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_30 = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("QLabel {\n"
"    font: 20pt \"Segoe UI\";\n"
"    color: rgb(152, 152, 152);\n"
"    border: none;\n"
"}")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_14.addWidget(self.label_30)
        self.todays_earnings = QtWidgets.QLineEdit(self.frame_15)
        self.todays_earnings.setStyleSheet("font: 20pt \"Segoe UI\";\n"
"background-color: rgb(25, 25, 25);\n"
"color: rgb(255,255,255)")
        self.todays_earnings.setAlignment(QtCore.Qt.AlignCenter)
        self.todays_earnings.setObjectName("todays_earnings")
        self.verticalLayout_14.addWidget(self.todays_earnings, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_7.addWidget(self.frame_15)
        self.horizontalLayout_5.addWidget(self.frame_11)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setStyleSheet("border:none;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_6.setStyleSheet("background-color: rgb(18, 18, 18);")
        #### create a horizontal layout
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        ##Canvas here
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        ##end of canvas
        ##add canvas
        self.horizontalLayout_1.addWidget(self.canvas)
        ##end of horizontal layout
        self.horizontalLayout_7.addWidget(self.frame_6)
        self.frame_10 = QtWidgets.QFrame(self.frame_4)
        self.frame_10.setStyleSheet("border:none;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")



        self.horizontalLayout_7.addWidget(self.frame_10)
        self.horizontalLayout_7.setStretch(0, 8)
        self.horizontalLayout_7.setStretch(1, 3)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.verticalLayout_3.setStretch(0, 3)
        self.verticalLayout_3.setStretch(1, 9)
        self.verticalLayout_6.addWidget(self.frame)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.page_3)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.page_4)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
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
        self.refresh_dashboard()
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DashBoard"))
        self.label.setText(_translate("MainWindow", "Loan Management System"))
        self.toggleButton_7.setText(_translate("MainWindow", "Refresh "))
        self.toggleButton_81.setText(_translate("MainWindow", "Close "))
        self.pushButton_removed.setText(_translate("MainWindow", "Removed Record"))
        self.pushButton_view.setText(_translate("MainWindow", "View Record"))
        self.pushButton_remove.setText(_translate("MainWindow", "Remove Record"))
        self.pushButton_add.setText(_translate("MainWindow", "Add Record"))
        self.pushButton_deposit.setText(_translate("MainWindow", "Add Deposit"))
        self.label_14.setText(_translate("MainWindow", "Total Investment"))
        self.label_22.setText(_translate("MainWindow", "Today\'s Investment"))
        self.label_26.setText(_translate("MainWindow", "Today\'s Return"))
        self.label_30.setText(_translate("MainWindow", "Today\'s Earnings"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.showFullScreen()
    sys.exit(app.exec_())