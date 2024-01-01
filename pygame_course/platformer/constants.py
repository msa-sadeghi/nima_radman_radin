import pygame

screen = pygame.display.set_mode()
SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()
FPS = 60
TILE_SIZE = 32

DIRT_IMG = pygame.image.load("assets/dirt.png")
GRASS_IMG = pygame.image.load("assets/grass.png")
WATER_IMG = pygame.image.load("assets/water.png")