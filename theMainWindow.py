from PyQt5.QtWidgets import QMainWindow,QLabel,QApplication,QPushButton;
from PyQt5.QtGui import QImage,QPalette,QBrush,QFont,QPainter
from PyQt5.QtCore import QSize,Qt,QPointF
from math import sin,cos,radians;
from spaceShip import SpaceShip;
import sys;


green = (0,70,0);
class theMainWindow(QMainWindow):
    def __init__(self):
        super().__init__();
        self.initUI();

    def initUI(self):
        self.mode = "INITIATING";
        self.setGeometry(200,200,750,750);
        background = QImage("E:\FAKS\DRS\ProjekatAsteroid\images\start_page.webp")
        background = background.scaled(QSize(750,750));

        palette = QPalette();
        palette.setBrush(QPalette.Window,QBrush(background))
        self.setPalette(palette);
        self.label = QLabel("Press space to play", self);

        self.label.move(250, 650);
        self.label.setFixedSize(750,100);
        self.label.setFont(QFont("Times new roman",25))
        self.label.setStyleSheet("color:white")
        self.spaceShip = SpaceShip(350,350);
        self.show();

    def paintEvent(self, e):
        qp = QPainter();
        qp.begin(self);
        qp.setBrush(QBrush(Qt.darkGreen));
        qp.drawLine(self.spaceShip.points[0], self.spaceShip.points[1]);
        qp.drawLine(self.spaceShip.points[1], self.spaceShip.points[2]);
        qp.drawLine(self.spaceShip.points[2], self.spaceShip.points[3]);
        qp.drawLine(self.spaceShip.points[3], self.spaceShip.points[4]);
        qp.drawLine(self.spaceShip.points[5], self.spaceShip.points[0]);

    def startGame(self):
        self.mode = "PLAYING";
        background = QImage("E:\FAKS\DRS\ProjekatAsteroid\images\space.jpg")
        background = background.scaled(750,750);
        palette = QPalette();
        palette.setBrush(QPalette.Window,QBrush(background));
        self.setPalette(palette);

        self.repaint();

    def rotate_point(self,point, angle, center_point=(0, 0)):
        """Rotates a point around center_point(origin by default)
        Angle is in degrees.
        Rotation is counter-clockwise
        """
        print(point);
        angle_rad = radians(angle % 360)

        # Shift the point so that center_point becomes the origin
        new_point = (point.x() - center_point[0], point.y() - center_point[1])
        new_point = (new_point[0] * cos(angle_rad) - new_point[1] * sin(angle_rad),
                     new_point[0] * sin(angle_rad) + new_point[1] * cos(angle_rad))
        # Reverse the shifting we have done
        new_point = (new_point[0] + center_point[0], new_point[1] + center_point[1])

        return new_point

    def rotate_spaceship(self):
        (x,y) = self.rotate_point()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Space and self.mode == "INITIATING":
            self.startGame();
            self.label.hide();
        if e.key() == Qt.Key_Up and self.mode == "PLAYING":
            self.spaceShip.move(self.spaceShip.x(),self.spaceShip.y() - 10);
        if (e.key() == Qt.Key_Left and self.mode == "PLAYING") or (e.key() == Qt.Key_Right and self.mode == "PLAYING"):
            i = 0;
            angle = 0;
            if(e.key() == Qt.Key_Left):
                angle = -10;
            else:
                angle = 10

            for point in self.spaceShip.points:
                (x,y) = self.rotate_point(point,angle,(self.spaceShip.x,self.spaceShip.y))
                self.spaceShip.points[i] = QPointF(x,y);
                i += 1;

            self.repaint();

if __name__ == "__main__":
    app = QApplication(sys.argv);
    mainWindow = theMainWindow();
    sys.exit(app.exec_())
