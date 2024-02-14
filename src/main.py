import pygame, sys
from colors import Colors
from game import Game

pygame.init()
background = Colors.screen_background
screen = pygame.display.set_mode((600, 480))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(background)
    game.draw(screen)
    pygame.display.update()
    clock.tick(60)