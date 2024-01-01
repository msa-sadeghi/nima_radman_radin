import pygame
from config import *
from monster import Monster
from random import randint, choice


class Game:
    def __init__(self, player, monster_group):
        self.score = 0
        self.round_number = 0
        self.player = player
        self.monster_group = monster_group
        self.font = pygame.font.Font("assets/Abrushow.ttf", 32)
        blue_image = pygame.image.load("assets/blue_monster.png")
        green_image = pygame.image.load("assets/green_monster.png")
        purple_image = pygame.image.load("assets/purple_monster.png")
        yellow_image = pygame.image.load("assets/yellow_monster.png")

        self.all_monsters = [blue_image,
                             green_image, purple_image, yellow_image]

        self.target_monster_type = randint(0, 3)
        self.target_monster_image = self.all_monsters[self.target_monster_type]
        self.target_monster_rect = self.target_monster_image.get_rect()
        self.target_monster_rect.bottom = 100
        self.target_monster_rect.centerx = WINDOW_WIDTH/2

    def change_target(self):
        remained_monsters = self.monster_group.sprites()
        target = choice(remained_monsters)
        self.target_monster_image = target.image
        self.target_monster_type = target.type

    def update(self):
        collided_monster = pygame.sprite.spritecollideany(
            self.player, self.monster_group)
        if collided_monster:
            if collided_monster.type == self.target_monster_type:
                collided_monster.remove(self.monster_group)
                self.player.catch_sound.play()
                self.score += 1
                if self.monster_group:
                    self.change_target()
                else:
                    self.start_new_level()

            else:
                self.player.reset()
                self.player.die_sound.play()
                self.player.lives -= 1

    def draw(self, screen):
        # TODO
        # display game score on the screen
        # display game level on the screen
        # display player lives on the screen
        COLORS = (
            (0, 0, 255),
            (0, 255, 0),
            (255, 0, 255),
            (255, 255, 0),
        )
        score_text = self.font.render(
            f'Score:{self.score}', True, (255, 255, 255))
        score_rect = score_text.get_rect()
        score_rect.topleft = (0, 0)

        lives_text = self.font.render(
            f'lives:{self.player.lives}', True, (255, 255, 255))
        lives_rect = lives_text.get_rect()
        lives_rect.topright = (WINDOW_WIDTH, 0)

        escape_text = self.font.render(
            f'escape:{self.player.escape_counter}', True, (255, 255, 255))
        escape_rect = escape_text.get_rect()
        escape_rect.topright = (WINDOW_WIDTH, 40)

        screen.blit(score_text, score_rect)
        screen.blit(lives_text, lives_rect)
        screen.blit(escape_text, escape_rect)
        screen.blit(self.target_monster_image, self.target_monster_rect)
        pygame.draw.rect(screen, COLORS[self.target_monster_type],
                         (0, 100, WINDOW_WIDTH, WINDOW_HEIGHT-200), 4)

    def start_new_level(self):
        self.round_number += 1
        self.player.escape_counter += 1
        for i in range(self.round_number):
            self.monster_group.add(
                Monster(randint(0, WINDOW_WIDTH - 64), randint(100, WINDOW_HEIGHT - 164), self.all_monsters[0], 0))
            self.monster_group.add(Monster(randint(
                0, WINDOW_WIDTH - 64), randint(100, WINDOW_HEIGHT - 164), self.all_monsters[1], 1))
            self.monster_group.add(Monster(randint(
                0, WINDOW_WIDTH - 64), randint(100, WINDOW_HEIGHT - 164), self.all_monsters[2], 2))
            self.monster_group.add(Monster(randint(
                0, WINDOW_WIDTH - 64), randint(100, WINDOW_HEIGHT - 164), self.all_monsters[3], 3))

        # TODO  play start new level sound
