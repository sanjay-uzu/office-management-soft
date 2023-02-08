import sys
import Equipment
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap, QIcon
from PyQt5.QtWidgets import *
import Feedback
import Meetings
import Account
from functools import partial
import MainAdm, MainEmp
import data
import sqlite3
con = sqlite3.connect('empolyee.db')
cur = con.cursor()

class Seats(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 2000,1000)
        self.setWindowTitle("Employee Main")
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.list1=[161,395,161,470,303,582,599,867,674,915,674,962,861,867,861,915,1233,820,1345,915,1531,962,1680,678,1680,631,1607,284,1560,284,972,66,972,19,675,19,599,66,489,161,413,161]
        imageComputer = QLabel(self)
        self.i=0
        self.j=0
        self.setStyleSheet("QWidget{background:#fef2da;font-size:12pt;}QLineEdit{background:#fffbf4;border-radius:10px}QComboBox{background:white;border-radius:10px}QTableWidget{background:white;border-radius:10px}QListWidget{background:white;border-radius:10px}")
        size = self.size()
        self.seta=[]
        while self.i<21:
            self.seta.append(0)
            self.i=self.i+1
        self.i=0
        imageComputer.setPixmap(QPixmap("Data/Plan.jpg").scaled(1775, 1035))
        imageComputer.move(0,0)
        self.imageComputer2 = QLabel(self)
        while self.i<21:
            self.seta[self.i]= QToolButton(self)
            print(self.i)
            h=self.i
            self.seta[self.i].resize(QSize(53,53))
            self.seta[self.i].setIconSize(QSize(53, 53))
            self.seta[self.i].setStyleSheet("background-color:transparent ; border-style:outset")
            self.seta[self.i].move(self.list1[self.j],self.list1[self.j+1])
            self.seta[self.i].clicked.connect(partial(self.book,h))
            self.i=self.i+1
            self.j=self.j+2
        self.btn = QToolButton(self)
        self.btn.setIcon(QIcon())
        self.btn.setIconSize(QSize(50, 50))
        self.btn.resize(QSize(50, 50))
        self.btn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.btn1 = QToolButton(self)
        self.btn1.setIcon(QIcon("Data/Legend@2x.png"))
        self.btn1.setIconSize(QSize(150,195))
        self.btn1.resize(QSize(150, 195))
        self.btn1.setStyleSheet("background-color:transparent ; border-style:outset")
        self.btn1.move(1766,398)
        self.seatbtn=QToolButton(self)
        self.seatbtn.setIcon(QIcon("Data/Back@2x.png"))
        self.seatbtn.setIconSize(QSize(80, 40))
        self.seatbtn.resize(QSize(80, 40))
        self.seatbtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.seatbtn.move(1825, 12)
        self.seatbtn.clicked.connect(self.back)
        self.helpbtn = QToolButton(self)
        self.helpbtn.setIcon(QIcon("Data/help.png"))
        self.helpbtn.setIconSize(QSize(225, 75))
        self.helpbtn.resize(QSize(225, 75))
        self.helpbtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.helpbtn.move(1751, 946 - 30)
        self.helpbtn.clicked.connect(self.help)
        self.i=0
        self.display()
        self.showMaximized()
    def help(self):
        print("HI")
        if self.i==0:
            self.imageComputer2.setPixmap(QPixmap("Data/Sel Seat 1@2x.png").scaled(3840, 2080))
            self.imageComputer2.resize(2000,1030)
            self.i=1
        else:
            self.imageComputer2.setPixmap(QPixmap("Data/Sel Seat 1@2x.png").scaled(3840 / 2, 2080 / 2))
            self.imageComputer2.resize(0, 0)
            self.i=0
        print("ok")
    def book(self,k):
        self.seta[k].setIcon(QIcon("Data/seats.png"))
        print(self.seta[k].x())
        print(self.seta[k].y())
        self.seta[k].setIconSize(QSize(53, 53))
        self.imageComputer2.setPixmap(QPixmap("Data/Sel Seat 1@2x.png").scaled(3840 / 2, 2080 / 2))
        self.imageComputer2.resize(0, 0)
        self.btn.setIcon(QIcon())

        mbox = QMessageBox.question(self, "Info", "You have selected seat number {}\n"
                                                  "Proceed with the booking?".format(k),
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            query = "UPDATE employee set Location=?  WHERE Empid=? ;"
            string=str(self.seta[k].x())+","+str((self.seta[k].y()))
            print(string)
            cur.execute(query, (string,data.id))
            print("Quere exedcuted")
            con.commit()
            self.close()
            if data.type==1:
                self.main=MainAdm.admmain()
                self.close()
            else:
                self.main=MainEmp.empmain()
                self.close()
        else:
            self.seta[k].setIcon(QIcon())
    def display(self):
        query = "SELECT Location from employee WHERE Empid=?;"
        employees = cur.execute(query,(data.id,)).fetchone()
        print(employees)
        x=employees[0]
        if x!=None:
            x=x.split(",")
            posx=(int(x[0]))
            posy=(int(x[1]))
            print(x[0])
            print(x[1])
            self.btn.setIcon(QIcon("Data/seats.png"))
            self.btn.move(posx,posy)
            data.occ=True
    def back(self):
        if data.type == 1:
            self.main = MainAdm.admmain()
            self.close()
        else:
            self.main = MainEmp.empmain()
            self.close()
