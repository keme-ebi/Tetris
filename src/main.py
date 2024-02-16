import pygame
from colors import Colors
from game import Game

pygame.init()
background = Colors.screen_background
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Tetris")

title = pygame.font.Font(None, 40)
score_surface = title.render("Score", True, Colors.grid_color)
next_surface = title.render("Next", True, Colors.grid_color)
game_over = title.render("GAME OVER", True, Colors.red)

next_rect = pygame.Rect(320, 220, 170, 150)
score_rect = pygame.Rect(320, 55, 170, 60)

clock = pygame.time.Clock()
game = Game()

UPDATE = pygame.USEREVENT
pygame.time.set_timer(UPDATE, 300)

while True:
    game.keypress(UPDATE)

    score_val_surf = title.render(str(game.score), True, Colors.screen_background)
    screen.fill(background)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))
    pygame.draw.rect(screen, Colors.thistle, score_rect, 0, 10)
    screen.blit(score_val_surf, score_val_surf.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.grid_color, next_rect, 0, 10)
    game.draw(screen)
    if game.game_over:
        screen.blit(game_over, (50, 250, 50, 50))
    pygame.display.update()
    clock.tick(60)