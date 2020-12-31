import pygame

class Ship:
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self._lasers = []
        self.cool_down = 0
    
    def draw(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y, 50, 50), 0)
        # pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.ship_img.get.height() + 10), self.ship_img.get.width(), 10)
        # pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_img.get.height() + 10), self.ship_img.get.width() * (self.health / self.max_health), 10)