from PyQt5.QtWidgets import QMainWindow,QLabel,QApplication,QPushButton;
from PyQt5.QtGui import QImage,QPalette,QBrush,QFont,QPainter, QPixmap
from PyQt5.QtCore import QSize,Qt,QPointF,QThread, pyqtSignal
from math import sin,cos,radians;
from spaceShip import SpaceShip;
import sys;
import sys, time;
from asteroid import Asteroid
from random import randrange, randint

asteroids = []
asteroidLabels = []

class AsteroidsThread(QThread):
    signal = pyqtSignal()

    def run(self):
        count = 0
        while True:
            count += 1
            time.sleep(0.07)
            for a in asteroids:
                if a.direction == 0:
                    a.posX = a.posX + a.speed
                    a.posY = a.posY + a.speed
                else:
                    a.posX = a.posX - a.speed
                    a.posY = a.posY - a.speed

            self.signal.emit()

green = (0,70,0);
class theMainWindow(QMainWindow):
    def __init__(self):
        super().__init__();

        self.smallAsteroidPixMap = QPixmap('./images/asteroid1.png').scaled(40, 40)
        self.mediumAsteroidPixMap = QPixmap('./images/asteroid1.png').scaled(60, 60)
        self.bigAsteroidPixMap = QPixmap('./images/asteroid1.png').scaled(80, 80)
        self.asteroidCount = 20

        self.initUI();

    def initUI(self):
        self.mode = "INITIATING";
        self.setGeometry(200,200,750,750);
        background = QImage("./images/start_page.webp")
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
        qp.drawLine(self.spaceShip.points[3], self.spaceShip.points[0]);
        qp.drawLine(self.spaceShip.points[2], self.spaceShip.points[0]);

    def startGame(self):
        self.mode = "PLAYING";
        background = QImage("./images/space.jpg")
        background = background.scaled(750,750);
        palette = QPalette();
        palette.setBrush(QPalette.Window,QBrush(background));
        self.setPalette(palette);
        self.repaint()




    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Space and self.mode == "INITIATING":
            self.startGame();
            self.startAsteroids()
            self.label.hide();
        if e.key() == Qt.Key_Up and self.mode == "PLAYING":
            self.spaceShip.move();
            self.repaint();
        if (e.key() == Qt.Key_Left and self.mode == "PLAYING") or (e.key() == Qt.Key_Right and self.mode == "PLAYING"):
            i = 0;
            angle = 0;
            if(e.key() == Qt.Key_Left):
                angle = -10;
            else:
                angle = 10

            for point in self.spaceShip.points:
                (x,y) = self.spaceShip.rotate_point(point,angle,(self.spaceShip.x,self.spaceShip.y))
                self.spaceShip.points[i] = QPointF(x,y);
                i += 1;

            self.spaceShip.vector =  self.spaceShip.rotate(self.spaceShip.vector,angle);

            self.repaint();

    def startAsteroids(self):
        self.createAsteroids()
        self.thread = AsteroidsThread()
        self.thread.signal.connect(self.update)
        self.thread.start()

    def update(self):
        for l in asteroidLabels:
            l.hide()

        for i in range(len(asteroids)):
            # provera da li je asteroid izasao iz prozora
            if asteroids[i].posX > self.frameGeometry().height():
                asteroids[i].posX = 0
            elif asteroids[i].posX <= 0:
                asteroids[i].posX = 750
            if asteroids[i].posY > self.frameGeometry().width():
                asteroids[i].posY = 0
            elif asteroids[i].posY <= 0:
                asteroids[i].posY = 750
            asteroidLabels[i].setGeometry(asteroids[i].posX, asteroids[i].posY, 100, 100)
            asteroidLabels[i].show()

    def createAsteroids(self):
        for a in range(self.asteroidCount):
            randomDirection = randint(0, 1)

            posX = randrange(1, 750)
            posY = randrange(1, 750)

            posY = randrange(1, 750)
            size = randrange(1, 4)
            asteroid = Asteroid(size, posX, posY, 3, randomDirection)
            asteroids.append(asteroid)
            lab = QLabel(self)
            if size == 1:
                lab.setPixmap(self.smallAsteroidPixMap)
            elif size == 2:
                lab.setPixmap(self.mediumAsteroidPixMap)
            else:
                lab.setPixmap(self.bigAsteroidPixMap)

            lab.setGeometry(posX, posY, 100, 100)
            asteroidLabels.append(lab)
            print(posX)
            print(posY)
        self.showAsteroids()

    def showAsteroids(self):
        for l in asteroidLabels:
            l.show()

if __name__ == "__main__":
    app = QApplication(sys.argv);
    mainWindow = theMainWindow();
    sys.exit(app.exec_())
