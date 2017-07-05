#Expand for the complete game class.
import pygame
import random
import math
import sys
#Import a coin, platform, and player.
from coinBase import Coin
from platformBase import Platform
from playerBase import Player
from pygame.locals import *
 
pygame.init()
 
screen = pygame.display.set_mode((640, 460))
background =  pygame.Surface((640, 460), 0, screen)
background.fill((255, 255, 255))
screen.blit(background, (0, 0))
font = pygame.font.SysFont(None, 36)
 
#Creates a group to hold platforms.
platforms = pygame.sprite.Group()
 
#Creates a Platform and adds it to the
#platform group. Add your own new
#platforms, or move these ones around!
platform1 = Platform(50, 150, 300, 20)
platforms.add(platform1)
platform2 = Platform(0, 300, 640, 20)
platforms.add(platform2)
 
#Creates a group to hold platforms.
coin_group = pygame.sprite.Group()
 
#Creates a Coin and adds it to the
#coin group. Add your own new
#coins, or move these ones around!
coin = Coin(100, 50)
coin_group.add(coin)
coin2 = Coin(10, 250)
coin_group.add(coin2)
coin3 = Coin(60, 250)
coin_group.add(coin3)
coin4 = Coin(110, 250)
coin_group.add(coin4)
coin5 = Coin(160, 50)
coin_group.add(coin5)
coin6 = Coin(210, 50)
coin_group.add(coin6)
 
#Variables that will control the player's x
#and y position.
x = 50
y = 50
speed = 5
 
#Creates a new player object.
player = Player(x, y)
 
#Creates a single group for drawing all
#of the sprites created.
draw_group = pygame.sprite.Group()
draw_group.add(player)
draw_group.add(platform1)
draw_group.add(platform2)
draw_group.add(coin)
draw_group.add(coin2)
draw_group.add(coin3)
draw_group.add(coin4)
draw_group.add(coin5)
draw_group.add(coin6)
 
def draw_text(display_string, font, surface, x_pos, y_pos):
    text_display = font.render(display_string, 1, (0, 0, 0))
    surface.blit(text_display, (x_pos, y_pos))
 
main_clock = pygame.time.Clock()
 
#Variables that control the players jumping.
jump_state = 0
jump_timer = 0
grounded = False
 
while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #Let's the player jump, only if they're
        #on the ground and press space.
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if jump_state == 0 and grounded:
                    jump_state = 1
 
    main_clock.tick(40)
 
    keys = pygame.key.get_pressed()
 
    if keys[K_a]:
        x -= speed
    if keys[K_d]:
        x += speed
 
    #Sets the player's position to be above the
    #platform they collided with.
    if grounded:
        #Makes sure the player is colliding with
        #a platform
        if pygame.sprite.spritecollideany(player, platforms) != None:
            sprite_rect = pygame.sprite.spritecollideany(player, platforms).rect
            y = sprite_rect.top - 45
 
    #For better understanding of this code, go
    #through the "Jumping" module.
    if jump_state == 0:
        if jump_timer == 0:
            if pygame.sprite.spritecollideany(player, platforms):
                grounded = True
            else:
                grounded = False
                y += 20
    elif jump_state == 1:
        jump_timer += main_clock.get_time()
        grounded = False
        y -= 20
        if jump_timer >= 275:
            jump_state = 2
    elif jump_state == 2:
        jump_timer = 0
        jump_state = 0
 
    screen.fill((255, 255, 255))
 
    #To understand this code better, go through
    #the "Pygame Sprite Class" module.
    collision_hit_list = pygame.sprite.spritecollide(player, coin_group, True)
 
    draw_group.clear(screen, background)
    draw_group.draw(screen)
 
    player.rect.y = y
    player.rect.x = x
    player.rect = pygame.Rect(x, y, player.rect.width, player.rect.height)
 
    pygame.display.update()
