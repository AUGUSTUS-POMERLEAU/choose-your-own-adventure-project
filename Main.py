import pygame

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
pygame.init()

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 650
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Destroyer's Kaputt")

clock = pygame.time.Clock()
running = True
#main loop
while running:
    #loop through all events. If one is a key, and that key was escape (clicking exit button on window), break loop
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()