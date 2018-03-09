import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Drawing")
        self.teletubbies = QPixmap("images/Teletubbies.png")
    def paintEvent(self, e):
        p= QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(128,128,128))
        p.drawPolygon(QPoint(90,100), QPoint(110,100), QPoint(110,200), QPoint(90,200))

        p.setPen(QColor(255,127,0))
        p.setBrush(QColor(220,20,60))
        p.drawPolygon(QPoint(50,200), QPoint(150,200), QPoint(100,400))

        p.drawPixmap(QRect(200,100,320,320), self.teletubbies)
        p.end()
def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window2()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())