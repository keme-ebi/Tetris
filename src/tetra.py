from colors import Colors
import pygame
from pos import BlockPosition as P


class Blocks:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.rotate = 0
        self.colors = Colors.get_color()
        self.y_offset = 0
        self.x_offset = 0

    def move(self, y, x):
        self.y_offset = y
        self.x_offset = x

    def cell_pos(self):
        tiles = self.cells[self.rotate]
        new_pos = []
        for ti in tiles:
            ti = P(ti.y + self.y_offset, ti.x + self.x_offset)
            new_pos.append(ti)
        return new_pos

    def draw_block(self, screen):
        tiles = self.cell_pos()
        for tile in tiles:
            # bx represents the column, by the row
            by = tile.y * self.cell_size  + 1
            bx = tile.x * self.cell_size  + 1
            width_height = self.cell_size - 1
            tile_rect = pygame.Rect(bx, by, width_height, width_height)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)