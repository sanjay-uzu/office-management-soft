import sys
from PyQt5.QtWidgets import *
import sqlite3
import data
con = sqlite3.connect('empolyee.db')
cur = con.cursor()

class ResetPass(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(750,200,450,400)
        self.setWindowTitle("Reset Password")
        self.show()
        self.layouts()
        self.widgets()
    def layouts(self):
        self.mainvbox=QVBoxLayout()
        self.setLayout(self.mainvbox)
    def widgets(self):
        self.mainvbox.addStretch()
        self.usnlabel=QLabel("Enter Old Password:",self)
        self.passlabel=QLabel("Enter New Password",self)
        self.usn=QLineEdit(self)
        self.passworde=QLineEdit(self)
        self.btn=QPushButton("Reset",self)
        self.mainvbox.addWidget(self.usnlabel)
        self.mainvbox.addSpacing(25)
        self.mainvbox.addWidget(self.usn)
        self.mainvbox.addSpacing(25)
        self.mainvbox.addWidget(self.passlabel)
        self.mainvbox.addSpacing(25)
        self.mainvbox.addWidget(self.passworde)
        self.mainvbox.addSpacing(25)
        self.mainvbox.addWidget(self.btn)
        self.mainvbox.addStretch()
        self.btn.clicked.connect(self.reset)
    def reset(self):
        old=self.usn.text()
        passworde=self.passworde.text()
        query = "SELECT Password FROM employee WHERE Empid=?"
        employees = cur.execute(query, (data.id,)).fetchone()
        print(employees)
        if employees[0]==old:
            query = "UPDATE employee set Password=?  WHERE Empid=?"
            cur.execute(query, (passworde, data.id))
            con.commit()
            print(passworde)
            QMessageBox.information(self, "Success", "Password has been updated")
        else:
            QMessageBox.information(self, "Wrong", "Wrong Old password")



