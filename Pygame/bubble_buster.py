import pygame
import sys
from pygame.locals import *
pygame.init()

#Initialize display size, caption, and color
screen = pygame.display.set_mode((640, 460))
pygame.display.set_caption("Bubble Buster!!!")
screen.fill((0, 128, 128))

#Player paddle
player= pygame.Rect(300, 400, 60, 10)
move_left = False
move_right = True

#Main Game Loop
while True:
    for event inpygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(screen, (0, 0, 0), player)
    pygame.display.update()


