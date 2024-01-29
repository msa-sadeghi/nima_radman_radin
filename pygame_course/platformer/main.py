import pygame
from constants import *
from world import World
from button import Button
import pickle
import os

restart_button = Button(RESTART_IMG, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
level = 1
def reset_level(level):
    player_group.empty()
    enemy_group.empty()
    exit_group.empty()
    if os.path.exists(f"levels/level{level}"):
        f = open(f"levels/level{level}", "rb")
        world_data = pickle.load(f)
    
    game_world = World(world_data,player_group, enemy_group, exit_group)
    return game_world
pygame.init()
clock = pygame.time.Clock()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
if os.path.exists(f"levels/level{level}"):
        f = open(f"levels/level{level}", "rb")
        world_data = pickle.load(f)
game_world = World(world_data,player_group, enemy_group, exit_group)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    game_world.draw(screen)
    player_group.update(game_world.tile_list, enemy_group, exit_group)
    player_group.draw(screen)
    if player_group.sprites()[0].game_status == "PLAYING":

        enemy_group.update()
    elif player_group.sprites()[0].game_status == "GAMEOVER":
        restart_button.draw()
        if restart_button.clicked:
            player_group.sprites()[0].game_status = "PLAYING"
            player_group.sprites()[0].reset(100,100)
    elif player_group.sprites()[0].game_status == "NEXTLEVEL":
        level += 1
        if level <= 10:
            game_world = reset_level(level)
            player_group.sprites()[0].game_status = "PLAYING"
            
        print(level)

    enemy_group.draw(screen)
    exit_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)