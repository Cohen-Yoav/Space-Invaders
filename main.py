import pygame
import os
import time
import random
from SpaceShip import Ship

## initaing the font
pygame.font.init()

## Setting the display window 
WIDTH, HEIGHT = 750, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders 1.0")

## Loading assets images
# Space Ships
ENEMY_RED_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
ENEMY_GREEN_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
ENEMY_BLUE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
PLAYER_YELLOW_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# lasers
ENEMY_RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
ENEMY_GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
ENEMY_BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
PLAYER_YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background
BACK_GROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

def main():
    Active = True
    Frames_Per_Second = 50
    lvl = 1
    lives = 5
    player_speed = 5
    
    main_font = pygame.font.SysFont("comicsans", 30)
    
    ship = Ship(350, 420)
    
    clock = pygame.time.Clock()
    
    def redraw_window():
        # draw the Back Ground
        WINDOW.blit(BACK_GROUND,(0,0))
        # draw the font
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {lvl}", 1, (255, 255, 255))
        WINDOW.blit(lives_label, (10, 10))
        WINDOW.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        # draw the ship
        ship.draw(WINDOW)
        
        pygame.display.update()
    
    while Active:
        clock.tick(Frames_Per_Second)
        redraw_window()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Active = False

        # movment keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and ship.x - player_speed > 0:              # left
            ship.x -= player_speed
        if keys[pygame.K_RIGHT] and ship.x + player_speed + 50 < WIDTH:    # right
            ship.x += player_speed
        if keys[pygame.K_UP] and ship.y - player_speed > 0:                # up
            ship.y -= player_speed
        if keys[pygame.K_DOWN] and ship.y + player_speed + 50 < HEIGHT:    # down
            ship.y += player_speed
        
main()