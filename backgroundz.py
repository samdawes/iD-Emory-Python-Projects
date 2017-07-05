import pygame
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640,460))
pygame.display.set_caption('hiiiii deep dish')
background_image = pygame.image.load("tupac.png").convert_alpha()
screen.fill((0, 0, 0))
screen.blit(background_image, (50, 50))

while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background_image, (50, 50))
    pygame.display.update()
