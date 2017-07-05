import pygame
import sys
from pygame.locals import *
pygame.init()


#This is our enemy class. It's an asteroid!!!
##class Enemy(pygame.sprite.Sprite):
##    def __init__(self):
##        super().__init__()
##        #change filepath depending on image location
##        self.image = pygame.impage.load("roblox.png")
##        self.rect =self.image.get_rect(center=(10, 350))
##    def update(self):
##        self.rect.x += 5

screen = pygame.display.set_mode((640, 460))
pygame.display.set_caption("Roblox")
screen.fill((0, 0, 0))
character = pygame.image.load("roblox.png").convert_alpha()

def draw_screen():
    screen.fill((0, 0, 0))

while True:
    screen.blit(character, (50,50))

    draw_screen()
