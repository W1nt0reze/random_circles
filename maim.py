import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.flag = False
        self.qp = QPainter()
        self.btn.clicked.connect(self.draw)
        self.coords = []

    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("Git и случайные окружности")
        self.btn = QPushButton('Создать окружность', self)
        self.btn.resize(150, 40)
        self.btn.move(185, 40)

    def draw(self):
        self.figure = 'circle'
        self.size = random.randint(10, 100)
        self.color = (random.randint(0, 225), random.randint(0, 255), random.randint(0, 255))
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp.begin(self)
            self.qp.setPen(QColor(*self.color))
            self.qp.setBrush(QColor(*self.color))
            self.x = random.randint(100, 400)
            self.y = random.randint(100, 400)
            if self.figure == 'circle':
                self.qp.drawEllipse(self.x, self.y, self.size, self.size)
            self.qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())