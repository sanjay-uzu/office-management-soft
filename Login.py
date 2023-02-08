import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
import sqlite3
import data



con = sqlite3.connect('empolyee.db')
cur = con.cursor()
from MainAdm import admmain
from MainEmp import empmain


class Loginwin(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(750, 100, 450, 400)
        self.setWindowTitle("Login")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.layouts()

        self.show()

    def layouts(self):
        self.mainvbox = QVBoxLayout()
        self.setLayout(self.mainvbox)
        self.setStyleSheet("background:#fef2da;font-size:12pt")
        self.mainvbox.addStretch()
        self.usnlabel = QLabel("Employee Id:", self)
        self.passlabel = QLabel("Password", self)
        self.usn = QLineEdit(self)
        self.usn.setMinimumHeight(40)
        self.usn.setStyleSheet("background:#fffbf4;border-radius:10px")
        self.usn.setPlaceholderText(" Enter Employee ID")
        self.passworde = QLineEdit(self)
        self.passworde.setMinimumHeight(40)
        self.passworde.setStyleSheet("background:#fffbf4;border-radius:10px")
        self.passworde.setPlaceholderText(" Enter Password")
        self.passworde.setEchoMode(QLineEdit.Password)
        self.passworde.returnPressed.connect(self.login)
        self.hbox=QHBoxLayout()
        self.btn = QToolButton( self)
        self.btn1 = QToolButton( self)
        self.hbox.setAlignment(Qt.AlignCenter)
        self.hbox.addWidget(self.btn)
        self.btn.setIcon(QIcon("Data/login.png"))
        self.btn.setIconSize(QSize(120,40))
        self.btn.resize(QSize(120, 40))
        self.btn1.setIcon(QIcon("Data/close.png"))
        self.btn1.setIconSize(QSize(41,35))
        self.btn1.clicked.connect(self.close)
        self.btn1.setStyleSheet("background:transparent;")
        self.btn1.resize(QSize(41, 25))
        self.imageComputer = QLabel()
        self.imageComputer.setPixmap(QPixmap("Data/Logo Long@2x.png").scaled(825 / 1.25, 303 / 1.25))
        self.btn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.hbox1=QHBoxLayout()
        self.hbox2=QVBoxLayout()
        self.hbox1.addWidget(self.imageComputer)
        self.hbox2.addWidget(self.btn1)
        self.hbox2.addStretch()
        self.hbox2.addSpacing(200)

        self.hbox1.setAlignment(Qt.AlignCenter)
        self.hbox2.setAlignment(Qt.AlignRight)
        self.mainvbox.addLayout(self.hbox2,2)
        self.mainvbox.addLayout(self.hbox1,10)
        self.mainvbox.addSpacing(25)
        self.mainvbox.addWidget(self.usnlabel,10)
        self.mainvbox.addSpacing(25)
        self.mainvbox.addWidget(self.usn,10)
        self.mainvbox.addSpacing(25)
        self.mainvbox.addWidget(self.passlabel,10)
        self.mainvbox.addSpacing(25)
        self.mainvbox.addWidget(self.passworde,10)
        self.mainvbox.addSpacing(25)
        self.mainvbox.addLayout(self.hbox,58)
        self.mainvbox.addStretch()

        self.btn.clicked.connect(self.login)

    def login(self):
        query = "SELECT Empid,Password,Type from employee"
        employees = cur.execute(query).fetchall()
        print(employees)
        data.id= self.usn.text()
        passw = self.passworde.text()
        flag = 0
        for employee in employees:
            if (data.id, passw) == (employee[0], employee[1]):
                data.type = employee[2]
                flag=1
        if flag==0:
            mbox = QMessageBox.information(self, "Information", "Wrong employee id or password")
        else:
            if data.type == 2:
                self.emplmain = empmain()
                self.close()
            if data.type == 1:
                self.admimain = admmain()
                self.close()



App = QApplication(sys.argv)
window = Loginwin()
sys.exit(App.exec())
