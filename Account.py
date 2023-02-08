import os
import sys
import sqlite3

import MainAdm
import MainEmp
import data
import Equipment
import Feedback
import Meetings
import ResetPassword
from PIL import Image
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap, QIcon
from PyQt5.QtWidgets import *
import date
import seat
con = sqlite3.connect('empolyee.db')
cur = con.cursor()
defaultImg="Data/eMP dEFAUILT.png"

class Accnt(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 2300, 1000)
        self.imageComputer2 = QLabel(self)
        self.setWindowTitle("Account")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.editbtn=QToolButton(self)
        self.editbtn.setIcon(QIcon("Data/Edit@2x.png"))
        self.editbtn.setIconSize(QSize(100,40))
        self.editbtn.resize(QSize(100,40))
        self.editbtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.resetpswd=QToolButton(self)
        self.resetpswd.setIcon(QIcon("Data/resetpass.png"))
        self.resetpswd.setIconSize(QSize(200,40))
        self.resetpswd.resize(QSize(200,40))
        self.resetpswd.setStyleSheet("background-color:transparent ; border-style:outset")
        self.setStyleSheet("QWidget{background:#fef2da;font-size:12pt;}QLineEdit{background:#fffbf4;border-radius:10px}QComboBox{background:white;border-radius:10px}QTableWidget{background:white;border-radius:10px}QListWidget{background:white;border-radius:10px}")
        self.editbtn.move(550,800)
        self.editbtn.clicked.connect(self.edit)
        self.resetpswd.move(660,800)
        self.resetpswd.clicked.connect(self.reset)
        self.savebtn=QToolButton(self)
        self.savebtn.setIcon(QIcon("Data/save.png"))
        self.savebtn.setIconSize(QSize(80,40))
        self.savebtn.resize(QSize(80,40))
        self.savebtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.savebtn.move(870,800)
        self.savebtn.clicked.connect(self.save)
        self.photo=QLabel(self)
        self.photo.resize(QSize(300,300))
        self.photo.setPixmap(QPixmap("Data/eMP dEFAUILT.png").scaled(300, 300))
        self.photo.move(600,50)
        self.changebtn=QToolButton(self)
        self.changebtn.setIcon(QIcon("Data/upload.png"))
        self.changebtn.setIconSize(QSize(100,40))
        self.changebtn.resize(QSize(100, 40))
        self.changebtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.changebtn.move(700,370)
        self.changebtn.setEnabled(False)
        self.changebtn.clicked.connect(self.uploadImage)
        self.emplbl=QLabel("Employee ID",self)
        self.empid=QLineEdit(self)
        self.emplbl.move(100+500,425)
        self.empid.move(230+500,425)
        self.empid.setEnabled(False)
        self.namelbl = QLabel("Name", self)
        self.name = QLineEdit(self)
        self.namelbl.move(100+500, 475)
        self.name.move(230+500, 475)
        self.name.setEnabled(False)
        self.teamlbl = QLabel("Team", self)
        self.team = QLineEdit(self)
        self.teamlbl.move(100+500, 525)
        self.team.move(230+500, 525)
        self.team.setEnabled(False)
        self.desiglbl = QLabel("Deisgnation", self)
        self.desig = QLineEdit(self)
        self.desiglbl.move(100+500, 575)
        self.desig.move(230+500, 575)
        self.desig.setEnabled(False)
        self.deparlbl = QLabel("Department", self)
        self.depar = QComboBox(self)
        departments=["Finance","IT","Others"]
        for department in departments:
            self.depar.addItem(department)
        self.deparlbl.move(100+500, 625)
        self.depar.setEnabled(False)
        self.depar.move(230+500, 625)
        self.phonelbl = QLabel("PhoneNo", self)
        self.phone = QLineEdit(self)
        self.phonelbl.move(100+500, 675)
        self.phone.move(230+500, 675)
        self.phone.setEnabled(False)
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
        self.accntbtn.setIcon(QIcon("Data/account.png"))
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
        self.seatbtn.clicked.connect(self.seats)
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
        self.i=0
        self.getemployee()
    def home(self):
        if data.type==1:
            self.adm=MainAdm.admmain()
        else:
            self.emp=MainEmp.empmain()
        self.close()
    def help(self):
        print("HI")
        if self.i==0:
            self.imageComputer2.setPixmap(QPixmap("Data/Account Help.png").scaled(1402, 162))
            self.imageComputer2.resize(1402,162)
            self.imageComputer2.move(60,857)
            self.imageComputer2.setStyleSheet("background:transparent")
            self.i=1
            print("in")
        else:
            self.imageComputer2.setPixmap(QPixmap("Data/Equip Help@2x.png").scaled(3840 / 2, 2080 / 2))
            self.imageComputer2.resize(0, 0)
            self.i=0
    def getemployee(self):
        global defaultImg
        query = "SELECT Empid,Name,Team, Designation , Department,Phone,Photo,Password FROM employee WHERE Empid=?"
        employees = cur.execute(query,(data.id,)).fetchone()
        self.photo.setPixmap(QPixmap(employees[-2]).scaled(300, 300))
        self.empid.setText(employees[0])
        self.name.setText(employees[1])
        self.team.setText(employees[2])
        self.desig.setText(employees[3])
        if employees[4]=="IT":
            self.depar.setCurrentIndex(1)
        if employees[4]=="Finance":
            self.depar.setCurrentIndex(0)
        if employees[4]=="Others":
            self.depar.setCurrentIndex(2)
        self.phone.setText(str(employees[5]))
        self.password=employees[-1]
        defaultImg=employees[-2]
    def edit(self):
        self.changebtn.setEnabled(True)
        self.name.setEnabled(True)
        self.empid.setEnabled(True)
        self.team.setEnabled(True)
        self.desig.setEnabled(True)
        self.depar.setEnabled(True)
        self.phone.setEnabled(True)
    def save(self):
        global defaultImg
        name=self.name.text()
        empid=self.empid.text()
        team=self.team.text()
        desig=self.team.text()
        depar=self.depar.currentText()
        phone=self.phone.text()

        query = "UPDATE employee set Empid=?,Name=?,Team=?, Designation=? , Department=?,Phone=?,Photo=?  WHERE Empid=?"
        cur.execute(query, (empid,name,team,desig,depar,phone,defaultImg,data.id))
        con.commit()
        QMessageBox.information(self, "Success", "Person has been updated")
    def uploadImage(self):
        global defaultImg
        size = (300,300)
        self.fileName, ok = QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Image Files (*.jpg *.png)')

        if ok:
            defaultImg = os.path.basename(self.fileName)
            img = Image.open(self.fileName)
            img = img.resize(size)
            img.save("Data/{}".format(defaultImg))
            defaultImg="Data/{}".format(defaultImg)
            self.photo.setPixmap(QPixmap(defaultImg).scaled(300, 300))
    def reset(self):
        self.reset=ResetPassword.ResetPass()
    def equipment(self):
        self.eq = Equipment.Equipment()
        self.close()
    def feedbacks(self):
        self.feed=Feedback.Feedbacks()
        self.close()
    def book(self):
        self.book=Meetings.Meetings()
        self.close()

    def seats(self):
        self.seatts = date.date()
        self.close()