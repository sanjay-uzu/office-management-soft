import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.qbtn = QPushButton('Quit', self)
        self.initUI()

    def initUI(self):
        self.qbtn.resize(self.qbtn.sizeHint())
        self.qbtn.move(50, 50)
        self.qbtn.clicked.connect(self.test)
        self.setGeometry(0, 0, 1024, 768)
        self.setWindowTitle('Quit button')
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.show()
    def test(self):
      self.qbtn.move(100,100)

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()