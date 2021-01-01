import pygame
import os
import time
import random
from SpaceShip import *

## initaing the font
pygame.font.init()

## Setting the display window 
WIDTH, HEIGHT = 750, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders 1.0")

## Loading assets images
# Background
BACK_GROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

def main():
    # game variables
    Active = True
    lost = False
    lost_counter = 0
    Frames_Per_Second = 50
    lvl = 0
    main_font = pygame.font.SysFont("comicsans", 30)
    lost_font = pygame.font.SysFont("comicsans", 50)
    clock = pygame.time.Clock()
    
    # player variables
    lives = 500
    player_speed = 5
    # player = Player_Ship(int(WIDTH / 2), HEIGHT - int(11*PLAYER_SHIP.get_height()/10))
    player = Player_Ship(350, 400)
    laser_speed = 4
    
    # enemy variables    
    enemies = []
    wave_length = 0
    shooting_probability = 2    
    
    def redraw_window():
        # draw the Back Ground
        WINDOW.blit(BACK_GROUND,(0,0))
        # draw the font
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {lvl}", 1, (255, 255, 255))
        WINDOW.blit(lives_label, (10, 10))
        WINDOW.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        
        for enemy in enemies:
            enemy.draw(WINDOW)
            
        # draw the ship
        player.draw(WINDOW)
        # draw the lost label
        if lost == True:
            lost_label = lost_font.render(f"You Lost !!!", 1, (255, 255, 255))
            WINDOW.blit(lost_label, ((WIDTH - lost_label.get_width())/2, HEIGHT/2))
            
        pygame.display.update()
    
    while Active:
        clock.tick(Frames_Per_Second)
        redraw_window()
        
        # check if we lost and increase the counter
        if lives <= 0 or player.health <= 0:
            lost = True
            lost_counter += 1
        
        # lost label show for 3 seconde and quit
        if lost:
            if lost_counter > Frames_Per_Second * 3:
                Active = False
            else:
                continue

        
        # level && number of enemies update
        if len(enemies) == 0:
            lvl += 1
            wave_length += 5
            # respawn enemies
            for i in range(wave_length):
                enemy = Enemey_Ship(random.randrange(50, WIDTH - 50), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]), random.randrange(1, 5))
                enemies.append(enemy)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Active = False

        # movment keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_speed > 0:                              # left
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.x + player_speed + player.get_width() < WIDTH:    # right
            player.x += player_speed
        if keys[pygame.K_UP] and player.y - player_speed > 0:                                # up
            player.y -= player_speed
        if keys[pygame.K_DOWN] and player.y + player_speed + player.get_height() < HEIGHT:   # down
            player.y += player_speed
        if keys[pygame.K_SPACE]:                                                             # shoot
            player.shoot()
        
        # make the enemies move
        for enemy in enemies[:]:
            enemy.move()
            enemy.move_lasers(laser_speed, player)
            
            #randomize the enemy shooting 
            if random.randrange(0, shooting_probability*Frames_Per_Second) == 1:
                enemy.shoot()
            
            # check if the enemy ship got passed us
            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)
            
            # handle collisions
            
        # handle the player lasers movement     
        player.move_lasers(-laser_speed, enemies)
       
main()