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
                cell_value = self.grid[ro][col]
                cell_rect = pygame.Rect(col * self.tile_size + 1, ro * self.tile_size + 1, self.tile_size - 1, self.tile_size - 1)
                pygame.draw.rect(screen, self.colors[0], cell_rect)