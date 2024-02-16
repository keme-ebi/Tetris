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
        self.game_over = False
        self.score = 0

    def keypress(self, update):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if self.game_over == True:
                    self.game_over = False
                    self.reset()
                if event.key == pygame.K_LEFT and self.game_over is False:
                    self.move_left()
                if event.key == pygame.K_RIGHT and self.game_over == False:
                    self.move_right()
                if event.key == pygame.K_DOWN and self.game_over == False:
                    self.move_down()
                if event.key == pygame.K_UP and self.game_over == False:
                    self.rotate()
            if event.type == update and self.game_over == False:
                self.move_down()

    def reset(self):
        self.grid.grid_reset()
        self.tetraminoes = [LBlock(), JBlock(), TBlock(), IBlock(), SquareBlock(), HBlock(), HInvertBlock(), HIlongBlock(), HlongBlock(), ZBlock(), SBlock(), UBlock(), TridentBlock(), CrossBlock()]
        self.current = self.random_block()
        self.next = self.random_block()

    def random_block(self):
        if len(self.tetraminoes) == 0:
            self.tetraminoes = [LBlock(), JBlock(), TBlock(), IBlock(), SquareBlock(), HBlock(), HInvertBlock(), HIlongBlock(), HlongBlock(), ZBlock(), SBlock(), UBlock(), TridentBlock(), CrossBlock()]
        block = random.choice(self.tetraminoes)
        self.tetraminoes.remove(block)
        return block
    
    def lock(self):
        cell = self.current.cell_pos()
        for pos in cell:
            self.grid.grid[pos.y][pos.x] = self.current.id
        self.current = self.next
        self.next = self.random_block()
        rows_cleared = self.grid.clear_row()
        self.scores(rows_cleared, 1)
        if not self.grid_empty():
            self.game_over = True

    def draw(self, screen):
        self.grid.draw_grid(screen)
        self.current.draw_block(screen, 1, 1)
        if self.next.id == 5:
            self.next.draw_block(screen, 250, 260)
        elif self.next.id == 2:
            self.next.draw_block(screen, 250, 240)
        else:
            self.next.draw_block(screen, 270, 240)

    def move_left(self):
        self.current.move(0, -1)
        if not self.block_check() or not self.grid_empty():
            self.current.move(0, 1)

    def move_right(self):
        self.current.move(0, 1)
        if not self.block_check() or not self.grid_empty():
            self.current.move(0, -1)

    def move_down(self):
        self.current.move(1, 0)
        if not self.block_check() or not self.grid_empty():
            self.current.move(-1, 0)
            self.lock()

    def block_check(self):
        tiles = self.current.cell_pos()
        for tile in tiles:
            if  not self.grid.grid_check(tile.y, tile.x):
                return False
        return True
    
    def grid_empty(self):
        tiles = self.current.cell_pos()
        for ti in tiles:
            if not self.grid.empty_grid(ti.y, ti.x):
                return False
        return True

    def rotate(self):
        self.current.rotation()
        if not self.block_check() or not self.grid_empty():
            self.current.un_rotate()

    def scores(self, line_cleared, one_point):
        if line_cleared == 1:
            self.score += 100
        elif line_cleared == 2:
            self.score += 250
        elif line_cleared == 3:
            self.score += 400
        elif line_cleared == 4:
            self.score += 800
        self.score += one_point