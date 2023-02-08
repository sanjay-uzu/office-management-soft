import sys

from PyQt5.QtCore import QSize,Qt
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap, QIcon
from PyQt5.QtWidgets import *
class Addeditequip(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500,800)
        self.setWindowTitle("Add edit Equipment")
        self.formLayout = QFormLayout()
        self.namelbl=QLabel("Name")
        self.name=QLineEdit()
        self.locationlbl=QLabel("Location")
        self.location=QLineEdit()
        self.hbox=QHBoxLayout()
        self.photo = QLabel(self)
        self.photo.resize(QSize(300, 300))
        self.photo.setPixmap(QPixmap("Data/test.png").scaled(300, 300))
        self.hbox.addWidget(self.photo)
        self.hbox.setAlignment(Qt.AlignCenter)
        self.Descriptionlbl=QLabel("Description")
        self.desc=QTextEdit()
        self.addbtn = QToolButton()
        self.addbtn.setIcon(QIcon("Data/btn.jpg"))
        self.addbtn.setIconSize(QSize(500, 500))
        self.addbtn.resize(QSize(415 / 2, 125 / 2))
        self.addbtn.setStyleSheet("background-color:transparent ; border-style:outset")
        self.formLayout.addRow(self.hbox)
        self.formLayout.addRow(self.namelbl,self.name)
        self.formLayout.addRow(self.locationlbl,self.location)
        self.formLayout.addRow(self.Descriptionlbl)
        self.formLayout.addRow(self.desc)
        self.formLayout.addRow(self.addbtn)
        self.setLayout(self.formLayout)
        self.show()
App=QApplication(sys.argv)
window=Addeditequip()
sys.exit(App.exec())
