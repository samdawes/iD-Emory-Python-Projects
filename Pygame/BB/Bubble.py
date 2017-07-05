#Complete Bubble Class
 
from pygame.locals import *
import pygame
 
class Bubble(pygame.sprite.Sprite):
    def __init__(self, a, b):
        super().__init__()
        self.image = pygame.Surface([40, 40])
        self.image = pygame.image.load("donut.png").convert_alpha()
        self.rect = self.image.get_rect(center=(40,40))
        self.rect.x = a
        self.rect.y = b
