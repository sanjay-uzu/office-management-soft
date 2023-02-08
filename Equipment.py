import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap, QIcon
from PyQt5.QtWidgets import *
import sqlite3
import Feedback
import Meetings
import Account
import MainEmp
import MainAdm
import Admin
import data
import seat
import date
con = sqlite3.connect('equipment.db')
cur = con.cursor()


class Equipment(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 2000, 1000)
        self.setWindowTitle("Employee Main")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.photo = QLabel(self)
        self.setStyleSheet("QWidget{background:#fef2da;font-size:12pt;}QLineEdit{background:#fffbf4;border-radius:10px}QComboBox{background:white;border-radius:10px}QTableWidget{background:white;border-radius:10px}QListWidget{background:white;border-radius:10px}")
        self.photo.resize(QSize(300, 300))
        self.photo.setPixmap(QPixmap("Data/Equip Default.png").scaled(300, 300))
        self.photo.move(1000+170, 0)
        self.locationlbl = QLabel("Location:", self)
        self.description = QLabel("Description:", self)
        self.destext = QTextEdit(self)
        self.destext.setStyleSheet("background:white;border-radius:10px")
        self.name = QLabel("Name:", self)
        self.nams = QLineEdit(self)
        self.location = QLineEdit(self)
        self.name.move(1000+170, 323)
        self.nams.move(1090+170, 323)
        self.locationlbl.move(1000+170, 353)
        self.location.move(1090+170, 353)
        self.location.setMinimumWidth(250)
        self.nams.setMinimumWidth(250)
        self.description.move(1000+170, 383)
        self.destext.move(1000+170, 410)
        self.destext.resize(QSize(400, 500))
        self.eqplbl = QLabel("Equipment:", self)
        self.eqplbl.move(100, 220+110-250)
        self.srch = QLineEdit(self)
        self.srch.setPlaceholderText("Enter Equipment Name to Search")
        self.srch.resize(QSize(600+57+170, 50))
        self.srch.move(100, 260+110-250)
        self.srcbtn = QToolButton(self)
        self.srcbtn.setIcon(QIcon("Data/search.png"))
        self.srcbtn.setIconSize(QSize(40,40))
        self.srcbtn.resize(QSize(40, 40))
        self.srcbtn.setStyleSheet("background-color:transparent ;border-style:outset ")
        self.srcbtn.move(700+57+170, 260+110-250)
        self.srcbtn.clicked.connect(self.search)
        self.equiplist = QListWidget(self)
        self.equiplist.move(100, 300+110-250)
        self.equiplist.resize(QSize(700+170, 500+250))
        self.equiplist.itemClicked.connect(self.singleClicks)
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
        self.bookbtn.clicked.connect(self.book)
        self.helpbtn = QToolButton(self)
        self.helpbtn.setIcon(QIcon("Data/help.png"))
        self.helpbtn.setIconSize(QSize(225, 75))
        self.helpbtn.resize(QSize(225, 75))
        self.helpbtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.helpbtn.move(1751, 946 - 30)
        self.helpbtn.clicked.connect(self.help)
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
        op3 = QGraphicsOpacityEffect(self)
        op3.setOpacity(0.3)
        self.feedbtn.setGraphicsEffect(op)
        self.feedbtn.setAutoFillBackground(True)
        self.accntbtn.setGraphicsEffect(op1)
        self.accntbtn.setAutoFillBackground(True)
        self.seatbtn.setGraphicsEffect(op2)
        self.seatbtn.setAutoFillBackground(True)
        self.bookbtn.setGraphicsEffect(op3)
        self.bookbtn.setAutoFillBackground(True)
        self.getEquipment()
        self.imageComputer2 = QLabel(self)
        self.helpbtn = QToolButton(self)
        self.helpbtn.setIcon(QIcon("Data/help.png"))
        self.helpbtn.setIconSize(QSize(225, 75))
        self.helpbtn.resize(QSize(225, 75))
        self.helpbtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.helpbtn.move(1751, 946 - 30)
        self.helpbtn.clicked.connect(self.help)
        self.helpbtn1 = QToolButton(self)
        self.helpbtn1.setIcon(QIcon("Data/Home@2x.png"))
        self.helpbtn1.setIconSize(QSize(75, 75))
        self.helpbtn1.resize(QSize(75, 75))
        self.helpbtn1.setStyleSheet("background-color:transparent ; border-style:outset")
        self.helpbtn1.move(1751 - 40, 946 - 30)
        self.helpbtn1.clicked.connect(self.home)
        self.i = 0
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
            self.imageComputer2.setPixmap(QPixmap("Data/Equip Help.png").scaled(756, 1029))
            self.imageComputer2.resize(756,1029)
            self.imageComputer2.move(498,33)
            self.imageComputer2.setStyleSheet("background:transparent")
            self.i=1
            print("in")
        else:
            self.imageComputer2.setPixmap(QPixmap("Data/Equip Help@2x.png").scaled(3840 / 2, 2080 / 2))
            self.imageComputer2.resize(0, 0)
            self.i=0
    def singleClicks(self):
        value = self.equiplist.currentItem().text()
        id = self.getid(value)
        query = ("SELECT * FROM equipment WHERE id=?")
        person = cur.execute(query, (id,)).fetchone()
        self.nams.setText(person[0])
        self.location.setText(person[3])
        self.destext.setText(person[4])
        self.photo.setPixmap(QPixmap(person[2]).scaled(300, 300))

    def getid(self, person):
        query = "SELECT id,name,location,photo,description FROM equipment"
        employees = cur.execute(query).fetchall()
        for employee in employees:
            if person == employee[1]:
                return employee[0]


    def getEquipment(self):
        query = "SELECT id,name,location,photo,description FROM equipment"
        employees = cur.execute(query).fetchall()
        for employee in employees:
            self.equiplist.addItem(employee[1])

    def search(self):
        value = self.srch.text()
        count = self.equiplist.count()
        print(count)
        if value == "":
            QMessageBox.information(self, "Warning!!!", "Please type something to search")
        else:
            self.srch.setText("")

            query = (
                "SELECT id,name FROM equipment WHERE name LIKE ?")
            results = cur.execute(query, ('%' + value + '%',)).fetchall()
            print(results)

            if results == []:
                QMessageBox.information(self, "Warning", "There is no such Equipment")

            else:
                self.equiplist.clear()
                for employee in results:
                    self.equiplist.addItem(employee[1])

    def book(self):
        self.book=Meetings.Meetings()
        self.close()
    def feedbacks(self):
        self.feed=Feedback.Feedbacks()
        self.close()
    def accnt(self):
        if data.type==1:
            self.accnt=Admin.admin()
            self.close()
        else:
            self.accnt=Account.Accnt()
            self.close()


    def seats(self):
        self.seatts = date.date()
        self.close()