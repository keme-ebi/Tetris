from grid import Grid
from tetraminoes import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.tetraminoes = [LBlock(), JBlock(), TBlock(), IBlock(), SquareBlock(), HBlock(), HInvertBlock(), HIlongBlock(), HlongBlock(), ZBlock(), SBlock(), UBlock(), TridentBlock(), CrossBlock()]
        self.current = self.random_block()
        self.next = self.random_block()

    def random_block(self):
        block = random.choice(self.tetraminoes)
        return block
    
    def draw(self, screen):
        self.grid.draw_grid(screen)
        self.current.draw_block(screen)