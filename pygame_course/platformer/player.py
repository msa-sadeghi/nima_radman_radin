import pygame
from pygame.sprite import Sprite
from constants import *


class Player(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.right_images = []
        self.left_images = []
        self.idle_right_images = []
        self.idle_left_images = []
        for i in range(1, 9):
            image = pygame.image.load(f'assets/boy/Run ({i}).png')
            image = pygame.transform.scale(image, (image.get_width() * 0.2, image.get_height() * 0.2))
            self.right_images.append(image)
            image = pygame.transform.flip(image, True, False)
            self.left_images.append(image)
        for i in range(1, 10):
            image = pygame.image.load(f'assets/boy/Idle ({i}).png')
            image = pygame.transform.scale(image, (image.get_width() * 0.2, image.get_height() * 0.2))
            self.idle_right_images.append(image)
            image = pygame.transform.flip(image, True, False)
            self.idle_left_images.append(image)

        image = pygame.image.load('assets/boy/Idle (1).png')
        self.image = pygame.transform.scale(image, (image.get_width() * 0.2, image.get_height() * 0.2))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.dead_image = pygame.image.load("assets/img/ghost.png")
        self.reset(x,y)
    def reset(self,x,y):
        self.rect.topleft = (x, y)
        self.speed = 5
        self.vely = 0
        self.jumped = False
        self.counter = 0
        self.frame_index = 0
        self.direction = 1
        self.idle = True
        self.in_air = False
        self.game_status = "PLAYING"
    def update(self, tile_list, enemy_group):
        if self.game_status == "PLAYING":
            self.move(tile_list)
            self.animation()
            if pygame.sprite.spritecollide(self, enemy_group, False):
                self.game_status = "GAMEOVER"
        elif self.game_status == "GAMEOVER":
            self.image = self.dead_image
            if self.rect.top >= 200:
                self.rect.y -= 5

    def move(self, tile_list):
        # pygame.draw.rect(screen, (10, 245, 220), self.rect, 4)
        if self.direction == 1:
            rect = pygame.Rect(self.rect.x + 40, self.rect.y + 10, self.image.get_width() - 60,
                               self.image.get_height() - 20)
        if self.direction == -1:
            rect = pygame.Rect(self.rect.x + 20, self.rect.y + 10, self.image.get_width() - 60,
                               self.image.get_height() - 20)

        # pygame.draw.rect(screen, (245, 10, 220), rect, 4)

        dx = 0
        dy = 0
        self.counter += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dx -= self.speed
            self.idle = False
            self.direction = -1

        if keys[pygame.K_RIGHT]:
            dx += self.speed
            self.idle = False
            self.direction = 1

        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.idle = True

        if keys[pygame.K_SPACE] and not self.jumped and not self.in_air:
            self.vely = -15
            self.jumped = True

            self.in_air = True
        if not keys[pygame.K_SPACE]:
            self.jumped = False

        self.vely += 1
        dy += self.vely

        for tile in tile_list:
            if tile[1].colliderect(rect.x + dx, rect.y, self.image.get_width() - 60, self.image.get_height() - 20):
                if self.direction == 1:
                    dx = tile[1].left - rect.right
                if self.direction == -1:
                    dx = tile[1].right - rect.left

            if tile[1].colliderect(rect.x, rect.y + dy, self.image.get_width() - 60, self.image.get_height() - 20):
                if self.vely < 0:
                    dy = tile[1].bottom - rect.top
                    self.vely = 0
                else:
                    self.vely = 0
                    dy = tile[1].top - rect.bottom
                    self.in_air = False

        self.rect.x += dx
        self.rect.y += dy

    def animation(self):
        ANIMATION_COOLDOWN = 1
        if self.counter >= ANIMATION_COOLDOWN:
            self.counter = 0
            self.frame_index += 1
        if not self.idle:
            if self.frame_index >= len(self.right_images) - 1:
                self.frame_index = 0
            if self.direction == 1:
                self.image = self.right_images[self.frame_index]
            if self.direction == -1:
                self.image = self.left_images[self.frame_index]

        elif self.in_air:
            if self.direction == 1:
                self.image = self.idle_right_images[0]
            if self.direction == -1:
                self.image = self.idle_left_images[0]

        else:
            if self.frame_index >= len(self.idle_right_images) - 1:
                self.frame_index = 0
            if self.direction == 1:
                self.image = self.idle_right_images[self.frame_index]
            if self.direction == -1:
                self.image = self.idle_left_images[self.frame_index]
