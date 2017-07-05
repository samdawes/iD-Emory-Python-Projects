#Expand to see the player class.
 
import pygame
 
class Player(pygame.sprite.Sprite):
 
    image = None
 
    #When a player is created, provide an x and
    #y position for it to be drawn at.
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 50, 50)
        self.image = pygame.Surface([50, 50])
        self.image = pygame.image.load("paddle.png")
