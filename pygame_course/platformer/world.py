import pygame
from constants import *
from player import Player
from enemy import Enemy
from exit import Exit
class World:
    def __init__(self, tile_map, player_group, enemy_group, exit_group):
        self.tile_list = []
        self.player_group = player_group
        self.enemy_group = enemy_group
        self.exit_group = exit_group
        self.image = pygame.image.load("assets/background.png")
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect(topleft = (0,0))

        for row in range(len(tile_map)):
            for col in range(len(tile_map[row])):
                if tile_map[row][col] == 1:
                    img = DIRT_IMG
                    img_rect = img.get_rect(topleft=(col*TILE_SIZE, row * TILE_SIZE))
                    self.tile_list.append((img, img_rect))
                if tile_map[row][col] == 2:
                    img = GRASS_IMG
                    img_rect = img.get_rect(topleft=(col*TILE_SIZE, row * TILE_SIZE))
                    self.tile_list.append((img, img_rect))
                if tile_map[row][col] == 3:
                    enemy = Enemy(col*TILE_SIZE, row * TILE_SIZE)
                    self.enemy_group.add(enemy)
                if tile_map[row][col] == 4:
                    img = WATER_IMG
                    img_rect = img.get_rect(topleft=(col*TILE_SIZE, row * TILE_SIZE))
                    self.tile_list.append((img, img_rect))

                if tile_map[row][col] == 5:
                    player = Player(col*TILE_SIZE, row * TILE_SIZE)
                    self.player_group.add(player)
                if tile_map[row][col] == 6:
                    exit = Exit(EXIT_IMG,col*TILE_SIZE, row * TILE_SIZE)
                    self.exit_group.add(exit)




    def draw(self,screen):
        screen.blit(self.image, self.rect)
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])