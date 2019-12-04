class Asteroid:
    def __init__(self, size, posX, posY, speed, direction):
        self.size = size
        self.posX = posX
        self.posY = posY
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

