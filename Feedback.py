import os

import Admin
import MainAdm
import MainEmp
import Meetings
import Account
import Equipment
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
import sqlite3
from PIL import Image
import data
import date
defaultImg="Data/Upload ur image here.png"
con = sqlite3.connect('feedback.db')
cur = con.cursor()
class Feedbacks(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 2000, 1000)
        self.setWindowTitle("Feedback")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet("QWidget{background:#fef2da;font-size:12pt;}QLineEdit{background:#fffbf4;border-radius:10px}QComboBox{background:white;border-radius:10px}QTableWidget{background:white;border-radius:10px}QListWidget{background:white;border-radius:10px}")
        self.imageComputer2 = QLabel(self)
        self.photo = QLabel(self)
        self.photo.resize(QSize(600, 500))
        self.photo.setPixmap(QPixmap("Data/Upload ur image here.png").scaled(600, 500))
        self.photo.move(800,300)
        self.photo.setStyleSheet("border-radius:10px")
        self.submitbtn=QToolButton(self)
        self.submitbtn.setIcon(QIcon("Data/submit.png"))

        self.submitbtn.setIconSize(QSize(100,40))
        self.submitbtn.resize(QSize(100,40))
        self.submitbtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.submitbtn.move(600,810)
        self.submitbtn.clicked.connect(self.submit)
        self.uploadbtn = QToolButton(self)
        self.uploadbtn.move(1300, 810)
        self.uploadbtn.setIcon(QIcon("Data/upload.png"))
        self.uploadbtn.setIconSize(QSize(100, 40))
        self.uploadbtn.resize(QSize(100, 40))
        self.uploadbtn .setStyleSheet("background-color:transparent ;border-style:outset ")
        self.uploadbtn.clicked.connect(self.uploadImage)
        self.furn = QToolButton(self)
        self.fedlbl=QLabel("Feedback:",self)
        self.fedlbl.move(100,260)
        self.imglbl = QLabel("Image (If any):", self)
        self.imglbl.move(800, 260)
        self.furn.move(100,50)
        self.furniture=0
        self.furn.setIcon(QIcon("Data/furniture.png"))
        self.furn.setIconSize(QSize(200, 200))
        self.furn.resize(QSize(200, 200))
        self.furn.clicked.connect(self.furnclick)
        self.furn.setStyleSheet("QToolButton{background-color:transparent ; border-style:outset; border-radius:10px} QToolButton:hover{background:#7a6b49;}")
        self.toilet=0
        self.toil = QToolButton(self)
        self.toil.setIcon(QIcon("Data/network.png"))
        self.toil.setIconSize(QSize(200, 200))
        self.toil.resize(QSize(200, 200))
        self.toil.move(466,50)
        self.toil.clicked.connect(self.toilclick)
        self.toil.setStyleSheet("QToolButton{background-color:transparent ; border-style:outset; border-radius:10px} QToolButton:hover{background:#7a6b49;}")
        self.electrical=0
        self.electric_net = QToolButton(self)
        self.electric_net.setIcon(QIcon("Data/electrical.png"))
        self.electric_net.setIconSize(QSize(200, 200))
        self.electric_net.resize(QSize(200, 200))
        self.electric_net.move(832,50)
        self.electric_net.clicked.connect(self.electclick)
        self.electric_net.setStyleSheet("QToolButton{background-color:transparent ; border-style:outset; border-radius:10px} QToolButton:hover{background:#7a6b49;}")
        self.equipments=0
        self.equipment = QToolButton(self)
        self.equipment.setIcon(QIcon("Data/equipments.png"))
        self.equipment.setIconSize(QSize(200,200))
        self.equipment.resize(QSize(200, 200))
        self.equipment.move(1200,50)
        self.equipment.clicked.connect(self.equipclick)
        self.equipment.setStyleSheet("QToolButton{background-color:transparent ; border-style:outset; border-radius:10px} QToolButton:hover{background:#7a6b49;}")
        self.editor = QTextEdit(self)
        self.editor.setStyleSheet("background:white;border-radius:10px")
        self.editor.move(100, 300)
        self.editor.setPlaceholderText("Please Select The Category Of Your Feedback")
        self.editor.setAcceptRichText(False)
        self.editor.resize(QSize(600,500))
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
        self.equipbtn.clicked.connect(self.equip)
        self.feedbtn = QToolButton(self)
        self.feedbtn.setIcon(QIcon("Data/feedback.png"))
        self.feedbtn.setIconSize(QSize(225, 75))
        self.feedbtn.resize(QSize(240, 90))
        self.feedbtn.setStyleSheet(
            "QToolButton{background-color:transparent ; border-style:outset; border-radius:10px} QToolButton:hover{background:#fac34b;}")
        self.feedbtn.move(1680 - 8, 401 - 30)
        self.accntbtn = QToolButton(self)
        if data.type==1:
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
        self.helpbtn1 = QToolButton(self)
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
        self.seatbtn.clicked.connect(self.seats)
        op = QGraphicsOpacityEffect(self)
        op.setOpacity(0.3)
        op1 = QGraphicsOpacityEffect(self)
        op1.setOpacity(0.3)
        op2 = QGraphicsOpacityEffect(self)
        op2.setOpacity(0.3)
        op3 = QGraphicsOpacityEffect(self)
        op3.setOpacity(0.3)
        op4 = QGraphicsOpacityEffect(self)
        op4.setOpacity(0.3)
        op5 = QGraphicsOpacityEffect(self)
        op5.setOpacity(0.3)
        op6 = QGraphicsOpacityEffect(self)
        op6.setOpacity(0.3)
        op7 = QGraphicsOpacityEffect(self)
        op7.setOpacity(0.3)
        self.equipment.setGraphicsEffect(op4)
        self.equipment.setAutoFillBackground(True)
        self.electric_net.setGraphicsEffect(op5)
        self.electric_net.setAutoFillBackground(True)
        self.furn.setGraphicsEffect(op6)
        self.furn.setAutoFillBackground(True)
        self.toil.setGraphicsEffect(op7)
        self.toil.setAutoFillBackground(True)
        self.bookbtn.setGraphicsEffect(op)
        self.bookbtn.setAutoFillBackground(True)
        self.accntbtn.setGraphicsEffect(op1)
        self.accntbtn.setAutoFillBackground(True)
        self.seatbtn.setGraphicsEffect(op2)
        self.seatbtn.setAutoFillBackground(True)
        self.equipbtn.setGraphicsEffect(op3)
        self.equipbtn.setAutoFillBackground(True)
        self.i=0

        self.showMaximized()
    def help(self):
        print("HI")
        if self.i==0:
            self.imageComputer2.setPixmap(QPixmap("Data/Feedbak Help.png").scaled(868, 973))
            self.imageComputer2.resize(868,973)
            self.imageComputer2.move(792,50)
            self.imageComputer2.setStyleSheet("background:transparent")
            self.i=1
            print("in")
        else:
            self.imageComputer2.setPixmap(QPixmap("Data/Equip Help@2x.png").scaled(3840 / 2, 2080 / 2))
            self.imageComputer2.resize(0, 0)
            self.i=0
    def furnclick(self):
        op = QGraphicsOpacityEffect(self)
        op.setOpacity(0.3)
        op1 = QGraphicsOpacityEffect(self)
        op1.setOpacity(1)
        if self.furniture==0:
            self.toilet = 0
            self.furniture =1
            self.equipments = 0
            self.electrical = 0
            self.furn.setGraphicsEffect(op1)
            self.furn.setAutoFillBackground(True)
            op3 = QGraphicsOpacityEffect(self)
            op3.setOpacity(0.3)
            op4 = QGraphicsOpacityEffect(self)
            op4.setOpacity(0.3)
            op5 = QGraphicsOpacityEffect(self)
            op5.setOpacity(0.3)
            op6 = QGraphicsOpacityEffect(self)
            op6.setOpacity(0.3)
            op7 = QGraphicsOpacityEffect(self)
            op7.setOpacity(0.3)
            self.equipment.setGraphicsEffect(op4)
            self.equipment.setAutoFillBackground(True)
            self.electric_net.setGraphicsEffect(op5)
            self.electric_net.setAutoFillBackground(True)
            self.toil.setGraphicsEffect(op7)
            self.toil.setAutoFillBackground(True)
        else:
            self.furn.setGraphicsEffect(op)
            self.furn.setAutoFillBackground(True)
            self.furniture=0
    def toilclick(self):
        op = QGraphicsOpacityEffect(self)
        op.setOpacity(0.3)
        op1 = QGraphicsOpacityEffect(self)
        op1.setOpacity(1)
        if self.toilet==0:
            self.toilet=1
            self.furniture=0
            self.equipments=0
            self.electrical=0
            op3 = QGraphicsOpacityEffect(self)
            op3.setOpacity(0.3)
            op4 = QGraphicsOpacityEffect(self)
            op4.setOpacity(0.3)
            op5 = QGraphicsOpacityEffect(self)
            op5.setOpacity(0.3)
            op6 = QGraphicsOpacityEffect(self)
            op6.setOpacity(0.3)
            op7 = QGraphicsOpacityEffect(self)
            op7.setOpacity(0.3)
            self.equipment.setGraphicsEffect(op4)
            self.equipment.setAutoFillBackground(True)
            self.electric_net.setGraphicsEffect(op5)
            self.electric_net.setAutoFillBackground(True)
            self.furn.setGraphicsEffect(op6)
            self.furn.setAutoFillBackground(True)
            self.toil.setGraphicsEffect(op1)
            self.toil.setAutoFillBackground(True)
        else:
            self.toil.setGraphicsEffect(op)
            self.toil.setAutoFillBackground(True)
            self.toilet=0
    def electclick(self):
        op = QGraphicsOpacityEffect(self)
        op.setOpacity(0.3)
        op1 = QGraphicsOpacityEffect(self)
        op1.setOpacity(1)
        if self.electrical==0:
            self.toilet = 0
            self.furniture = 0
            self.equipments = 0
            self.electrical = 1
            self.electric_net.setGraphicsEffect(op1)
            self.electric_net.setAutoFillBackground(True)
            op3 = QGraphicsOpacityEffect(self)
            op3.setOpacity(0.3)
            op4 = QGraphicsOpacityEffect(self)
            op4.setOpacity(0.3)
            op5 = QGraphicsOpacityEffect(self)
            op5.setOpacity(0.3)
            op6 = QGraphicsOpacityEffect(self)
            op6.setOpacity(0.3)
            op7 = QGraphicsOpacityEffect(self)
            op7.setOpacity(0.3)
            self.equipment.setGraphicsEffect(op4)
            self.equipment.setAutoFillBackground(True)
            self.furn.setGraphicsEffect(op6)
            self.furn.setAutoFillBackground(True)
            self.toil.setGraphicsEffect(op7)
            self.toil.setAutoFillBackground(True)
        else:
            self.electrical=0
            self.electric_net.setGraphicsEffect(op)
            self.electric_net.setAutoFillBackground(True)
    def equipclick(self):
        op = QGraphicsOpacityEffect(self)
        op.setOpacity(0.3)
        op1 = QGraphicsOpacityEffect(self)
        op1.setOpacity(1)
        if self.equipments==0:
            self.toilet = 0
            self.furniture = 0
            self.equipments = 1
            self.electrical = 0
            self.equipment.setGraphicsEffect(op1)
            self.equipment.setAutoFillBackground(True)
            op3 = QGraphicsOpacityEffect(self)
            op3.setOpacity(0.3)
            op4 = QGraphicsOpacityEffect(self)
            op4.setOpacity(0.3)
            op5 = QGraphicsOpacityEffect(self)
            op5.setOpacity(0.3)
            op6 = QGraphicsOpacityEffect(self)
            op6.setOpacity(0.3)
            op7 = QGraphicsOpacityEffect(self)
            op7.setOpacity(0.3)
            self.electric_net.setGraphicsEffect(op5)
            self.electric_net.setAutoFillBackground(True)
            self.furn.setGraphicsEffect(op6)
            self.furn.setAutoFillBackground(True)
            self.toil.setGraphicsEffect(op7)
            self.toil.setAutoFillBackground(True)
        else:
            self.equipments=0
            self.equipment.setGraphicsEffect(op)
            self.equipment.setAutoFillBackground(True)
    def home(self):
        if data.type==1:
            self.adm=MainAdm.admmain()
        else:
            self.emp=MainEmp.empmain()
        self.close()
    def uploadImage(self):
        global defaultImg
        size = (500,500)
        self.fileName, ok = QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Image Files (*.jpg *.png)')

        if ok:
            defaultImg = os.path.basename(self.fileName)
            img = Image.open(self.fileName)
            img = img.resize(size)
            img.save("Data/{}".format(defaultImg))
            defaultImg = "Data/{}".format(defaultImg)
            self.photo.setPixmap(QPixmap(defaultImg).scaled(500, 500))
    def submit(self):
        global defaultImg
        type=[]
        if self.equipments==1:
            type.append("equipments")
        if self.toilet==1:
            type.append("toilet")
        if self.furniture==1:
            type.append("furniture")
        if self.electrical==1:
            type.append("Electrical or network")
        type=' '.join(type)
        feed=self.editor.toPlainText()
        if feed=="":
            mbox = QMessageBox.information(self, "Information", "Please type some feedback")
        else:
            query = "INSERT INTO feedback (feedback,type,empid,photo) VALUES(?,?,?,?)"
            cur.execute(query,(feed,type,data.id,defaultImg))
            con.commit()
            QMessageBox.information(self, "Success", "Feedback Sumbitted")
    def book(self):
        self.book=Meetings.Meetings()
        self.close()
    def accnt(self):
        if data.type==1:
            self.accnt=Admin.admin()
            self.close()
        else:
            self.accnt=Account.Accnt()
            self.close()

    def equip(self):
        self.eq = Equipment.Equipment()
        self.close()

    def seats(self):
        self.seatts = date.date()
        self.close()
    def home(self):
        if data.type==1:
            self.adm=MainAdm.admmain()
        else:
            self.emp=MainEmp.empmain()
        self.close()