class Asteroid:
    def __init__(self, size, posX, posY, speed, direction):
        self.size = size
        self.posX = posX
        self.posY = posY
        self.posMinX = 0;
        self.posMaxX = 0
        self.posMinY = 0
        self.posMaxY = 0
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


    def asignMinAndMaxToAsteroid(self):
        self.posMinX = self.posX - 10;
        self.posMaxX = self.posX + 10;
        self.posMinY = self.posY - 10;
        self.posMaxY = self.posY + 10;

