"""Module for base Blocks class"""

from colors import Colors
from pos import BlockPosition as P
import pygame


class Blocks:
    """a base class Blocks that each block/tetramino will inherit from"""
    def __init__(self, id):
        """inititalization of Block class
        Args:
            id (int): id of the block
        """
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.rot = 0
        self.colors = Colors.get_color()
        self.y_offset = 0
        self.x_offset = 0

    def move(self, y, x):
        """moves the block/tetramino
        Args:
            y (int): y axis (row)
            x (int): x axis (column)
        """
        # increases the offsets according to the number gotten from x and y
        self.y_offset += y
        self.x_offset += x

    def cell_pos(self):
        """gets the position of each cell of the current block/tetramino
        Returns:
            new (list): a list of the position for the current block
        """
        # get the block according to the rotation position
        tiles = self.cells[self.rot]
        new_pos = []
        for ti in tiles:
            ti = P(ti.y + self.y_offset, ti.x + self.x_offset)
            new_pos.append(ti)
        return new_pos

    def draw_block(self, screen, offset_x, offset_y):
        """draws the block on the screen
        Args:
            screen (obj): screen object
            offset_x (int): position of the block on the offset postion on the x axis (column)
            offset_y (int): position of the block on the offset position on the y axis (row)
        """
        # get the position of each cell of the current block
        tiles = self.cell_pos()
        for tile in tiles:
            # bx represents the column, by the row
            by = offset_y + tile.y * self.cell_size
            bx = offset_x + tile.x * self.cell_size
            width_height = self.cell_size - 1
            tile_rect = pygame.Rect(bx, by, width_height, width_height)
            # draw the block to the screen
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)

    def rotation(self):
        """rotates the block/tetramino according to the number of rotation the block holds
        """
        # gets the number of rotation a block can make
        length = len(self.cells)
        self.rot += 1
        # set rotation back to original after getting to the final rotation
        if self.rot == length or self.rot < 0:
            self.rot = 0

    def un_rotate(self):
        """does the opposite of the rotation method"""
        length = len(self.cells)
        self.rot -= 1
        if self.rot == 0:
            self.rot = length - 1