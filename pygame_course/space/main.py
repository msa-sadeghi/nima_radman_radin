import pygame
from player import Player
from constants import *
from pygame.locals import *
from game import Game
pygame.init()
clock = pygame.time.Clock()
enemy_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
player = Player(player_bullet_group)

font = pygame.font.Font("assets/Facon.ttf",64)
welcome_text = font.render("Welcome to Space Game", True, (245, 30,178))
welcome_rect = welcome_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

start_time = pygame.time.get_ticks()


game = Game(player, enemy_group,player_bullet_group, enemy_bullet_group)
game.start_new_level()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == K_SPACE:
                player.fire()
    screen.fill((0,0,0))

    if pygame.time.get_ticks() - start_time < 3000:
        screen.blit(welcome_text, welcome_rect)
    else:
        player.draw(screen)
        player_bullet_group.update()
        player_bullet_group.draw(screen)
        enemy_group.update()
        enemy_group.draw(screen)
        game.draw(screen)
        game.check_if_on_edge()
        game.check_collisions()
    pygame.display.update()
    clock.tick(FPS)
