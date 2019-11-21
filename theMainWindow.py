from PyQt5.QtWidgets import QMainWindow,QLabel,QApplication,QPushButton;
from PyQt5.QtGui import QImage,QPalette,QBrush,QFont
from PyQt5.QtCore import QSize,Qt
from math import sin,cos,radians;
import sys;
import msvcrt;

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

        self.show();


    def spaceHit(self):
        x = msvcrt.kbhit()

        if x:
            if x == 32:
                print("123");
        else:
            ret = False;

        return ret;


    def startGame(self):
        self.mode = "PLAYING";
        background = QImage("E:\FAKS\DRS\ProjekatAsteroid\images\space.jpg")
        background = background.scaled(750,750);
        palette = QPalette();
        palette.setBrush(QPalette.Window,QBrush(background));
        self.setPalette(palette);
        self.spaceShip = QPushButton(self)
        photo = QImage("E:\FAKS\DRS\ProjekatAsteroid\images\spaceShip.png");
        photo = photo.scaled(50,50);
        spaceShipIcon = QPalette();
        spaceShipIcon.setBrush(QPalette.Button,QBrush(photo));
        self.spaceShip.setFlat(True);
        self.spaceShip.setAutoFillBackground(True);
        self.spaceShip.setPalette(spaceShipIcon);
        self.spaceShip.setGeometry(350, 350, 50, 50);
        self.spaceShip.show();
        self.repaint();

    def rotate_point(point, angle, center_point=(0, 0)):
        """Rotates a point around center_point(origin by default)
        Angle is in degrees.
        Rotation is counter-clockwise
        """
        angle_rad = radians(angle % 360)
        # Shift the point so that center_point becomes the origin
        new_point = (point[0] - center_point[0], point[1] - center_point[1])
        new_point = (new_point[0] * cos(angle_rad) - new_point[1] * sin(angle_rad),
                     new_point[0] * sin(angle_rad) + new_point[1] * cos(angle_rad))
        # Reverse the shifting we have done
        new_point = (new_point[0] + center_point[0], new_point[1] + center_point[1])
        return new_point

    def rotate_shaceShip(self):
        rotatedX = self.rotate_point(self.spaceShip.x(),90,(self.spaceShip.x(),self.spaceShip.y()));
        rotatedY = self.rotate_point(self.spaceShip.y(),90,(self.spaceShip.x(),self.spaceShip.y()));
        self.spaceShip.move(rotatedX,rotatedY);

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Space and self.mode == "INITIATING":
            self.startGame();
            self.label.hide();
        if e.key() == Qt.Key_Up and self.mode == "PLAYING":
            self.spaceShip.move(self.spaceShip.x(),self.spaceShip.y() - 10);
        if e.key == Qt.Key_Left and self.mode == "PLAYING":
            self.rotate_shaceShip();

if __name__ == "__main__":
    app = QApplication(sys.argv);
    mainWindow = theMainWindow();
    sys.exit(app.exec_())
