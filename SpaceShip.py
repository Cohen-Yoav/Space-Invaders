import pygame
import os
from Lasers import Laser
WIDTH, HEIGHT = 750, 500

## Loading assets images
# Space Ships
ENEMY_RED_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
ENEMY_GREEN_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
ENEMY_BLUE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
PLAYER_SHIP = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png")), (50, 50))

# lasers
ENEMY_RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
ENEMY_GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
ENEMY_BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
PLAYER_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

class Ship:
    COOLDOWN = 30
    
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down = 0
    
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)
    
    def move_lasers(self, speed, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(speed)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)
        
    def get_width(self):
        return self.ship_img.get_width()
    
    def get_height(self):
        return self.ship_img.get_height()
    
    def shoot(self):
        if self.cool_down == 0:
            laser = Laser(self.x - int(self.get_width()/2), self.y - int(self.get_height()/2), self.laser_img)
            self.lasers.append(laser)
            self.cool_down = 1
            
    def cooldown(self):
        if self.cool_down >= self.COOLDOWN:
            self.cool_down = 0
        elif self.cool_down > 0:
            self.cool_down += 1
      
        
class Player_Ship(Ship):
    def __init__(self, x, y, health = 100):
        super().__init__(x, y, health)
        self.ship_img = PLAYER_SHIP
        self.laser_img = PLAYER_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        
    def move_lasers(self, speed, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(speed)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)
                        
    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.ship_img.get_height() + 5, self.ship_img.get_width(), 5))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_img.get_height() + 5, self.ship_img.get_width() * (self.health / self.max_health), 5))    

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)
    
    
class Enemey_Ship(Ship):
    COLOR_MAP = {
        "red" : (ENEMY_RED_SHIP, ENEMY_RED_LASER),
        "green" : (ENEMY_GREEN_SHIP, ENEMY_GREEN_LASER),
        "blue" : (ENEMY_BLUE_SHIP, ENEMY_BLUE_LASER)    
    }
    def __init__(self, x, y, color, speed, health = 100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img  = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.speed = speed
        
    def move(self):
        self.y += self.speed
    
    def get_speed(self):
        return self.speed
    
    def shoot(self):
        if self.cool_down == 0:
            x = self.ship_img.get_width()
            laser = Laser(self.x - int(self.ship_img.get_width()/5), self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down = 1