"""Module for the Game class holding the general game logic"""

from grid import Grid
from tetraminoes import *
import pygame, random, sys


class Game:
    """Game class holding all the game logic together"""
    def __init__(self):
        """inititalization of the Game class"""
        # instance of the Grid class
        self.grid = Grid()
        # list of all the blocks/tetraminoes
        self.tetraminoes = [LBlock(), JBlock(), TBlock(), IBlock(), SquareBlock(), HBlock(), HInvertBlock(), HIlongBlock(), HlongBlock(), ZBlock(), SBlock(), UBlock(), TridentBlock(), CrossBlock()]
        # current block on the grid
        self.current = self.random_block()
        # incoming or next block
        self.next = self.random_block()
        self.game_over = False
        self.score = 0
        self.pause = False

    def keypress(self, update):
        """listens for keypresses by the user/player
        Args:
            update (timer): timer for automatic dropdown of blocks
        """
        for event in pygame.event.get():
            # if player hits the x(close) button
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if player strucks a key
            if event.type == pygame.KEYDOWN:
                # if return key is pressed and game over is true, game resets
                if event.key == pygame.K_RETURN and self.game_over == True:
                    self.game_over = False
                    self.reset()
                # if left arrow key is pressed
                if event.key == pygame.K_LEFT and self.game_over is False:
                    self.move_left()
                # right arrow key
                if event.key == pygame.K_RIGHT and self.game_over == False:
                    self.move_right()
                # down arrow key
                if event.key == pygame.K_DOWN and self.game_over == False:
                    self.move_down()
                # up arrow key to rotate the block
                if event.key == pygame.K_UP and self.game_over == False:
                    self.rotate()
                # spacebar key to pause and un-pause the game
                if event.key == pygame.K_SPACE and self.game_over == False:
                    self.pause_game()
            # drop down current block automatically
            if event.type == update and self.game_over == False:
                self.move_down()

    def reset(self):
        """resets the game"""
        # reset the grid to empty
        self.grid.grid_reset()
        # reset the block or tetramino list
        self.tetraminoes = [LBlock(), JBlock(), TBlock(), IBlock(), SquareBlock(), HBlock(), HInvertBlock(), HIlongBlock(), HlongBlock(), ZBlock(), SBlock(), UBlock(), TridentBlock(), CrossBlock()]
        # reset both current and next block
        self.current = self.random_block()
        self.next = self.random_block()
        self.score = 0

    def pause_game(self):
        """Pauses the game"""
        self.pause = True
        # keeps running while pause is True
        while self.pause:
            for event in pygame.event.get():
                # listens for keypress in case player quits game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # checks if player unpauses the game
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.pause = False

    def random_block(self):
        """generates random blocks from the list"""
        # checks if all blocks has appeared once and there's none left in the list
        if len(self.tetraminoes) == 0:
            # resets the list
            self.tetraminoes = [LBlock(), JBlock(), TBlock(), IBlock(), SquareBlock(), HBlock(), HInvertBlock(), HIlongBlock(), HlongBlock(), ZBlock(), SBlock(), UBlock(), TridentBlock(), CrossBlock()]
        # gets a block at random
        block = random.choice(self.tetraminoes)
        # ensures each block appears once and removes the block assigned at random from the list
        self.tetraminoes.remove(block)
        return block

    def lock(self):
        """locks the current block in place when it gets to the bottom of the grid
        """
        # get the current position of each cell of the block
        cell = self.current.cell_pos()
        for pos in cell:
            # set the grid value to the value of the current block
            self.grid.grid[pos.y][pos.x] = self.current.id
        # set the current block to the next after locking the block
        self.current = self.next
        # generate another block to the next
        self.next = self.random_block()
        # get the number of rows cleared
        rows_cleared = self.grid.clear_row()
        self.scores(rows_cleared, 1)
        # check if the blocks has gotten to the top of the grid
        if not self.grid_empty():
            self.game_over = True

    def draw(self, screen):
        """draw the block on screen
        Args:
            screen (obj): screen to draw block on
        """
        # draw the game grid
        self.grid.draw_grid(screen)
        # draw current block on the screen
        self.current.draw_block(screen, 1, 1)
        # draw next block and aligns the according to their id
        if self.next.id == 5:
            self.next.draw_block(screen, 250, 190)
        elif self.next.id == 2:
            self.next.draw_block(screen, 250, 180)
        else:
            # default alignment for blocks that appear in the middle
            self.next.draw_block(screen, 270, 180)

    def move_left(self):
        """move the block left"""
        self.current.move(0, -1)
        # checks if the space to the left is out of the grid or occupied
        if not self.block_check() or not self.grid_empty():
            self.current.move(0, 1)

    def move_right(self):
        """move the block right"""
        self.current.move(0, 1)
        # checks if the space to the right is out of the grid or occupied
        if not self.block_check() or not self.grid_empty():
            self.current.move(0, -1)

    def move_down(self):
        """move the block down"""
        self.current.move(1, 0)
        # checks if the bottom is out of the grid or occupied
        if not self.block_check() or not self.grid_empty():
            self.current.move(-1, 0)
            # locks the block in place once it gets to the bottom or on top of another block
            self.lock()

    def block_check(self):
        """checks for blocks occupying a space in the grid"""
        tiles = self.current.cell_pos()
        for tile in tiles:
            if  not self.grid.grid_check(tile.y, tile.x):
                return False
        return True
    
    def grid_empty(self):
        """checks if the grid or cell is empty"""
        tiles = self.current.cell_pos()
        for ti in tiles:
            if not self.grid.empty_grid(ti.y, ti.x):
                return False
        return True

    def rotate(self):
        """rotates/changes position of the current block"""
        self.current.rotation()
        # stops rotation if space is occupied
        if not self.block_check() or not self.grid_empty():
            self.current.un_rotate()

    def scores(self, line_cleared, one_point):
        """sets the player's score
        Args:
            line_cleared (int): number of lines cleared
            one_point (int): one point score for each successful block locked in place
        """
        if line_cleared == 1:
            self.score += 100
        elif line_cleared == 2:
            self.score += 250
        elif line_cleared == 3:
            self.score += 400
        elif line_cleared == 4:
            self.score += 800
        self.score += one_point