from colors import Colors
from disp import Display
from game import Game
import pygame

# pygame initialisation
pygame.init()
# background color
background = Colors.screen_background
# set up screen display
screen = pygame.display.set_mode((500, 600))
# game caption
pygame.display.set_caption("Tetris")

# initialize font for text displayed
title = pygame.font.Font(None, 40)
score_text = title.render("Score", True, Colors.grid_color)
next_text = title.render("Next", True, Colors.grid_color)
game_over = title.render("GAME OVER", True, Colors.red)

# box to display next block
next_rect = pygame.Rect(320, 220, 170, 150)
# box to display player's score
score_rect = pygame.Rect(320, 55, 170, 60)

clock = pygame.time.Clock()
# instance of the Game class
game = Game()
# instance of the Display class
display = Display(screen)

# make game update itself ever 300 milliseconds
UPDATE = pygame.USEREVENT
pygame.time.set_timer(UPDATE, 300)

while True:
    # listens for keypresses
    game.keypress(UPDATE)

    score_val_surf = title.render(str(game.score), True, background)
    screen.fill(background)
    # score text
    display.display(score_text, (365, 20, 50, 50))
    # next text
    display.display(next_text, (375, 180, 50, 50))
    # draw score box
    pygame.draw.rect(screen, Colors.thistle, score_rect, 0, 10)
    # score display
    display.display(score_val_surf, score_val_surf.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    # draw box to display next block
    pygame.draw.rect(screen, Colors.grid_color, next_rect, 0, 10)
    # game method to draw next or incoming block
    game.draw(screen)
    # if game over is true display a text
    if game.game_over:
        display.display(game_over, (50, 250, 50, 50))
    pygame.display.update()
    clock.tick(60)