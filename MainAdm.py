import sqlite3
import sys
import Admin
from PyQt5.QtCore import QSize, Qt, QUrl
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap, QIcon
from PyQt5.QtWidgets import *
import Feedback
import data
import Meetings
import Equipment
import seat
con = sqlite3.connect('empolyee.db')
cur = con.cursor()
con1 = sqlite3.connect('newsfeed.db')
cur1 = con1.cursor()
from PyQt5.QtGui import QDesktopServices
import date
from PyQt5.QtCore import QTimer

class admmain(QWidget):
    def __init__(self):
        super().__init__()
        self.id=id
        self.i=0
        self.setGeometry(100, 100, 2000,1000)
        self.setWindowTitle("Admin Main")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.timer = QTimer()
        self.timer.setInterval(3000)
        self.timer.start()
        self.timer1 = QTimer()
        self.timer1.setInterval(10000)
        self.timer1.start()
        self.timer.timeout.connect(self.change)
        self.timer1.timeout.connect(self.changes)
        self.imageComputer = QLabel(self)
        self.setStyleSheet("QWidget{background:#fef2da;font-size:12pt;}QLineEdit{background:#fffbf4;border-radius:10px}QComboBox{background:white;border-radius:10px}QTableWidget{background:white;border-radius:10px}QListWidget{background:white;border-radius:10px}")
        self.imageComputer.setPixmap(QPixmap("Data/Plan.jpg").scaled(1644, 959))
        self.imageComputer.move(18,62-8)
        self.imageComputer1 = QLabel(self)
        self.imageComputer1.setPixmap(QPixmap("Data/Help Click.png").scaled(235, 236))
        self.imageComputer1.move(1676, 665)
        self.btn = QToolButton(self)
        self.btn.setIcon(QIcon())
        self.btn.setIconSize(QSize(50, 50))
        self.btn.resize(QSize(50, 50))
        self.btn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.btn.clicked.connect(self.gotolink)
        self.imageComputer2 = QLabel(self)
        self.seatbtn=QToolButton(self)
        self.seatbtn.setIcon(QIcon("Data/myseat.png"))
        self.seatbtn.setIconSize(QSize(225,75))
        self.seatbtn.resize(QSize(240,90))
        self.seatbtn.setStyleSheet("QToolButton{background-color:transparent ; border-style:outset; border-radius:10px} QToolButton:hover{background:#fac34b;}")
        self.seatbtn.move(1680-8,74-30)
        self.seatbtn.clicked.connect(self.seats)
        self.equipbtn = QToolButton(self)
        self.equipbtn.setIcon(QIcon("Data/equipment.png"))
        self.equipbtn.setIconSize(QSize(225,75))
        self.equipbtn.resize(QSize(240, 90))
        self.equipbtn.setStyleSheet("QToolButton{background-color:transparent ; border-style:outset; border-radius:10px} QToolButton:hover{background:#fac34b;}")
        self.equipbtn.move(1680-8,293-30)
        self.equipbtn.clicked.connect(self.equipment)
        self.feedbtn = QToolButton(self)
        self.feedbtn.setIcon(QIcon("Data/feedback.png"))
        self.feedbtn.setIconSize(QSize(225,75))
        self.feedbtn.resize(QSize(240, 90))
        self.feedbtn.setStyleSheet("QToolButton{background-color:transparent ; border-style:outset; border-radius:10px} QToolButton:hover{background:#fac34b;}")
        self.feedbtn.move(1680-8, 401-30)
        self.feedbtn.clicked.connect(self.feedbacks)
        self.accntbtn = QToolButton(self)
        self.accntbtn.setIcon(QIcon("Data/Admin@2x.png"))
        self.accntbtn.setIconSize(QSize(225,75))
        self.accntbtn.resize(QSize(240, 90))
        self.accntbtn.setStyleSheet("QToolButton{background-color:transparent ; border-style:outset; border-radius:10px} QToolButton:hover{background:#fac34b;}")
        self.accntbtn.move(1680-8, 512-30)
        self.accntbtn.clicked.connect(self.admin)
        self.bookbtn = QToolButton(self)
        self.bookbtn.setIcon(QIcon("Data/meetings.png"))
        self.bookbtn.setIconSize(QSize(225,75))
        self.bookbtn.resize(QSize(240, 90))
        self.bookbtn.setStyleSheet("QToolButton{background-color:transparent ; border-style:outset; border-radius:10px} QToolButton:hover{background:#fac34b;}")
        self.bookbtn.move(1680-8, 183-30)
        self.bookbtn.clicked.connect(self.book)
        self.helpbtn = QToolButton(self)
        self.helpbtn.setIcon(QIcon("Data/help.png"))
        self.helpbtn.setIconSize(QSize(225, 75))
        self.helpbtn.resize(QSize(225, 75))
        self.helpbtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.helpbtn.move(1751, 946-30)
        self.helpbtn.clicked.connect(self.help)
        self.helpbtn1 = QToolButton(self)
        self.helpbtn1.setIcon(QIcon("Data/Home@2x.png"))
        self.helpbtn1.setIconSize(QSize(75, 75))
        self.helpbtn1.resize(QSize(75, 75))
        self.helpbtn1.setStyleSheet("background-color:transparent ; border-style:outset")
        self.helpbtn1.move(1751 - 40, 946 - 30)
        self.helpbtn1.clicked.connect(self.home)
        self.closebtn = QToolButton(self)
        self.closebtn.setIcon(QIcon("Data/close.png"))
        self.closebtn.setIconSize(QSize(41,25))
        self.closebtn.resize(QSize(41,25))
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
        self.get()

        self.j=0
        self.showMaximized()
        self.display()
    def home(self):
        pass
    def help(self):
        print("HI")
        if self.j==0:
            self.imageComputer2.setPixmap(QPixmap("Data/mainad.png").scaled(3840 / 2, 2080 / 2))
            self.imageComputer2.resize(2000,1030)
            self.j=1
        else:
            self.imageComputer2.setPixmap(QPixmap("Data/Main T@2x (1).png").scaled(3840 / 2, 2080 / 2))
            self.imageComputer2.resize(0, 0)
            self.j=0
        print("ok")

    def ok(self):
        self.t.stop()
        print("now")
        self.imageComputer2.setPixmap(QPixmap())
    def changes(self):
        self.timer1.stop()
        self.imageComputer1.setPixmap(QPixmap())

    def gotolink(self):
        if self.i==2 or self.i==3:
            QDesktopServices.openUrl(QUrl("https://globalshala.com/"))
    def book(self):
        self.book=Meetings.Meetings()
        self.close()
    def feedbacks(self):
        self.feed=Feedback.Feedbacks()
        self.close()
    def admin(self):
        self.admin=Admin.admin()
        self.close()
    def equipment(self):
        self.eq=Equipment.Equipment()
        self.close()
    def seats(self):
        self.seatts=date.date()
        self.close()
    def display(self):
        query = "SELECT Location from employee WHERE Empid=?;"
        employees = cur.execute(query,(data.id,)).fetchone()
        print(employees)
        x=employees[0]
        if x!=None:
            x=x.split(",")
            self.posx=(int(x[0]))*0.9264+18
            self.posy=(int(x[1]))*0.9265+62-8
            print(x[0])
            print(x[1])
            self.btn.setIcon(QIcon("Data/seats.png"))
            self.btn.move(self.posx,self.posy)
            data.occ=True
    def change(self):
        print("timeout")
        self.i=self.i+1

        print(len(self.employees))
        if self.i==len(self.employees):
            self.i=0
        if self.i==0:
            print("done")
            print(self.i)
            self.btn.setIcon(QIcon("Data/seats.png"))
            self.imageComputer.setPixmap(QPixmap("Data/Plan.jpg").scaled(1644, 959))
            print("done")
            self.display()
            if data.occ==True:
                self.btn.move(self.posx, self.posy)
                self.btn.resize(QSize(50,50))
            else:
                self.btn.setIcon(QIcon())

        else:
            print(self.i)
            print(self.employees[self.i])
            self.imageComputer.setPixmap(QPixmap(self.employees[self.i][0]).scaled(1644, 959))
            self.btn.setIcon(QIcon("Data/More@2x.png"))
            self.btn.setIconSize(QSize(100,40))
            self.btn.resize(QSize(100, 40))
            self.btn.move(803,864)
    def get(self):
        print(1)
        query = "SELECT photo FROM feed"
        self.employees = cur1.execute(query).fetchall()
        print("hi")
        print(len(self.employees))
