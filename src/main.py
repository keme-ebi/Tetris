import pygame, sys
from colors import Colors
from game import Game

pygame.init()
background = Colors.screen_background
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()
game = Game()

UPDATE = pygame.USEREVENT
pygame.time.set_timer(UPDATE, 200)

while True:
    game.keypress(UPDATE)

    screen.fill(background)
    game.draw(screen)
    pygame.display.update()
    clock.tick(60)