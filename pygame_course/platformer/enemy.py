from constants import *
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load("assets/img/blob.png")
        self.rect = self.image.get_rect(topleft = (x,y))
        self.direction = 1
        self.counter = 0

    def update(self):
        self.rect.x += self.direction
        self.counter += 1
        if self.counter > TILE_SIZE * 2:
            self.direction *= -1
            self.counter *= -1



