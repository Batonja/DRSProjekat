from PyQt5.QtWidgets import QMainWindow,QLabel,QApplication,QLineEdit,QPushButton;
from PyQt5.QtGui import QImage,QPalette,QBrush,QFont,QPainter, QPixmap,QPen
from PyQt5.QtCore import QSize,Qt,QPointF,QThread, pyqtSignal,QRect
from math import sin,cos,radians;
from spaceShip import SpaceShip;
import sys, time;
from pynput.keyboard import Key, Controller
from asteroid import Asteroid
from random import randrange, randint
from moveRotate import MOVE_ROTATE;
import multiprocessing
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
        self.labelPlayers = QLabel("Players",self);
        self.labelPlayers.move(320, 250)
        self.labelPlayers.setFont(QFont("Times new roman",25));
        self.labelPlayers.setFixedSize(300,200);
        self.labelPlayers.setStyleSheet("color:white")
        self.inputNumbers = QLineEdit(self)
        self.inputNumbers.setGeometry(450,345,25,20);
        self.rect = QRect(300,250,200,300);
        self.startButton = QPushButton("Start",self);
        self.startButton.setGeometry(305,490,190,50);
        self.startButton.clicked.connect(self.setPlayers)



        self.spaceShip = [SpaceShip(350,350,Qt.red),SpaceShip(350,350,Qt.green)]



        self.show();

    def setPlayers(self):
        if(self.inputNumbers.text() == '1' or self.inputNumbers.text() == '2'):
            self.startAsteroids()
            self.numberOfPlayers = self.inputNumbers.text();
            self.startGame();
            self.rect.setHeight(0);
            self.rect.setWidth(0);
            self.startButton.hide();
            self.labelPlayers.hide();
            self.inputNumbers.focusWidget().clearFocus();
            self.inputNumbers.hide();

            self.repaint();


    def paintEvent(self, e):
        qp = QPainter();
        qp.begin(self);

        qp.setPen(QPen(self.spaceShip[0].color));
        qp.drawLine(self.spaceShip[0].points[0], self.spaceShip[0].points[1]);
        qp.drawLine(self.spaceShip[0].points[1], self.spaceShip[0].points[2]);
        qp.drawLine(self.spaceShip[0].points[2], self.spaceShip[0].points[3]);
        qp.drawLine(self.spaceShip[0].points[3], self.spaceShip[0].points[0]);
        qp.drawLine(self.spaceShip[0].points[2], self.spaceShip[0].points[0]);

        qp.setPen(QPen(self.spaceShip[0].colorOfProjectile))
        qp.setBrush(QBrush(self.spaceShip[0].colorOfProjectile))
        qp.drawEllipse(self.spaceShip[0].projectile,5,5);

        if(self.spaceShip.__len__() == 2):
            qp.setPen(QPen(self.spaceShip[1].color));
            qp.drawLine(self.spaceShip[1].points[0], self.spaceShip[1].points[1]);
            qp.drawLine(self.spaceShip[1].points[1], self.spaceShip[1].points[2]);
            qp.drawLine(self.spaceShip[1].points[2], self.spaceShip[1].points[3]);
            qp.drawLine(self.spaceShip[1].points[3], self.spaceShip[1].points[0]);
            qp.drawLine(self.spaceShip[1].points[2], self.spaceShip[1].points[0]);
            qp.setPen(QPen(self.spaceShip[1].colorOfProjectile))
            qp.setBrush(QBrush(self.spaceShip[1].colorOfProjectile))
            qp.drawEllipse(self.spaceShip[1].projectile, 5, 5);
        qp.setBrush(QBrush(Qt.black));
        qp.drawRect(self.rect);

    def startGame(self):
        self.mode = "PLAYING";
        if(self.numberOfPlayers == '1'):
            del self.spaceShip[-1];
        background = QImage("./images/space.jpg")
        background = background.scaled(750,750);
        palette = QPalette();
        palette.setBrush(QPalette.Window,QBrush(background));
        self.setPalette(palette);
        self.repaint()


    def moveIt(self):
        for x in range(10):
            self.spaceShip.move();
            self.repaint();

    def rotate_spaceShip(self,angle,spaceShip):
        i = 0;
        for point in spaceShip.points:
            (x, y) = spaceShip.rotate_point(point, angle, MOVE_ROTATE.ROTATE,
                                                    (spaceShip.x, spaceShip.y))
            spaceShip.points[i] = QPointF(x, y);
            i += 1;
        (vecX, vecY) = spaceShip.rotate(spaceShip.vector, angle)
        spaceShip.vector.setX(vecX);
        spaceShip.vector.setY(vecY);

        return spaceShip;

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Up and self.mode == "PLAYING" and e.isAutoRepeat():
           # moving = multiprocessing.Process(target=self.moveIt(),args=()); preko threada
           # moving.start()
           self.spaceShip[0].move();
           self.repaint();
        if e.key() == Qt.Key_W and self.mode == "PLAYING" and self.spaceShip.__len__() == 2:
            # moving = multiprocessing.Process(target=self.moveIt(),args=()); preko threada
            # moving.start()
            self.spaceShip[1].move();
            self.repaint();
        if (e.key() == Qt.Key_Left and self.mode == "PLAYING") or (e.key() == Qt.Key_Right and self.mode == "PLAYING" ):
            angle = 0;
            if(e.key() == Qt.Key_Left):
                angle = -10;
            else:
                angle = 10

            self.spaceShip[0] = self.rotate_spaceShip(angle,spaceShip=self.spaceShip[0]);

            self.repaint();
        if ((e.key() == Qt.Key_A and self.mode == "PLAYING") or (e.key() == Qt.Key_D and self.mode == "PLAYING" )) and self.spaceShip.__len__() == 2:
            angle = 0;
            if(e.key() == Qt.Key_A):
                angle = -10;
            else:
                angle = 10
            self.spaceShip[1] = self.rotate_spaceShip(angle,spaceShip=self.spaceShip[1]);

            self.repaint();
        if(e.key() == Qt.Key_PageDown):
            self.shoot(self.spaceShip[0])
        if(e.key() == Qt.Key_Space and self.spaceShip.__len__() == 2):
            self.shoot(self.spaceShip[1])

    def shoot(self,ship):
        ship.colorOfProjectile = ship.color;
        ship.projectile = QPointF(ship.points[0]);

        while ((ship.projectile.x() < 760 and ship.projectile.x() > -10) and(ship.projectile.y() < 760 and ship.projectile.y() > -10))  :
            ship.projectile.setX(ship.projectile.x() + ship.vector.x() * ship.velocity/2);
            ship.projectile.setY(ship.projectile.y() + ship.vector.y() * ship.velocity/2);
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

        self.showAsteroids()

    def showAsteroids(self):
        for l in asteroidLabels:
            l.show()

if __name__ == "__main__":
    app = QApplication(sys.argv);
    mainWindow = theMainWindow();
    sys.exit(app.exec_())
