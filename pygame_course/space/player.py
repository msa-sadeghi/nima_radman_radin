from pygame.sprite import Sprite
import pygame
from constants import *
from playerbullet import PlayerBullet

class Player(Sprite):
    def __init__(self, bullet_group):
        super().__init__()
        self.image = pygame.image.load("assets/player_ship.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.bottom = SCREEN_HEIGHT
        self.lives = 4
        self.player_fire_sound = pygame.mixer.Sound("assets/player_fire.wav")
        self.bullet_group = bullet_group

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        """
        به سمت چپ و راست
        """
        pass
    def fire(self):
        if len(self.bullet_group) <2:
            PlayerBullet(self.rect.centerx, self.rect.top, self.bullet_group)
            self.player_fire_sound.play()
