import sqlite3
import sys
from functools import partial

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import data
import Meetings
con = sqlite3.connect('meetings.db')
cur = con.cursor()
list=None
i=0


styleSheet = """
      QPushButton{
      border:5px solid;
      border-width:1px;
      border-radius:5px;
      min-height:30px;
      min-width:100px;
      }      
      """
styleSheet1 = """
      QPushButton{
      background:#fac34b;
      border:5px solid;
      border-width:1px;
      border-radius:5px;
      min-height:30px;
      min-width:100px;
      }      
      """


class book(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600,100,800,700)
        self.setWindowTitle("Please Select Your Time Slot")
        self.show()
        self.layouts()
        self.widgets()
        self.setStyleSheet(styleSheet)
        self.meetings = []


    def layouts(self):
        self.mainvbox=QVBoxLayout()
        self.mainhbox=QHBoxLayout()
        self.vbox=QVBoxLayout()
        self.hbox=QHBoxLayout()
        self.savebtn=QPushButton("Save")
        self.savebtn.setStyleSheet(styleSheet1)
        self.hbox.addWidget(self.savebtn)
        self.hbox.setAlignment(Qt.AlignCenter)
        self.mainmainvbox=QVBoxLayout()
        self.mainmainvbox.addLayout(self.mainvbox)
        self.mainmainvbox.addLayout(self.hbox)
        self.mainhbox.setAlignment(Qt.AlignCenter)
        self.mainvbox.setAlignment(Qt.AlignCenter)
        self.mainhbox.addLayout(self.vbox)
        self.mainhbox.addLayout(self.mainmainvbox)
        self.setLayout(self.mainhbox)
        self.mainhbox.setContentsMargins(0,0,0,0)
        self.mainvbox.setSpacing(0)
        self.vbox.setSpacing(16)
        self.mainhbox.setSpacing(10)

    def widgets(self):
        self.lbl1=QLabel("0-1")
        self.lbl2=QLabel("1-2")
        self.lbl3=QLabel("2-3")
        self.lbl4=QLabel("3-4")
        self.lbl5=QLabel("4-5")
        self.lbl6=QLabel("5-6")
        self.lbl7=QLabel("6-7")
        self.lbl8=QLabel("7-8")
        self.lbl9=QLabel("8-9")
        self.lbl10=QLabel("9-10")
        self.lbl12=QLabel("10-11")
        self.lbl13=QLabel("11-12")
        self.lbl14=QLabel("12-13")
        self.lbl15=QLabel("13-14")
        self.lbl16=QLabel("14-15")
        self.lbl17=QLabel("15-16")
        self.lbl18=QLabel("16-17")
        self.lbl19=QLabel("17-18")
        self.lbl20=QLabel("18-19")
        self.lbl21=QLabel("19-20")
        self.lbl22=QLabel("20-21")
        self.lbl23=QLabel("21-22")
        self.lbl24=QLabel("22-23")
        self.lbl25=QLabel("23-24")
        self.lbl1.setAlignment(Qt.AlignRight)
        self.lbl2.setAlignment(Qt.AlignRight)
        self.lbl3.setAlignment(Qt.AlignRight)
        self.lbl4.setAlignment(Qt.AlignRight)
        self.lbl5.setAlignment(Qt.AlignRight)
        self.lbl6.setAlignment(Qt.AlignRight)
        self.lbl7.setAlignment(Qt.AlignRight)
        self.lbl8.setAlignment(Qt.AlignRight)
        self.lbl9.setAlignment(Qt.AlignRight)
        self.lbl10.setAlignment(Qt.AlignRight)
        self.lbl12.setAlignment(Qt.AlignRight)
        self.lbl13.setAlignment(Qt.AlignRight)
        self.lbl14.setAlignment(Qt.AlignRight)
        self.lbl15.setAlignment(Qt.AlignRight)
        self.lbl16.setAlignment(Qt.AlignRight)
        self.lbl17.setAlignment(Qt.AlignRight)
        self.lbl18.setAlignment(Qt.AlignRight)
        self.lbl19.setAlignment(Qt.AlignRight)
        self.lbl20.setAlignment(Qt.AlignRight)
        self.lbl21.setAlignment(Qt.AlignRight)
        self.lbl22.setAlignment(Qt.AlignRight)
        self.lbl23.setAlignment(Qt.AlignRight)
        self.lbl24.setAlignment(Qt.AlignRight)
        self.lbl25.setAlignment(Qt.AlignRight)
        self.vbox.addWidget(self.lbl1)
        self.vbox.addWidget(self.lbl2)
        self.vbox.addWidget(self.lbl3)
        self.vbox.addWidget(self.lbl4)
        self.vbox.addWidget(self.lbl5)
        self.vbox.addWidget(self.lbl6)
        self.vbox.addWidget(self.lbl7)
        self.vbox.addWidget(self.lbl8)
        self.vbox.addWidget(self.lbl9)
        self.vbox.addWidget(self.lbl10)
        self.vbox.addWidget(self.lbl12)
        self.vbox.addWidget(self.lbl13)
        self.vbox.addWidget(self.lbl14)
        self.vbox.addWidget(self.lbl15)
        self.vbox.addWidget(self.lbl16)
        self.vbox.addWidget(self.lbl17)
        self.vbox.addWidget(self.lbl18)
        self.vbox.addWidget(self.lbl19)
        self.vbox.addWidget(self.lbl20)
        self.vbox.addWidget(self.lbl21)
        self.vbox.addWidget(self.lbl22)
        self.vbox.addWidget(self.lbl23)
        self.vbox.addWidget(self.lbl24)
        self.vbox.addWidget(self.lbl25)
        self.vbox.addStretch()
        self.mainvbox.addStretch()
        self.btns=[]
        self.i=0
        while self.i<26:
            self.btns.append(0)
            self.i=self.i+1
        self.i=1
        print(self.btns)
        while self.i<25:
            print(self.i)
            self.btns[self.i]=QPushButton()
            print(self.i)
            self.mainvbox.addWidget(self.btns[self.i])
            self.btns[self.i].clicked.connect(partial(self.btnclick,self.i))
            self.i=self.i+1
            print(self.i)
        self.mainvbox.addStretch()
        self.savebtn.clicked.connect(self.save)
        self.display()
    def display(self):
        global list
        list=[]
        print("in here")
        query = "SELECT list from meetings WHERE date=?;"
        employees = cur.execute(query, (data.date,)).fetchall()
        print("in here")
        if employees!=[]:
            x=employees[-1]
            print("in here")
            print(x[0])
            print("in here")
            x=x[0]
            print("hi")
            self.j=0
            while self.j<len(x):
                list.append(int(x[self.j]))
                self.j=self.j+1
            i=1

            if x!=None:
                while i<25:
                    if x[i]=='1':
                        self.btns[i].setStyleSheet("background-color:red")
                        self.btns[i].setEnabled(False)
                    i=i+1
        else:
            h=0
            while h<25:
                list.append(0)
                h=h+1

    def btnclick(self,i):
        global list
        print("in func")
        if list[i]==0:
            print("after1")
            print(i)
            self.meetings.append("{}-{}Hrs".format(i,i+1))
            print("after2")
            list[i]= 1
            print("after3")
            self.btns[i].setStyleSheet("background-color:green")
            print("after")

        else:
            self.btns[i].setStyleSheet("background-color:transparent")
            self.meetings.remove("{}-{}Hrs".format(i,i+1))
            list[i]=0

    def save(self):
        global list
        for i in range(len(list)):
            list[i]=str(list[i])
        self.meetings=','.join(self.meetings)
        self.meetings=str(self.meetings)
        list=''.join(list)
        print(list)
        print(data.room)
        print((self.meetings))
        list=str(list)
        print(type(list))
        print(type(data.id))
        print(type(data.date))
        print(type(data.room))
        query = "INSERT INTO meetings (empid,meetin,list,date,meetingroom) VALUES(?,?,?,?,?)"
        cur.execute(query, (data.id,self.meetings,list,data.date,data.room))
        print("OOK")
        con.commit()
        QMessageBox.information(self, "Success", "Meeting Added")
        self.close()



