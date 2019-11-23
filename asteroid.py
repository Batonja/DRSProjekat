class Asteroid:
    def __init__(self, size, posX, posY, speed, direction):
        self.size = size
        self.posX = posX
        self.posY = posY
        self.speed = speed
        #0 - UP, 1 - DOWN
        self.direction = direction