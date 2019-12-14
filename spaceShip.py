from PyQt5.QtCore import QPointF,QRectF,Qt,QThread
from PyQt5.QtGui import QVector2D,QPainter,QPen
from PyQt5.QtWidgets import QWidget
from math import ceil,sin,cos,radians;
from moveRotate import MOVE_ROTATE;

class SpaceShip(QThread):
    def __init__(self,x,y,color):
        super().__init__()
        self.x = x;
        self.y = y;
        self.width = 24.0;
        self.height = 32.0;
        self.color = (255, 25, 255);
        self.vector = QVector2D(QPointF(0.0,-1.0));
        self.velocity = 10;
        self.score = 0;
        self.rotatedFor = 0;
        self.lives = 3;
        self.color = color;
        self.isDead = False;
        self.colorOfProjectile = Qt.transparent;
        points = [
            QPointF(self.x, self.y - (self.height / 2.0)),
            QPointF(self.x - ((self.width / 2.0)), self.y + (self.height / 2.0)),
            QPointF(self.x, self.y + ((self.height / 4.0))),
            QPointF(self.x + (self.width / 2.0), self.y + (self.height / 2.0)),

        ]

        self.points = points;
        self.projectile = 0;
        self.reloadProjectile();
    def reloadProjectile(self):
        self.projectile = QPointF(self.points[0]);
        self.colorOfProjectile = Qt.transparent;

    def die(self):
        self.x = 350;
        self.y = 350;
        self.lives -= 1;
        self.points = [
            QPointF(self.x, self.y - (self.height / 2.0)),
            QPointF(self.x - ((self.width / 2.0)), self.y + (self.height / 2.0)),
            QPointF(self.x, self.y + ((self.height / 4.0))),
            QPointF(self.x + (self.width / 2.0), self.y + (self.height / 2.0)),

        ]

        print(self.color.__str__() + " spaceshipu ostalo jos: " + self.lives.__str__() + " zivota");

    def move(self):
       # print(self.x.__str__() + "+= " + self.vector.x().__str__() + "*" + self.velocity.__str__())
       # print(self.y.__str__() + "+= " + self.vector.y().__str__() + "*" + self.velocity.__str__())

       if(self.x > 750):
           self.x = 0;
       elif(self.x < 0):
           self.x = 750;
       if(self.y > 750):
           self.y = 0;
       elif(self.y < 0):
           self.y = 750;
       self.x += self.vector.x() * self.velocity
       self.y += self.vector.y() * self.velocity

       self.points = [
            QPointF(self.x, self.y - (self.height / 2.0)),
            QPointF(self.x - ((self.width / 2.0)), self.y + (self.height / 2.0)),
            QPointF(self.x, self.y + ((self.height / 4.0))),
            QPointF(self.x + (self.width / 2.0), self.y + (self.height / 2.0))
        ]

       i = 0;


       for point in self.points:
           (x,y) = self.rotate_point(point,self.rotatedFor,MOVE_ROTATE.MOVE,(self.x,self.y));
           self.points[i] = QPointF(x,y);
           i += 1;
       #print("X: " + self.x.__str__() + "Y: " +  self.y.__str__());





    def rotate(self,point,angle):
        angle = radians(angle % 360)
        point = (point[0] * cos(angle) - point[1] * sin(angle),
                 point[0] * sin(angle) + point[1] * cos(angle))
        return point

    def rotate_point(self,point, angle, moveOrRotate,center_point=(0, 0)):
        if (moveOrRotate == MOVE_ROTATE.ROTATE):
            self.rotatedFor += angle / 4;

        pointX = point.x() - center_point[0]
        pointY = point.y() - center_point[1];
        new_point = (pointX, pointY)
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



