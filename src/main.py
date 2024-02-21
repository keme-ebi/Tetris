"""main module"""

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
intro = pygame.font.Font(None, 30)
score_text = title.render("Score", True, Colors.grid_color)
next_text = title.render("Next", True, Colors.grid_color)
game_over = title.render("GAME OVER", True, Colors.red)

# game instructions
left = intro.render("< move left", True, Colors.grid_color)
right = intro.render("> move right", True, Colors.grid_color)
down = intro.render("v move down", True, Colors.grid_color)
up = intro.render("^ to rotate", True, Colors.grid_color)
space = intro.render("spacebar to pause", True, Colors.grid_color)
enter = intro.render("Enter to restart", True, Colors.grid_color)
enter2 = intro.render("after game over", True, Colors.grid_color)

# box to display next block
next_rect = pygame.Rect(320, 160, 170, 150)
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
    display.display(next_text, (375, 130, 50, 50))

    # draw score box
    pygame.draw.rect(screen, Colors.thistle, score_rect, 0, 10)

    # score display
    display.display(score_val_surf, score_val_surf.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))

    # instructions
    display.display(left, (310, 350, 50, 50))
    display.display(right, (310, 380, 50, 50))
    display.display(down, (310, 410, 50, 50))
    display.display(up, (310, 440, 50, 50))
    display.display(space, (310, 470, 50, 50))
    display.display(enter, (310, 500, 50, 50))
    display.display(enter2, (310, 520, 50, 50))

    # draw box to display next block
    pygame.draw.rect(screen, Colors.grid_color, next_rect, 0, 10)

    # game method to draw next or incoming block
    game.draw(screen)

    # if game over is true display a text
    if game.game_over:
        display.display(game_over, (50, 250, 50, 50))

    # update screen
    pygame.display.update()
    clock.tick(60)