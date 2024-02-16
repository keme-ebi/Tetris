from colors import Colors
import pygame

class Grid:
    def __init__(self):
        self.rows = 20
        self.columns = 10
        self.tile_size = 30
        self.grid = [[0 for j in range(self.columns)] for i in range(self.rows)]
        self.colors = Colors.get_color()

    def draw_grid(self, screen):
        """Draws the grid to the screen"""
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
        if y >= 0 and y < self.rows and x >= 0 and x < self.columns:
            return True
        return False
    
    def empty_grid(self, y, x):
        if self.grid[y][x] == 0:
            return True
        return False
    
    def full_row(self, y):
        for x in range(self.columns):
            if self.grid[y][x] == 0:
                return False
        return True
    
    def clear(self, y):
        for x in range(self.columns):
            self.grid[y][x] == 0

    def move_row(self, y, num_row):
        for x in range(self.columns):
            self.grid[y + num_row][x] = self.grid[y][x]
            self.grid[y][x] = 0

    def clear_row(self):
        complete = 0
        for y in range(self.rows-1, 0, -1):
            if self.full_row(y):
                self.clear(y)
                complete += 1
            elif complete > 0:
                self.move_row(y, complete)
        return complete
    
    def grid_reset(self):
        self.grid = [[0 for j in range(self.columns)] for i in range(self.rows)]