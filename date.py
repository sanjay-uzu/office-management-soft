import sys
import Admin
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap, QIcon
from PyQt5.QtWidgets import *
import Feedback
import data
import Meetings
import Equipment
import seat
import MainAdm, MainEmp
from datetime import datetime

class date(QWidget):
    def __init__(self):
        super().__init__()
        self.id=id
        self.setGeometry(100, 100,2000,1000)
        self.setWindowTitle("Admin Main")
        self.setStyleSheet("font-size:12pt;")
        now = datetime.now()
        self.date = str(now.strftime("%Y-%m-%d %H:%M:%S"))
        self.date = self.date.split()
        self.date = self.date[0]
        self.date = self.date.split('-')
        self.daycur = self.date[2]
        self.monthcur = self.date[1]
        self.yearcur = self.date[0]

        imageComputer = QLabel(self)
        imageComputer.setPixmap(QPixmap("Data/Select Date@2x.png").scaled(3824, 2070))
        imageComputer.move(0, 0)

        self.day = QComboBox(self)
        list2 = ["1","2","3","4","5","6","7","8","9","10","11","12"]
        for number in range(1, 32):
            self.day.addItem(str(number))
        self.month = QComboBox(self)
        self.month.addItems(list2)
        self.year = QComboBox(self)
        self.day.move(850,500)
        self.day.setStyleSheet("border-radius:10px")
        self.month.setStyleSheet("border-radius:10px")
        self.year.setStyleSheet("border-radius:10px")
        self.day.setMinimumWidth(30)
        self.month.setMinimumWidth(70)
        self.year.setMinimumWidth(80)
        self.month.move(910,500)
        self.year.move(990,500)
        self.day.setStyleSheet("font-size:12pt;")
        self.month.setStyleSheet("font-size:12pt;")
        self.year.setStyleSheet("font-size:12pt;")
        for number in range(2020, 2022):
            self.year.addItem(str(number))
        self.day.setCurrentIndex(int(self.daycur) - 1)
        self.month.setCurrentIndex(int(self.monthcur) - 1)
        self.seatbtn = QToolButton(self)
        self.seatbtn.setIcon(QIcon("Data/Go@2x.png"))
        self.seatbtn.setIconSize(QSize(80,40))
        self.seatbtn.resize(QSize(80,40))
        self.seatbtn.setStyleSheet(
            "QToolButton{background-color:transparent ; border-style:outset; border-radius:10px}")
        self.seatbtn.move(919,642)
        self.seatbtn.clicked.connect(self.next)
        self.seatbtn = QToolButton(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet("background:#fef2da")
        self.seatbtn.setIcon(QIcon("Data/Back@2x.png"))
        self.seatbtn.setIconSize(QSize(80, 40))
        self.seatbtn.resize(QSize(80, 40))
        self.seatbtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.seatbtn.move(1829, 10)
        self.seatbtn.clicked.connect(self.back)
        self.showMaximized()
    def next(self):
        self.seat=seat.Seats()
        self.close()
    def back(self):
        if data.type==1:
            self.adm=MainAdm.admmain()
        else:
            self.emp=MainEmp.empmain()
        self.close()