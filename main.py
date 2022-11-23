import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPolygon
from random import randint
from clas import Ui_Ui
class Example(QMainWindow, Ui_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.a = False
        self.pushButton.clicked.connect(self.start)
        self.pushButton.clicked.connect(self.update)

    def drawing(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        a = randint(1, 300)
        b = randint(1, 800 - a // 2)
        c = randint(1, 600 - a // 2)
        qp.drawEllipse(b, c, a, a)

    def paintEvent(self, event):
        if self.a:
            qp = QPainter()
            qp.begin(self)
            self.drawing(qp)
            qp.end()

    def start(self):
        self.a = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

