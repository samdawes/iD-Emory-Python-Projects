#Expand to see the coin class.
 
import pygame
 
class Coin(pygame.sprite.Sprite):
 
    image = None
 
    #When a coin is created, provide an x and
    #y position for it to be drawn at.
    def __init__(self, x, y):
        super().__init__()
        self.image = self.image = pygame.Surface([20, 20])
        self.image.fill((185, 100, 0))
        self.rect = pygame.Rect(x, y, 20, 20)
