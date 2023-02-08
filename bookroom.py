import sqlite3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import data

con = sqlite3.connect('meetings.db')
cur = con.cursor()
list=[]
i=0

while i<26:
    list.append(0)
    i=i+1
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
        self.btn1=QPushButton("")
        self.btn2=QPushButton("")
        self.btn3=QPushButton("")
        self.btn4=QPushButton("")
        self.btn5=QPushButton("")
        self.btn6=QPushButton("")
        self.btn7=QPushButton("")
        self.btn8=QPushButton("")
        self.btn9=QPushButton("")
        self.btn10=QPushButton("")
        self.btn11=QPushButton("")
        self.btn12=QPushButton("")
        self.btn13=QPushButton("")
        self.btn14=QPushButton("")
        self.btn15=QPushButton("")
        self.btn16=QPushButton("")
        self.btn17=QPushButton("")
        self.btn18=QPushButton("")
        self.btn19=QPushButton("")
        self.btn20=QPushButton("")
        self.btn21=QPushButton("")
        self.btn22=QPushButton("")
        self.btn23=QPushButton("")
        self.btn24=QPushButton("")
        self.mainvbox.addWidget(self.btn1)
        self.mainvbox.addWidget(self.btn2)
        self.mainvbox.addWidget(self.btn3)
        self.mainvbox.addWidget(self.btn4)
        self.mainvbox.addWidget(self.btn5)
        self.mainvbox.addWidget(self.btn6)
        self.mainvbox.addWidget(self.btn7)
        self.mainvbox.addWidget(self.btn8)
        self.mainvbox.addWidget(self.btn9)
        self.mainvbox.addWidget(self.btn10)
        self.mainvbox.addWidget(self.btn11)
        self.mainvbox.addWidget(self.btn12)
        self.mainvbox.addWidget(self.btn13)
        self.mainvbox.addWidget(self.btn14)
        self.mainvbox.addWidget(self.btn15)
        self.mainvbox.addWidget(self.btn16)
        self.mainvbox.addWidget(self.btn17)
        self.mainvbox.addWidget(self.btn18)
        self.mainvbox.addWidget(self.btn19)
        self.mainvbox.addWidget(self.btn20)
        self.mainvbox.addWidget(self.btn21)
        self.mainvbox.addWidget(self.btn22)
        self.mainvbox.addWidget(self.btn23)
        self.mainvbox.addWidget(self.btn24)
        self.mainvbox.addStretch()
        self.btn1.clicked.connect(self.btnclick1)
        self.btn2.clicked.connect(self.btnclick2)
        self.btn3.clicked.connect(self.btnclick3)
        self.btn4.clicked.connect(self.btnclick4)
        self.btn5.clicked.connect(self.btnclick5)
        self.btn6.clicked.connect(self.btnclick6)
        self.btn7.clicked.connect(self.btnclick7)
        self.btn8.clicked.connect(self.btnclick8)
        self.btn9.clicked.connect(self.btnclick9)
        self.btn10.clicked.connect(self.btnclick10)
        self.btn11.clicked.connect(self.btnclick11)
        self.btn12.clicked.connect(self.btnclick12)
        self.btn13.clicked.connect(self.btnclick13)
        self.btn14.clicked.connect(self.btnclick14)
        self.btn15.clicked.connect(self.btnclick15)
        self.btn16.clicked.connect(self.btnclick16)
        self.btn17.clicked.connect(self.btnclick17)
        self.btn18.clicked.connect(self.btnclick18)
        self.btn19.clicked.connect(self.btnclick19)
        self.btn20.clicked.connect(self.btnclick20)
        self.btn21.clicked.connect(self.btnclick21)
        self.btn22.clicked.connect(self.btnclick22)
        self.btn23.clicked.connect(self.btnclick23)
        self.btn24.clicked.connect(self.btnclick24)
        self.savebtn.clicked.connect(self.save)



    def btnclick1(self):
        global list
        if list[1]==0:
            self.meetings.append("0-1AM")
            list[1]= 1
            self.btn1.setStyleSheet("background-color:green")
        else:
            self.btn1.setStyleSheet("background-color:transparent")
            self.meetings.remove("0-1AM")
            list[1]=0
    def btnclick2(self):
        global list
        if list[2]==0:
            self.meetings.append("1-2AM")
            list[2]= 1
            self.btn2.setStyleSheet("background-color:green")
        else:
            self.btn2.setStyleSheet("background-color:transparent")
            self.meetings.remove("1-2AM")
            list[2]=0
    def btnclick3(self):
        global list
        if list[3]==0:
            self.meetings.append("2-3AM")
            list[3]= 1
            self.btn3.setStyleSheet("background-color:green")
        else:
            self.btn3.setStyleSheet("background-color:transparent")
            self.meetings.remove("2-3AM")
            list[3]=0
    def btnclick4(self):
        global list
        if list[4]==0:
            self.meetings.append("3-4AM")
            list[4]= 1
            self.btn4.setStyleSheet("background-color:green")
        else:
            self.btn4.setStyleSheet("background-color:transparent")
            self.meetings.remove("3-4AM")
            list[4]=0
    def btnclick5(self):
        global list
        if list[5]==0:
            self.meetings.append("4-5AM")
            list[5]= 1
            self.btn5.setStyleSheet("background-color:green")
        else:
            self.btn5.setStyleSheet("background-color:transparent")
            self.meetings.remove("4-5AM")
            list[5]=0
    def btnclick6(self):
        global list
        if list[6]==0:
            self.meetings.append("5-6AM")
            list[6]= 1
            self.btn6.setStyleSheet("background-color:green")
        else:
            self.btn6.setStyleSheet("background-color:transparent")
            self.meetings.remove("5-6AM")
            list[6]=0
    def btnclick7(self):
        global list
        if list[7]==0:
            self.meetings.append("6-7AM")
            list[7]= 1
            self.btn7.setStyleSheet("background-color:green")
        else:
            self.btn7.setStyleSheet("background-color:transparent")
            self.meetings.remove("6-7AM")
            list[7]=0
    def btnclick8(self):
        global list
        if list[8]==0:
            self.meetings.append("7-8AM")
            list[8]= 1
            self.btn8.setStyleSheet("background-color:green")
        else:
            self.btn8.setStyleSheet("background-color:transparent")
            self.meetings.remove("7-8AM")
            list[8]=0
    def btnclick9(self):
        global list
        if list[9]==0:
            self.meetings.append("8-9AM")
            list[9]= 1
            self.btn9.setStyleSheet("background-color:green")
        else:
            self.btn9.setStyleSheet("background-color:transparent")
            self.meetings.remove("8-9AM")
            list[9]=0
    def btnclick10(self):
        global list
        if list[10]==0:
            self.meetings.append("9-10AM")
            list[10]= 1
            self.btn10.setStyleSheet("background-color:green")
        else:
            self.btn10.setStyleSheet("background-color:transparent")
            self.meetings.remove("9-10AM")
            list[10]=0
    def btnclick11(self):
        global list
        if list[11]==0:
            self.meetings.append("10-11AM")
            list[11]= 1
            self.btn11.setStyleSheet("background-color:green")
        else:
            self.btn11.setStyleSheet("background-color:transparent")
            self.meetings.remove("10-11AM")
            list[11]=0
    def btnclick12(self):
        global list
        if list[12]==0:
            self.meetings.append("11-12AM")
            list[12]= 1
            self.btn12.setStyleSheet("background-color:green")
        else:
            self.btn12.setStyleSheet("background-color:transparent")
            self.meetings.remove("11-12AM")
            list[12]=0
    def btnclick13(self):
        global list
        if list[13]==0:
            self.meetings.append("12-1PM")
            list[13]= 1
            self.btn13.setStyleSheet("background-color:green")
        else:
            self.btn13.setStyleSheet("background-color:transparent")
            self.meetings.remove("12-1PM")
            list[13]=0
    def btnclick14(self):
        global list
        if list[14]==0:
            self.meetings.append("1-2PM")
            list[14]= 1
            self.btn14.setStyleSheet("background-color:green")
        else:
            self.btn14.setStyleSheet("background-color:transparent")
            self.meetings.remove("1-2PM")
            list[14]=0
    def btnclick15(self):
        global list
        if list[15]==0:
            self.meetings.append("2-3PM")
            list[15]= 1
            self.btn15.setStyleSheet("background-color:green")
        else:
            self.btn15.setStyleSheet("background-color:transparent")
            self.meetings.remove("2-3PM")
            list[15]=0
    def btnclick16(self):
        global list
        if list[16]==0:
            self.meetings.append("3-4PM")
            list[16]= 1
            self.btn16.setStyleSheet("background-color:green")
        else:
            self.btn16.setStyleSheet("background-color:transparent")
            self.meetings.remove("3-4PM")
            list[16]=0
    def btnclick17(self):
        global list
        if list[17]==0:
            self.meetings.append("4-5PM")
            list[17]= 1
            self.btn17.setStyleSheet("background-color:green")
        else:
            self.btn17.setStyleSheet("background-color:transparent")
            self.meetings.remove("4-5PM")
            list[17]=0
    def btnclick18(self):
        global list
        if list[18]==0:
            self.meetings.append("5-6PM")
            list[18]= 1
            self.btn18.setStyleSheet("background-color:green")
        else:
            self.btn18.setStyleSheet("background-color:transparent")
            self.meetings.remove("5-6PM")
            list[18]=0
    def btnclick19(self):
        global list
        if list[19]==0:
            self.meetings.append("6-7PM")
            list[19]= 1
            self.btn19.setStyleSheet("background-color:green")
        else:
            self.btn19.setStyleSheet("background-color:transparent")
            self.meetings.remove("6-7PM")
            list[19]=0
    def btnclick20(self):
        global list
        if list[20]==0:
            self.meetings.append("7-8PM")
            list[20]= 1
            self.btn20.setStyleSheet("background-color:green")
        else:
            self.btn20.setStyleSheet("background-color:transparent")
            self.meetings.remove("7-8PM")
            list[20]=0
    def btnclick21(self):
        global list
        if list[21]==0:
            self.meetings.append("8-9PM")
            list[21]= 1
            self.btn21.setStyleSheet("background-color:green")
        else:
            self.btn21.setStyleSheet("background-color:transparent")
            self.meetings.remove("8-9PM")
            list[21]=0
    def btnclick22(self):
        global list
        if list[22]==0:
            self.meetings.append("9-10PM")
            list[22]= 1
            self.btn22.setStyleSheet("background-color:green")
        else:
            self.btn22.setStyleSheet("background-color:transparent")
            self.meetings.remove("9-10PM")
            list[22]=0
    def btnclick23(self):
        global list
        if list[23]==0:
            self.meetings.append("10-11PM")
            list[23]= 1
            self.btn23.setStyleSheet("background-color:green")
        else:
            self.btn23.setStyleSheet("background-color:transparent")
            self.meetings.remove("10-11PM")
            list[23]=0
    def btnclick24(self):
        global list
        if list[24]==0:
            self.meetings.append("11-12PM")
            list[24]= 1
            self.btn24.setStyleSheet("background-color:green")
        else:
            self.btn24.setStyleSheet("background-color:transparent")
            self.meetings.remove("11-12PM")
            list[24]=0

    def save(self):
        global list
        for i in range(len(list)):
            list[i]=str(list[i])
        self.meetings=','.join(self.meetings)
        self.meetings=str(self.meetings)
        print(data.room)
        list=''.join(list)
        query = "INSERT INTO meetings (empid,meetin,list,date,meetingroom) VALUES(?,?,?,?,?)"
        cur.execute(query, (data.id,self.meetings,list,data.date,data.room))
        con.commit()
        QMessageBox.information(self, "Success", "Meeting Added")
        self.close()



