from grid import Grid
from tetraminoes import *
import random
import pygame, sys

class Game:
    def __init__(self):
        self.grid = Grid()
        self.tetraminoes = [LBlock(), JBlock(), TBlock(), IBlock(), SquareBlock(), HBlock(), HInvertBlock(), HIlongBlock(), HlongBlock(), ZBlock(), SBlock(), UBlock(), TridentBlock(), CrossBlock()]
        self.current = self.random_block()
        self.next = self.random_block()

    def keypress(self, update):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_left()
                if event.key == pygame.K_RIGHT:
                    self.move_right()
                if event.key == pygame.K_DOWN:
                    self.move_down()
                if event.key == pygame.K_UP:
                    self.rotate()
            if event.type == update:
                self.move_down()

    def random_block(self):
        block = random.choice(self.tetraminoes)
        return block
    
    def draw(self, screen):
        self.grid.draw_grid(screen)
        self.current.draw_block(screen)

    def move_left(self):
        self.current.move(0, -1)
        if not self.block_check():
            self.current.move(0, 1)

    def move_right(self):
        self.current.move(0, 1)
        if not self.block_check():
            self.current.move(0, -1)

    def move_down(self):
        self.current.move(1, 0)
        if not self.block_check():
            self.current.move(-1, 0)

    def block_check(self):
        tiles = self.current.cell_pos()
        for tile in tiles:
            if not self.grid.grid_check(tile.y, tile.x):
                return False
        return True
    
    def rotate(self):
        self.current.rotation()
        if not self.block_check():
            self.current.un_rotate()