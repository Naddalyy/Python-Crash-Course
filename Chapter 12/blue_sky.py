import pygame
import sys

# Simply setting up a pygame window with a blue bg
pygame.init()
screen = pygame.display.set_mode((800, 800))
screen.fill((0, 0, 150))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()