import pygame
from enemy import Enemy
from constants import *
class Game:
    def __init__(self, player, enemy_group, player_bullet_group, enemy_bullet_group) -> None:
        self.score = 0
        self.level_number = 0
        self.player = player
        self.enemy_group = enemy_group
        self.player_bullet_group = player_bullet_group
        self.enemy_bullet_group = enemy_bullet_group
        self.font = pygame.font.Font("assets/Facon.ttf")

    def start_new_level(self):
        self.level_number += 1
        for row in range(4):
            for col in range(15):
                enemy = Enemy(col * 64 , row * 64 + 100, self.enemy_bullet_group)
                self.enemy_group.add(enemy)


    def check_if_on_edge(self):
        on_edge = False
        for enemy in self.enemy_group:
            if enemy.rect.right > SCREEN_WIDTH or enemy.rect.left <0:
                on_edge = True
                break
        if on_edge:
            for enemy in self.enemy_group:
                enemy.direction *= -1
                enemy.rect.y += self.level_number * 10

        # TODO   در صورت رسیدن بیگانه ها به نقطه امن بازیکن بازی ریست شود
        # TODO   در صورت از بین رفتن تمام بیگانه ها وارد مرحله جدید شویم
        # TODO   scoreboard را تکمیل نمائید

    
    def draw(self,screen):
        """scoreboard"""
        score_text = self.font.render(f'Score: {self.score}', True, (120,12,170))
        score_rect = score_text.get_rect(topleft=(10,10))

        screen.blit(score_text, score_rect)
    
    def check_collisions(self):
        if pygame.sprite.groupcollide(self.player_bullet_group, self.enemy_group, True, True):
            self.score += 1