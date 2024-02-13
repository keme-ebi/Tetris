import pygame, sys
from colors import Colors#
from grid import Grid

pygame.init()
background = Colors.background
grid = Grid()
screen = pygame.display.set_mode((600, 480))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(background)
    grid.draw_grid(screen)
    pygame.display.update()
    clock.tick(60)