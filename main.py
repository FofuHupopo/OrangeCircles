import sys
import random
import time

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5 import uic


class OCWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('UI.ui', self)
        
        self.pushButton.clicked.connect(self.btn_clicked)
        self.draw_circle = False
        
    def btn_clicked(self):
        button = self.sender()
        self.draw_circle = True
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.yellow, 3, Qt.SolidLine))

        if self.draw_circle:
            for i in range(random.randint(5, 20)):
                radius = random.randint(10, 100)
                x_coords = random.randint(0, 600)
                y_coords = random.randint(0, 400)

                painter.drawEllipse(x_coords, y_coords, radius, radius)

            self.draw_circle = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OCWindow()
    ex.show()
    sys.exit(app.exec_())
