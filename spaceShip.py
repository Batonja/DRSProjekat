from PyQt5.QtCore import QPoint,Qt;
from PyQt5.QtGui import QPainter,QBrush
from PyQt5.QtWidgets import QWidget

class SpaceShip(QWidget):
    def __init__(self,x,y):
        super().__init__()
        self.x = x;
        self.y = y;
        self.width = 24;
        self.height = 32;
        self.color = (255, 25, 255);
        points = [
            QPoint(self.x, self.y - (self.height / 2)),
            QPoint(self.x - (self.width / 2), self.y + (self.height / 2)),
            QPoint(self.x, self.y + (self.height / 4)),
            QPoint(self.x + (self.width / 2), self.y + (self.height / 2)),
            QPoint(self.x, self.y - (self.height / 2)),
            QPoint(self.x, self.y + (self.height / 4)),
        ]
        self.points = points;




