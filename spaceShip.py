from PyQt5.QtCore import QPointF,Qt
from PyQt5.QtGui import QVector2D
from PyQt5.QtWidgets import QWidget
from math import ceil,sin,cos,radians;


class SpaceShip(QWidget):
    def __init__(self,x,y):
        super().__init__()
        self.x = x;
        self.y = y;
        self.width = 24.0;
        self.height = 32.0;
        self.color = (255, 25, 255);
        self.vector = QVector2D(0.0,-1.0);
        self.velocity = 1;
        points = [
            QPointF(self.x, self.y - (self.height / 2.0)),
            QPointF(self.x - ((self.width / 2.0)), self.y + (self.height / 2.0)),
            QPointF(self.x, self.y + ((self.height / 4.0))),
            QPointF(self.x + (self.width / 2.0), self.y + (self.height / 2.0)),

        ]
        self.points = points;

    def move(self):
        print(self.x.__str__() + "+= " + self.vector.x().__str__() + "*" + self.velocity.__str__())
        print(self.y.__str__() + "+= " + self.vector.y().__str__() + "*" + self.velocity.__str__())
        self.x += self.vector.x() * self.velocity
        self.y += self.vector.y() * self.velocity

        self.points = [
            QPointF(self.x, self.y - (self.height / 2.0)),
            QPointF(self.x - ((self.width / 2.0)), self.y + (self.height / 2.0)),
            QPointF(self.x, self.y + ((self.height / 4.0))),
            QPointF(self.x + (self.width / 2.0), self.y + (self.height / 2.0)),

        ]

    def rotate(self,point,angle):
        angle= radians(angle % 360)
        point = (point[0] * cos(angle) - point[1] * sin(angle),
                     point[0] * sin(angle) + point[1] * cos(angle))

        return point
    def rotate_point(self,point, angle, center_point=(0, 0)):
        """Rotates a point around center_point(origin by default)
        Angle is in degrees.
        Rotation is counter-clockwise
        """
        # Shift the point so that center_point becomes the origin
        new_point = (point.x() - center_point[0], point.y() - center_point[1])
        new_point = self.rotate(new_point,angle);
        # Reverse the shifting we have done
        new_point = (new_point[0] + center_point[0], new_point[1] + center_point[1])

        return new_point;

    def mojeKoordinate(self):
        print("Koordinata X: " + self.x.__str__());
        print("Koordinata Y: " + self.y.__str__());
        print("Pointi:")
        for point in self.points:
            print("X: " + point.x().__str__() + "Y: "+ point.y().__str__())



