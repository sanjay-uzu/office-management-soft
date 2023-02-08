import sys,os
from PIL import Image
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap, QIcon
from PyQt5.QtWidgets import *
import sqlite3
import Admin
con = sqlite3.connect('equipment.db')
cur = con.cursor()
defaultImg="Data/Equip Default.png"

class Addequip(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 2000,1000)
        self.setWindowTitle("Add Equipment")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet("QWidget{background:#fef2da;font-size:12pt;}QLineEdit{background:#fffbf4;border-radius:10px}QComboBox{background:white;border-radius:10px}QTableWidget{background:white;border-radius:10px}QListWidget{background:white;border-radius:10px}")
        self.mainhbox=QHBoxLayout()
        self.leftvbox=QVBoxLayout()
        self.rightvbox=QVBoxLayout()
        self.bottomhbox=QHBoxLayout()
        self.backbtn = QToolButton()
        self.backbtn.setIcon(QIcon("Data/Back@2x.png"))
        self.backbtn.setIconSize(QSize(80,40))
        self.backbtn.resize(QSize(80, 40))
        self.backbtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.backbtn.clicked.connect(self.back)
        self.addbtn = QToolButton()
        self.addbtn.setIcon(QIcon("Data/New@2x.png"))
        self.addbtn.setIconSize(QSize(100,40))
        self.addbtn.resize(QSize(100, 40))
        self.addbtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.addbtn.clicked.connect(self.addclick)
        self.deletebtn = QToolButton()
        self.deletebtn.setIcon(QIcon("Data/delete.png"))
        self.deletebtn.setIconSize(QSize(100, 40))
        self.deletebtn.resize(QSize(100,40))
        self.deletebtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.deletebtn.clicked.connect(self.deleteEmployee)
        self.editbtn = QToolButton()
        self.editbtn.setIcon(QIcon("Data/Edit@2x.png"))
        self.editbtn.setIconSize(QSize(100,40))
        self.editbtn.resize(QSize(100,40))
        self.editbtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.editbtn.clicked.connect(self.edit)
        self.equiplistlbl=QLabel("Equipment List:")
        self.equiplist=QListWidget()
        self.photo = QLabel()
        self.photo.resize(QSize(300, 300))
        self.photo.setPixmap(QPixmap("Data/Equip Default.png").scaled(300, 300))
        self.locationlbl=QLabel("Location:")
        self.description=QLabel("Description:")
        self.destext=QTextEdit()
        self.destext.setStyleSheet("background:white;border-radius:10px")
        self.name=QLabel("Name:")
        self.names=QLineEdit()
        self.location=QLineEdit()
        self.addsbtn=QToolButton()
        self.addsbtn.setIcon(QIcon("Data/add.png"))
        self.addsbtn.setIconSize(QSize(100, 40))
        self.addsbtn.resize(QSize(100, 40))
        self.addsbtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.addsbtn.clicked.connect(self.add)
        self.savebtn=QToolButton()
        self.savebtn.setIcon(QIcon("Data/save.png"))
        self.savebtn.setIconSize(QSize(80, 40))
        self.savebtn.resize(QSize(80, 40))
        self.savebtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.savebtn.clicked.connect(self.updateEmployee)
        self.hbox3=QHBoxLayout()
        self.hbox3.addWidget(self.addsbtn)
        self.hbox3.addWidget(self.savebtn)
        self.hbox3.setAlignment(Qt.AlignCenter)
        self.uploadbtn=QToolButton()
        self.uploadbtn.setIcon(QIcon("Data/upload.png"))
        self.uploadbtn.setIconSize(QSize(100, 40))
        self.uploadbtn.resize(QSize(100, 40))
        self.uploadbtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.uploadbtn.clicked.connect(self.uploadImage)
        self.hbox1=QHBoxLayout()
        self.hbox2=QHBoxLayout()
        self.hbox1.setAlignment(Qt.AlignCenter)
        self.hbox2.setAlignment(Qt.AlignCenter)
        self.hbox1.addWidget(self.photo)
        self.hbox2.addWidget(self.uploadbtn)
        self.rightvbox.addLayout(self.hbox1)
        self.rightvbox.addLayout(self.hbox2)
        self.rightvbox.addWidget(self.name)
        self.rightvbox.addWidget(self.names)
        self.rightvbox.addWidget(self.locationlbl)
        self.rightvbox.addWidget(self.location)
        self.rightvbox.addWidget(self.description)
        self.rightvbox.addWidget(self.destext)
        self.rightvbox.addLayout(self.hbox3)
        self.leftvbox.addWidget(self.backbtn)
        self.leftvbox.addWidget(self.equiplistlbl)
        self.leftvbox.addWidget(self.equiplist)
        self.bottomhbox.addWidget(self.addbtn)
        self.bottomhbox.addWidget(self.editbtn)
        self.bottomhbox.addWidget(self.deletebtn)
        self.leftvbox.addLayout(self.bottomhbox)
        self.mainhbox.addLayout(self.leftvbox)
        self.mainhbox.addLayout(self.rightvbox)
        self.setLayout(self.mainhbox)
        self.names.setEnabled(False)
        self.location.setEnabled(False)
        self.destext.setEnabled(False)
        self.savebtn.setEnabled(False)
        self.getEquipment()
        self.equiplist.itemClicked.connect(self.singleClick)
        self.addsbtn.setEnabled(False)
        self.showMaximized()
    def back(self):
        self.admin=Admin.admin()
        self.close()
    def edit(self):
        if self.equiplist.selectedItems():
            self.names.setEnabled(True)
            self.location.setEnabled(True)
            self.destext.setEnabled(True)
            self.addsbtn.setEnabled(False)
            self.savebtn.setEnabled(True)
        else:
            QMessageBox.information(self, "Warning!!!", "Please select a Equipment to update")



    def getEquipment(self):
        query = "SELECT id,name,location,photo,description FROM equipment"
        employees = cur.execute(query).fetchall()
        for employee in employees:
            self.equiplist.addItem(employee[1])
    def addclick(self):
        self.names.setEnabled(True)
        self.location.setEnabled(True)
        self.destext.setEnabled(True)
        self.addsbtn.setEnabled(True)
        self.names.setText("")
        self.location.setText("")
        self.destext.setText("")
        self.photo.setPixmap(QPixmap("Data/Equip Default.png").scaled(300, 300))
    def uploadImage(self):
        global defaultImg
        size = (300,300)
        self.fileName, ok = QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Image Files (*.jpg *.png)')

        if ok:
            defaultImg = os.path.basename(self.fileName)
            img = Image.open(self.fileName)
            img = img.resize(size)
            img.save("Data/{}".format(defaultImg))
            defaultImg = "Data/{}".format(defaultImg)
            self.photo.setPixmap(QPixmap(defaultImg).scaled(300, 300))

    def add(self):
        global defaultImg
        name=self.names.text()
        location=self.location.text()
        desc=self.destext.toPlainText()
        if name=="" or location=="" or desc=="" :
            mbox = QMessageBox.information(self, "Information", "Please Do Not Leave Any Fields Empty")
        else:
            query = "INSERT INTO equipment (name,location,photo,description) VALUES(?,?,?,?)"
            cur.execute(query, (name,location,defaultImg,desc))
            con.commit()
            QMessageBox.information(self, "Success", "Equipment Added")
            self.names.setText("")
            self.location.setText("")
            self.destext.setText("")
            self.equiplist.clear()
            self.getEquipment()

    def singleClick(self):
        person = self.equiplist.currentItem().text()
        id = self.getid(person)
        query = ("SELECT * FROM equipment WHERE id=?")
        person = cur.execute(query, (id,)).fetchone()  # single item tuple=(1,)
        self.names.setText(person[0])
        self.location.setText(person[3])
        self.destext.setText(person[4])
        self.photo.setPixmap(QPixmap(person[2]).scaled(300, 300))
        self.names.setEnabled(False)
        self.location.setEnabled(False)
        self.destext.setEnabled(False)
        self.addsbtn.setEnabled(False)
        self.savebtn.setEnabled(False)

    def updateEmployee(self):
            employee = self.equiplist.currentItem().text()
            id = self.getid(employee)
            query = ("SELECT * FROM equipment WHERE id=?")
            global defaultImg
            name = self.names.text()
            print(name)
            location = self.location.text()
            desc = self.destext.toPlainText()
            print(name)
            try:
                query = "UPDATE equipment set name =?, location=?, photo=?,description=? WHERE id=?"
                cur.execute(query,(name,location,defaultImg,desc,id))
                con.commit()
                QMessageBox.information(self, "Success", "Equipment has been updated")
                self.equiplist.clear()

            except:
                QMessageBox.information(self, "Warning", "Equipment has not been updated")
            self.getEquipment()
    def deleteEmployee(self):
        if self.equiplist.selectedItems():
            person=self.equiplist.currentItem().text()
            id = self.getid(person)
            mbox=QMessageBox.question(self,"Warning","Are you sure to delete this Equipment?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
            if mbox == QMessageBox.Yes:
                try:
                    query="DELETE FROM equipment WHERE id=?"
                    cur.execute(query,(id,))
                    con.commit()
                    QMessageBox.information(self,"Info!!!","Equipment has been deleted")
                except:
                    QMessageBox.information(self,"Warning!!!","Equipment has not been deleted")
            self.equiplist.clear()
            self.names.setText("")
            self.location.setText("")
            self.destext.setText("")
            self.getEquipment()
        else:
            QMessageBox.information(self, "Warning!!!", "Please select a Equipment to delete")
    def getid(self,person):
        query = "SELECT id,name,location,photo,description FROM equipment"
        employees = cur.execute(query).fetchall()
        for employee in employees:
            if person==employee[1]:
                return employee[0]



