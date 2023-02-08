from PyQt5.QtCore import Qt
import sqlite3
import sys
import Equipment
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap, QIcon
from PyQt5.QtWidgets import *
import Feedback
import Meetings
import Account
import seat
import data
import Admin

class mvmdata(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 2000,1000)
        imageComputer = QLabel(self)
        imageComputer.setPixmap(QPixmap("Data/Movement Map@2x.png").scaled(3846, 1921))
        imageComputer.resize(3846, 1921)
        imageComputer.move(0, -420)
        self.setWindowTitle("Employee Main")
        self.seatbtn = QToolButton(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet("background:#fef2da")
        self.seatbtn.setIcon(QIcon("Data/Back@2x.png"))
        self.seatbtn.setIconSize(QSize(80,40))
        self.seatbtn.resize(QSize(80,40))
        self.seatbtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.seatbtn.move(10,12)
        self.seatbtn.clicked.connect(self.back)

        self.showMaximized()
    def back(self):
        self.ad=Admin.admin()
        self.close()