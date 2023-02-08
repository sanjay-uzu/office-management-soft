import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def mousePressEvent(self, QMouseEvent):
        x=str(QMouseEvent.pos())
        x=x.split('(')
        x=x[-1]
        x=x[0:-1]
        x=x.split(",")
        posx=int(x[0])
        posy=int(x[1])
        print(x)
    def initUI(self):
        qbtn =QPushButton('Quit', self)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(0, 0, 1024, 768)
        self.setWindowTitle('Quit button')
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.show()
    def test(self):
      print("test")

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()