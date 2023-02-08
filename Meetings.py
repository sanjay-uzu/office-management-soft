import sqlite3

import MainAdm
import MainEmp
import seat
import Account
import Admin
import Feedback
import data
from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
import sys
import bookroom2
import Equipment
import date
con = sqlite3.connect('meetings.db')
cur = con.cursor()
from datetime import datetime

class QVLine(QFrame):
    def __init__(self):
        super(QVLine, self).__init__()
        self.setFrameShape(QFrame.VLine)
        self.setFrameShadow(QFrame.Sunken)
class Meetings(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 2000,1000)
        self.setWindowTitle("Meeting")
        self.setWindowFlag(Qt.FramelessWindowHint)


        self.schedulbl=QLabel("Schedule A Meeting Room",self)
        self.schedulbl.setStyleSheet("font-size:15pt")
        self.setStyleSheet("QWidget{background:#fef2da;font-size:12pt;}QLineEdit{background:#fffbf4;border-radius:10px}QComboBox{background:white;border-radius:10px}QTableWidget{background:white;border-radius:10px}QListWidget{background:white;border-radius:10px}")
        self.schedulbl.move(800,50)
        self.datelbl=QLabel("Select  Date:",self)
        self.datelbl.move(800,150)
        self.daylbl=QLabel("Day:",self)
        self.monthlbl=QLabel("Month:",self)
        self.yearlbl=QLabel("Year:",self)
        self.day=QComboBox(self)
        list1 = ["1-2", "2-5", "5-10", "10-20"]
        list2=["1","2","3","4","5","6","7","8","9","10","11","12"]
        for number in range(1,32):
            self.day.addItem(str(number))
        self.month=QComboBox(self)
        self.month.addItems(list2)
        self.year=QComboBox(self)
        now = datetime.now()
        self.date=str(now.strftime("%Y-%m-%d %H:%M:%S"))
        self.date=self.date.split()
        self.date=self.date[0]
        self.date = self.date.split('-')
        self.daycur=self.date[2]
        self.monthcur=self.date[1]
        self.yearcur=self.date[0]
        print(self.date)
        for number in range(2020,2022):
            self.year.addItem(str(number))
        self.day.setCurrentIndex(int(self.daycur)-1)
        self.month.setCurrentIndex(int(self.monthcur)-1)
        self.daylbl.move(800,180)
        self.monthlbl.move(910,180)
        self.yearlbl.move(1050,180)
        self.day.move(845,180)
        self.month.move(975,180)
        self.year.move(1105,180)
        self.day.setMinimumWidth(60)
        self.month.setMinimumWidth(70)
        self.year.setMinimumWidth(80)
        print(self.year.size())
        print(self.month.size())
        self.pplbl=QLabel("Select No. of people:",self)
        self.pplbl.move(800,110)
        self.showbtn=QToolButton(self)
        self.showbtn.setIcon(QIcon("Data/Search Rooms@2x.png"))
        self.showbtn.setIconSize(QSize(100,40))
        self.showbtn.resize(QSize(100,40))
        self.showbtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.showbtn.clicked.connect(self.show)
        self.showbtn.move(1200,175)
        self.combo = QComboBox(self)
        self.combo.move(990, 110)
        list1=["1-2","2-5","5-20"]
        for number in list1:
            self.combo.addItem((number))
        self.metinlbl=QLabel("Your Meetings:",self)
        self.metinlbl.move(50,210)
        self.metinglist=QTableWidget(self)
        self.metinglist.setRowCount(13)
        self.metinglist.setColumnCount(2)
        self.metinglist.setHorizontalHeaderItem(0, QTableWidgetItem("Date"))
        self.metinglist.setHorizontalHeaderItem(1, QTableWidgetItem("Time"))
        self.metinglist.resize(QSize(600,500))
        self.metinglist.move(50,300)
        self.metinglist.horizontalHeader().setStretchLastSection(True)
        self.metinglist.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.rmslbl = QLabel("Meetings Rooms(Select One):", self)
        self.rmslbl.move(800, 260)
        self.rmslist = QListWidget(self)
        self.rmslist.resize(QSize(600, 500))
        self.rmslist.move(800, 300)
        self.rmslist.itemClicked.connect(self.singleClicks)
        self.line=QFrame(self)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Plain)
        self.line.move(700,40)
        self.line.setFixedHeight(925)
        self.line.setStyleSheet("color:black")
        self.setGeometry(100, 100, 2000, 1000)
        self.setWindowTitle("Employee Main")
        self.seatbtn = QToolButton(self)
        self.seatbtn.setIcon(QIcon("Data/myseat.png"))
        self.seatbtn.setIconSize(QSize(225, 75))
        self.seatbtn.resize(QSize(240, 90))
        self.seatbtn.setStyleSheet(
            "QToolButton{background-color:transparent ; border-style:outset; border-radius:10px} QToolButton:hover{background:#fac34b;}")
        self.seatbtn.move(1680 - 8, 74 - 30)
        self.seatbtn.clicked.connect(self.seats)
        self.equipbtn = QToolButton(self)
        self.equipbtn.setIcon(QIcon("Data/equipment.png"))
        self.equipbtn.setIconSize(QSize(225, 75))
        self.equipbtn.resize(QSize(240, 90))
        self.equipbtn.setStyleSheet(
            "QToolButton{background-color:transparent ; border-style:outset; border-radius:10px} QToolButton:hover{background:#fac34b;}")
        self.equipbtn.move(1680 - 8, 293 - 30)
        self.equipbtn.clicked.connect(self.equipment)
        self.feedbtn = QToolButton(self)
        self.feedbtn.setIcon(QIcon("Data/feedback.png"))
        self.feedbtn.setIconSize(QSize(225, 75))
        self.feedbtn.resize(QSize(240, 90))
        self.feedbtn.setStyleSheet(
            "QToolButton{background-color:transparent ; border-style:outset; border-radius:10px} QToolButton:hover{background:#fac34b;}")
        self.feedbtn.move(1680 - 8, 401 - 30)
        self.feedbtn.clicked.connect(self.feedbacks)
        self.accntbtn = QToolButton(self)
        if data.type == 1:
            self.accntbtn.setIcon(QIcon("Data/Admin@2x.png"))
        else:
            self.accntbtn.setIcon(QIcon("Data/account.png"))
        self.accntbtn.setIconSize(QSize(225, 75))
        self.accntbtn.resize(QSize(240, 90))
        self.accntbtn.setStyleSheet(
            "QToolButton{background-color:transparent ; border-style:outset; border-radius:10px} QToolButton:hover{background:#fac34b;}")
        self.accntbtn.move(1680 - 8, 512 - 30)
        self.accntbtn.clicked.connect(self.accnt)
        self.bookbtn = QToolButton(self)
        self.bookbtn.setIcon(QIcon("Data/meetings.png"))
        self.bookbtn.setIconSize(QSize(225, 75))
        self.bookbtn.resize(QSize(240, 90))
        self.bookbtn.setStyleSheet(
            "QToolButton{background-color:transparent ; border-style:outset; border-radius:10px} QToolButton:hover{background:#fac34b;}")
        self.bookbtn.move(1680 - 8, 183 - 30)
        self.getmeetings()
        self.closebtn = QToolButton(self)
        self.closebtn.setIcon(QIcon("Data/close.png"))
        self.closebtn.setIconSize(QSize(41, 25))
        self.closebtn.resize(QSize(41, 25))
        self.closebtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.closebtn.move(1877, 0)
        self.closebtn.clicked.connect(self.close)
        self.minimbtn = QToolButton(self)
        self.minimbtn.setIcon(QIcon("Data/minimise.png"))
        self.minimbtn.setIconSize(QSize(41, 25))
        self.minimbtn.resize(QSize(41, 25))
        self.minimbtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.minimbtn.move(1834, 0)
        self.minimbtn.clicked.connect(self.showMinimized)
        op = QGraphicsOpacityEffect(self)
        op.setOpacity(0.3)
        op1 = QGraphicsOpacityEffect(self)
        op1.setOpacity(0.3)
        op2 = QGraphicsOpacityEffect(self)
        op2.setOpacity(0.3)
        op3= QGraphicsOpacityEffect(self)
        op3.setOpacity(0.3)
        self.feedbtn.setGraphicsEffect(op)
        self.feedbtn.setAutoFillBackground(True)
        self.accntbtn.setGraphicsEffect(op1)
        self.accntbtn.setAutoFillBackground(True)
        self.seatbtn.setGraphicsEffect(op2)
        self.seatbtn.setAutoFillBackground(True)
        self.equipbtn.setGraphicsEffect(op3)
        self.equipbtn.setAutoFillBackground(True)
        self.imageComputer2 = QLabel(self)
        self.helpbtn=QToolButton(self)
        self.helpbtn.setIcon(QIcon("Data/help.png"))
        self.helpbtn.setIconSize(QSize(225, 75))
        self.helpbtn.resize(QSize(225, 75))
        self.helpbtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.helpbtn.move(1751, 946 - 30)
        self.helpbtn.clicked.connect(self.help)
        self.helpbtn1 = QToolButton(self)
        self.helpbtn1 = QToolButton(self)
        self.helpbtn1.setIcon(QIcon("Data/Home@2x.png"))
        self.helpbtn1.setIconSize(QSize(75, 75))
        self.helpbtn1.resize(QSize(75, 75))
        self.helpbtn1.setStyleSheet("background-color:transparent ; border-style:outset")
        self.helpbtn1.move(1751 - 40, 946 - 30)
        self.helpbtn1.clicked.connect(self.home)
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.getmeetings)
        self.i=0

        self.showMaximized()
    def home(self):
        if data.type==1:
            self.adm=MainAdm.admmain()
        else:
            self.emp=MainEmp.empmain()
        self.close()
    def help(self):
        print("HI")
        if self.i==0:
            self.imageComputer2.setPixmap(QPixmap("Data/Meeting Help@2x.png").scaled(3840, 2080))
            self.imageComputer2.resize(2000,1030)
            self.i=1
            print("in")
        else:
            self.imageComputer2.setPixmap(QPixmap("Data/Meeting Help@2x.png").scaled(3840 / 2, 2080 / 2))
            self.imageComputer2.resize(0, 0)
            self.i=0
    def getmeetings(self):
        query = "SELECT date,meetin FROM meetings WHERE empid=?"
        employees = cur.execute(query,(data.id,)).fetchall()
        print(employees)
        i=0
        for employee in employees:
            self.metinglist.setItem(i, 0, QTableWidgetItem(employee[0]))
            self.metinglist.setItem(i, 1, QTableWidgetItem(employee[1]))
            i=i+1
    def show(self):
        item = self.combo.currentText()
        self.rmslist.clear()
        if item == "1-2":
            list3 = ["2 Person Room Number-1", "2 Person Room Number-2", "2 Person Room Number-3",
                     "2 Person Room Number-4", "2 Person Room Number-5"]
            self.rmslist.addItems(list3)
        if item == "2-5":
            list3 = ["5 Person Room Number-1", "5 Person Room Number-2"]
            self.rmslist.addItems(list3)
        if item == "5-20":
            list3 = ["20 Person Room Number-1"]
            self.rmslist.addItems(list3)
    def singleClicks(self):
        item=self.rmslist.currentItem().text()
        data.room=item
        day=self.day.currentText()
        month=self.month.currentText()
        year=self.year.currentText()
        data.date=str(day+"-"+month+"-"+year)
        print(data.date)
        self.books=bookroom2.book()
        self.getmeetings()
    def accnt(self):
        if data.type==1:
            self.accnt=Admin.admin()
            self.close()
        else:
            self.accnt=Account.Accnt()
            self.close()

    def equipment(self):
        self.eq = Equipment.Equipment()
        self.close()
    def feedbacks(self):
        self.feed=Feedback.Feedbacks()
        self.close()



    def seats(self):
        self.seatts = date.date()
        self.close()


