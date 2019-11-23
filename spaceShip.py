from PyQt5.QtCore import QPointF,Qt;
from PyQt5.QtGui import QPainter,QBrush
from PyQt5.QtWidgets import QWidget
import math
class SpaceShip(QWidget):
    def __init__(self,x,y):
        super().__init__()
        self.x = x;
        self.y = y;
        self.width = 24.0;
        self.height = 32.0;
        self.color = (255, 25, 255);
        points = [
            QPointF(self.x, self.y - (self.height / 2.0)),
            QPointF(self.x - (math.ceil(self.width / 2.0)), self.y + math.ceil(self.height / 2.0)),
            QPointF(self.x, self.y + ((self.height / 4.0))),
            QPointF(self.x + math.ceil(self.width / 2.0), self.y + math.ceil(self.height / 2.0)),

        ]
        self.points = points;

    def mojeKoordinate(self):
        print("Koordinata X: " + self.x.__str__());
        print("Koordinata Y: " + self.y.__str__());
        print("Pointi:")
        for point in self.points:
            print("X: " + point.x().__str__() + "Y: "+ point.y().__str__())



