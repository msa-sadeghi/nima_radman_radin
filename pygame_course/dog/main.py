from random import randint
import pygame
pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

dog_left = pygame.image.load("dog/dog.png")
dog_right = pygame.transform.flip(dog_left, True, False)


dog = dog_right
dog_rect = dog.get_rect()
dog_rect.bottom = WINDOW_HEIGHT
dog_rect.centerx = WINDOW_WIDTH/2
DOG_NORMAL_VELOCITY = 5
DOG_FAST_VELOCITY = 15
dog_velocity = DOG_NORMAL_VELOCITY
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dog_rect.x -= dog_velocity
        dog = dog_left 
    if keys[pygame.K_RIGHT]:
        dog_rect.x += dog_velocity
        dog = dog_right 
    
    display_surface.fill((0, 0, 0))
    display_surface.blit(dog, dog_rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
