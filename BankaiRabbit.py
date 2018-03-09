import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class BankaiRabbit(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")
    def paintEvent(self, e):
        p= QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,0,0))
        p.drawPolygon(
            QPoint(100,100), QPoint(125,100), QPoint(125, 150), QPoint(150, 150), QPoint(150, 100), QPoint(225, 100),
            QPoint(225, 125), QPoint(175, 125), QPoint(175, 150), QPoint(225, 150), QPoint(225, 225),
            QPoint(200, 225), QPoint(200, 175), QPoint(175, 175), QPoint(175, 225), QPoint(100, 225),
            QPoint(100, 200), QPoint(150, 200), QPoint(150, 175), QPoint(100, 175),
            )

        p.drawPixmap(QRect(200,100,320,320), self.rabbit)
        p.end()
def main():
    app = QApplication(sys.argv)
    w = BankaiRabbit()
    w.show()

    return app.exec_()
if __name__ == "__main__":
    sys.exit(main())