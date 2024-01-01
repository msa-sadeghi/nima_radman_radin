from pygame.sprite import Sprite
import pygame

class Enemy(Sprite):
    def __init__(self, x, y, bullet_group):
        super().__init__()
        self.image = pygame.image.load("assets/alien.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.velocity = 3
        self.direction = 1
        self.bullet_group = bullet_group

    def update(self):
        self.rect.x += self.direction * self.velocity

        