import pygame, sys

pygame.init()
background = (135, 25, 55)

screen = pygame.display.set_mode((600, 480))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(background)
    pygame.display.update()
    clock.tick(60)