import sys

import MainAdm
import MainEmp
import data
import mvmdata
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap, QIcon
from PyQt5.QtWidgets import *
import seat
import officemap
import Addemp
import  AddEquipment
import Equipment
import Feedback
import Meetings

import  date
import newsfeed
class admin(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 2000,1000)
        self.setWindowTitle("Admin")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet("QWidget{background:#fef2da;font-size:12pt;}QLineEdit{background:#fffbf4;border-radius:10px}QComboBox{background:white;border-radius:10px}QTableWidget{background:white;border-radius:10px}QListWidget{background:white;border-radius:10px}QTextEdit{background:white;border-radius:10px}")
        self.destext1=QTextEdit(self)
        self.destext2=QTextEdit(self)
        self.destext3=QTextEdit(self)
        self.destext4=QTextEdit(self)
        self.destext5=QTextEdit(self)
        self.destext1.resize(400,100)
        self.destext1.setText("Check the movement collected using sensors here.")
        self.destext2.setText("Manage your employee data here ")
        self.destext3.setText("Feed your office Map here ")
        self.destext4.setText("Manage your Equipment data here")
        self.destext5.setText("Manage your News Feed data here")
        self.destext1.setReadOnly(True)
        self.destext2.setReadOnly(True)
        self.destext3.setReadOnly(True)
        self.destext4.setReadOnly(True)
        self.destext5.setReadOnly(True)
        self.destext1.move(350,110)
        self.destext2.resize(400, 100)
        self.destext2.move(350+800, 110)
        self.destext3.resize(400, 100)
        self.destext3.move(350, 110+450-150)
        self.destext4.resize(400, 100)
        self.destext4.move(350 + 800, 110+450-150)
        self.destext5.resize(400, 100)
        self.destext5.move(350,710)
        self.mvmdata=QToolButton(self)
        self.mvmdata.setIcon(QIcon("Data/movedata.png"))
        self.mvmdata.setIconSize(QSize(200,200))
        self.mvmdata.resize(QSize(200,200))
        self.mvmdata.setStyleSheet("QToolButton{background-color:transparent ; border-style:outset; border-radius:10px} QToolButton:hover{background:#7a6b49;}")
        self.mvmdata.move(100,100)
        self.mvmdata.clicked.connect(self.moves)
        self.emptable = QToolButton(self)
        self.emptable.setIcon(QIcon("Data/empdata.png"))
        self.emptable.setIconSize(QSize(200, 200))
        self.emptable.resize(QSize(200, 200))
        self.emptable.setStyleSheet("QToolButton{background-color:transparent ; border-style:outset; border-radius:10px} QToolButton:hover{background:#7a6b49;}")
        self.emptable.move(900, 100)
        self.emptable.clicked.connect(self.employee)
        self.map = QToolButton(self)
        self.map.setIcon(QIcon("Data/OfficeMap@2x.png"))
        self.map.setIconSize(QSize(200, 200))
        self.map.resize(QSize(200,200))
        self.map.setStyleSheet("QToolButton{background-color:transparent ; border-style:outset; border-radius:10px} QToolButton:hover{background:#7a6b49;}")
        self.map.move(100, 550-150)
        self.map.clicked.connect(self.maps)
        self.eqpmnt = QToolButton(self)
        self.eqpmnt.setIcon(QIcon("Data/equipments.png"))
        self.eqpmnt.setIconSize(QSize(200, 200))
        self.eqpmnt.resize(QSize(200, 200))
        self.eqpmnt.setStyleSheet("QToolButton{background-color:transparent ; border-style:outset; border-radius:10px} QToolButton:hover{background:#7a6b49;}")
        self.eqpmnt.move(900,550-150)
        self.eqpmnt.clicked.connect(self.equipment)
        self.feeds = QToolButton(self)
        self.feeds.setIcon(QIcon("Data/NewsFeed.png"))
        self.feeds.setIconSize(QSize(200, 200))
        self.feeds.resize(QSize(200, 200))
        self.feeds.setStyleSheet(
            "QToolButton{background-color:transparent ; border-style:outset; border-radius:10px} QToolButton:hover{background:#7a6b49;}")
        self.feeds.move(100, 700)
        self.feeds.clicked.connect(self.feedto)
        ##############################################################################################
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
        self.accntbtn.setIcon(QIcon("Data/Admin@2x.png"))
        self.accntbtn.setIconSize(QSize(225, 75))
        self.accntbtn.resize(QSize(240, 90))
        self.accntbtn.setStyleSheet(
            "QToolButton{background-color:transparent ; border-style:outset; border-radius:10px} QToolButton:hover{background:#fac34b;}")
        self.accntbtn.move(1680 - 8, 512 - 30)
        self.bookbtn = QToolButton(self)
        self.bookbtn.setIcon(QIcon("Data/meetings.png"))
        self.bookbtn.setIconSize(QSize(225, 75))
        self.bookbtn.resize(QSize(240, 90))
        self.bookbtn.setStyleSheet(
            "QToolButton{background-color:transparent ; border-style:outset; border-radius:10px} QToolButton:hover{background:#fac34b;}")
        self.bookbtn.move(1680 - 8, 183 - 30)
        self.bookbtn.clicked.connect(self.book)
        self.helpbtn1 = QToolButton(self)
        self.helpbtn1.setIcon(QIcon("Data/Home@2x.png"))
        self.helpbtn1.setIconSize(QSize(75, 75))
        self.helpbtn1.resize(QSize(75, 75))
        self.helpbtn1.setStyleSheet("background-color:transparent ; border-style:outset")
        self.helpbtn1.move(1751 - 40, 946 - 30)
        self.helpbtn1.clicked.connect(self.home)
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
        self.bookbtn.setGraphicsEffect(op1)
        self.bookbtn.setAutoFillBackground(True)
        self.seatbtn.setGraphicsEffect(op2)
        self.seatbtn.setAutoFillBackground(True)
        self.equipbtn.setGraphicsEffect(op3)
        self.equipbtn.setAutoFillBackground(True)
        self.showMaximized()
    def home(self):
        if data.type==1:
            self.adm=MainAdm.admmain()
        else:
            self.emp=MainEmp.empmain()
        self.close()
    def feedto(self):
        self.fed=newsfeed.offmain()
        self.close()
    def employee(self):
        self.addemp=Addemp.Addemp()
        self.close()
    def equipment(self):
        self.equipment=AddEquipment.Addequip()
        self.close()
    def book(self):
        self.book=Meetings.Meetings()
        self.close()
    def feedbacks(self):
        self.feed=Feedback.Feedbacks()
        self.close()
    def equipments(self):
        self.eq=Equipment.Equipment()
        self.close()
    def seats(self):
        self.seatts = date.date()
        self.close()

    def moves(self):
        self.mm=mvmdata.mvmdata()
        self.close()
    def maps(self):
        self.mmm=officemap.offmain()
        self.close()

