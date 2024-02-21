"""The Grid class module"""

from colors import Colors
import pygame


class Grid:
    """A class Grid to display the area for the blocks"""
    def __init__(self):
        self.rows = 20 # also mean y axis
        self.columns = 10 # also mean x axis
        self.tile_size = 30 # the size of each grid cell
        # set each area of the grid to be 0 which means empty
        self.grid = [[0 for j in range(self.columns)] for i in range(self.rows)]
        # get the list of colors
        self.colors = Colors.get_color()

    def draw_grid(self, screen):
        """Draws the grid to the screen
        Args:
            screen (obj): screen display
        """
        # loop through each rows and colums and change the cell value according to the block dropped
        for ro in range(self.rows):
            for col in range(self.columns):
                # cell_value will change according to the number in the grid
                cell_value = self.grid[ro][col]
                # col is the x axis, ro is the y axis, tile_size is the width and height
                x = col * self.tile_size + 1
                y = ro * self.tile_size + 1
                width_height = self.tile_size - 1
                cell_rect = pygame.Rect(x, y, width_height, width_height)
                # color is changed according to the number in cell_value
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

    def grid_check(self, y, x):
        """checks each grid cell if they are occupied by a block
        Args:
            y (int): y axis (rows)
            x (int): x axis (columns)
        Returns:
            bool: True if cell is not occupied, False otherwise
        """
        if y >= 0 and y < self.rows and x >= 0 and x < self.columns:
            return True
        return False
    
    def empty_grid(self, y, x):
        """checks for empty grid cells
        Args:
            y (int): y axis (rows)
            x (int): x axis (columns)
        Returns:
            bool: True if cell is empty, False otherwise
        """
        if self.grid[y][x] == 0:
            return True
        return False
    
    def full_row(self, y):
        """checks if the row of the grid is completely filled
        Args:
            y (int): y axis (rows)
        Returns:
            bool: True if row is filled, False otherwise
        """
        for x in range(self.columns):
            if self.grid[y][x] == 0:
                return False
        return True
    
    def clear(self, y):
        """clears the grid row
        Args:
            y (int): y axis (rows)
        """
        for x in range(self.columns):
            self.grid[y][x] == 0

    def move_row(self, y, num_row):
        """moves the blocks above cleared row down according to the number of rows cleared
        Args:
            y (int): y axis (rows)
            num_row (int): number of rows cleared
        """
        for x in range(self.columns):
            self.grid[y + num_row][x] = self.grid[y][x]
            self.grid[y][x] = 0

    def clear_row(self):
        """clears the rows from the bottom up
        Returns:
            complete (int): number of rows completed
        """
        complete = 0
        for y in range(self.rows-1, 0, -1):
            if self.full_row(y):
                self.clear(y)
                complete += 1
            elif complete > 0:
                self.move_row(y, complete)
        return complete
    
    def grid_reset(self):
        """reset the grid to 0 or empty"""
        self.grid = [[0 for j in range(self.columns)] for i in range(self.rows)]