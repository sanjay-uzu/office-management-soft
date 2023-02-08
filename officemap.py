import os
import sqlite3

import Admin
from PIL import Image
defaultImg="Data/Plan.jpg"

from PyQt5.QtCore import QSize,Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import *

con = sqlite3.connect('empolyee.db')
cur = con.cursor()

class offmain(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 2000,1000)
        self.imageComputer2 = QLabel(self)
        self.setWindowTitle("Employee Main")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.imageComputer = QLabel(self)
        self.setStyleSheet("QWidget{background:#fef2da;font-size:12pt;}QLineEdit{background:#fffbf4;border-radius:10px}QComboBox{background:white;border-radius:10px}QTableWidget{background:white;border-radius:10px}QListWidget{background:white;border-radius:10px}")
        size = self.size()
        self.imageComputer.setPixmap(QPixmap("Data/Plan Base.jpg").scaled(1500, 875))
        self.imageComputer.move(180,62)
        self.uploadbtn = QToolButton(self)
        self.uploadbtn.move(740, 950)
        self.uploadbtn.setIcon(QIcon("Data/upload.png"))
        self.uploadbtn.setIconSize(QSize(100, 40))
        self.uploadbtn.resize(QSize(100, 40))
        self.uploadbtn.setStyleSheet("background-color:transparent ;border-style:outset ")
        self.uploadbtn.clicked.connect(self.uploadImage)
        self.addseatsbtn = QToolButton(self)
        self.addseatsbtn.move(940, 950)
        self.addseatsbtn.setIcon(QIcon("Data/Add Seat@2x.png"))
        self.addseatsbtn.setIconSize(QSize(120, 40))
        self.addseatsbtn.resize(QSize(120, 40))
        self.addseatsbtn.setStyleSheet("background-color:transparent ;border-style:outset ")
        self.backbtn = QToolButton(self)
        self.backbtn.setIcon(QIcon("Data/Back@2x.png"))
        self.backbtn.setIconSize(QSize(80, 40))
        self.backbtn.resize(QSize(80, 40))
        self.backbtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.backbtn.clicked.connect(self.back)
        self.backbtn.move(10,20)
        self.helpbtn=QToolButton(self)
        self.helpbtn.setIcon(QIcon("Data/help.png"))
        self.helpbtn.setIconSize(QSize(225, 75))
        self.helpbtn.resize(QSize(225, 75))
        self.helpbtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.helpbtn.move(1751, 946 - 30)
        self.helpbtn.clicked.connect(self.help)
        self.i=0
        self.btns=[]
        i=0
        while i<100:
            self.btns.append(0)
            i=i+1
        i=0
        while i<100:
            self.btns[i]=QToolButton(self)
            self.btns[i].setStyleSheet("background-color:transparent ;border-style:outset ")
            i=i+1
        self.showMaximized()
        self.k=0
    def help(self):
        print("HI")
        if self.i==0:
            self.imageComputer2.setPixmap(QPixmap("Data/Floor Map Help.png").scaled(1887, 102))
            self.imageComputer2.resize(1887,102)
            self.imageComputer2.move(56,944)
            self.imageComputer2.setStyleSheet("background:transparent")
            self.i=1
            print("in")
        else:
            self.imageComputer2.setPixmap(QPixmap("Data/Equip Help@2x.png").scaled(3840 / 2, 2080 / 2))
            self.imageComputer2.resize(0, 0)
            self.i=0
    def uploadImage(self):
        global defaultImg
        size = (1500,875)
        self.fileName, ok = QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Image Files (*.jpg *.png)')

        if ok:
            defaultImg = os.path.basename(self.fileName)
            img = Image.open(self.fileName)
            img = img.resize(size)
            img.save("Data/{}".format(defaultImg))
            defaultImg = "Data/{}".format(defaultImg)
            self.imageComputer.setPixmap(QPixmap(defaultImg).scaled(1500, 875))
    def back(self):
        self.admin=Admin.admin()
        self.close()
    def mousePressEvent(self, QMouseEvent):
        if self.k<100:
            x=str(QMouseEvent.pos())
            x=x.split('(')
            x=x[-1]
            x=x[0:-1]
            x=x.split(",")
            posx=int(x[0])-25
            posy=int(x[1])-25
            print(x)
            if posx>180 and posx<1677 and posy>63 and posy<934:
                self.btns[self.k].move(posx,posy)
                print("done")
                self.btns[self.k].setIcon(QIcon("Data/seats.png"))
                self.btns[self.k].setIconSize(QSize(50,50))
                self.btns[self.k].resize(QSize(50, 50))

                self.k=self.k+1
