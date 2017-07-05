#Expand to see the platform class.
 
import pygame
 
class Platform(pygame.sprite.Sprite):
 
    image = None
 
    #When a platform is created, provide an x and
    #y position for it to be drawn at.
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = pygame.Rect(x, y, width, height)
