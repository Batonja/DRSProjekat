class Asteroid:
    def __init__(self, size, posX, posY, speed, direction):
        self.size = size
        self.posX = posX
        self.posY = posY
        self.posMinX = 0;
        self.posMaxX = 0
        self.posMinY = 0
        self.posMaxY = 0
        self.theMiddleX = 0;
        self.theMiddleY = 0;
        self.whatSizeAmI = '';
        self.asignMinAndMaxToAsteroid();
        self.speed = speed
        self.points = 0
        #0 - UP, 1 - DOWN
        self.direction = direction
        if size == 1:
            self.points = 10
        elif size == 2:
            self.points = 20
        else:
            self.points = 10

    def calculateMyMiddle(self):
        if(self.whatSizeAmI == 'SMALL'):
            self.theMiddleX = self.posX + 20;
            self.theMiddleY = self.posY + 50;
        if(self.whatSizeAmI == "MEDIUM"):
            self.theMiddleX = self.posX + 30;
            self.theMiddleY = self.posY + 50;
        if(self.whatSizeAmI == "BIG"):
            self.theMiddleX = self.posX + 50;
            self.theMiddleY = self.posY + 50;

    def asignMinAndMaxToAsteroid(self):
        if(self.whatSizeAmI == 'SMALL'):
            self.posMinX = self.theMiddleX - 10;
            self.posMaxX = self.theMiddleX + 10;
            self.posMinY = self.theMiddleY - 10;
            self.posMaxY = self.theMiddleY + 10;
        elif(self.whatSizeAmI == 'MEDIUM'):
            self.posMinX = self.theMiddleX - 15;
            self.posMaxX = self.theMiddleX + 15;
            self.posMinY = self.theMiddleY - 15;
            self.posMaxY = self.theMiddleY + 15;
        elif(self.whatSizeAmI == 'BIG'):
            self.posMinX = self.theMiddleX - 20;
            self.posMaxX = self.theMiddleX + 20;
            self.posMinY = self.theMiddleY - 20;
            self.posMaxY = self.theMiddleY + 20;

