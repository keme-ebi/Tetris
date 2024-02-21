"""This module holds all the blocks/tetraminoes"""

from pos import BlockPosition as P
from tetra import Blocks


class LBlock(Blocks):
    """The Lblock tetramino"""
    def __init__(self):
        # inherit from base Block class and have the id set to 1
        super().__init__(id = 1)
        # dictionary holding each rotation for the block
        self.cells = {
            0 : [P(0,1), P(1,1), P(2,1), P(2,2)],
            1 : [P(1,0), P(1,1), P(1,2), P(2,0)],
            2 : [P(0,0), P(0,1), P(1,1), P(2,1)],
            3 : [P(0,2), P(1,0), P(1,1), P(1,2)]
        }
        # initital position of the block on the screen
        self.move(0, 3)

class JBlock(Blocks):
    """The Jblock tetramino"""
    def __init__(self):
        # inherit from base Block class and have the id set to 2
        super().__init__(id = 2)
        # dictionary holding each rotation for the block
        self.cells = {
            0 : [P(0,1), P(1,1), P(2,1), P(2,0)],
            1 : [P(0,0), P(1,0), P(1,1), P(1,2)],
            2 : [P(0,1), P(0,2), P(1,1), P(2,1)],
            3 : [P(1,0), P(1,1), P(1,2), P(2,2)]
        }
        # initital position of the block on the screen
        self.move(0, 4)


class IBlock(Blocks):
    """The Iblock tetramino"""
    def __init__(self):
        # inherit from base Block class and have the id set to 3
        super().__init__(id = 3)
        # dictionary holding each rotation for the block
        self.cells = {
            0 : [P(0,1), P(1,1), P(2,1), P(3,1)],
            1 : [P(1,0), P(1,1), P(1,2), P(1,3)]
        }
        # initital position of the block on the screen
        self.move(0, 3)


class TBlock(Blocks):
    """The Tblock tetramino"""
    def __init__(self):
        # inherit from base Block class and have the id set to 4
        super().__init__(id = 4)
        # dictionary holding each rotation for the block
        self.cells = {
            0 : [P(0,1), P(1,0), P(1,1), P(1,2)],
            1 : [P(0,1), P(1,1), P(1,2), P(2,1)],
            2 : [P(1,0), P(1,1), P(1,2), P(2,1)],
            3 : [P(1,0), P(0,1), P(1,1), P(2,1)]
        }
        # initital position of the block on the screen
        self.move(0, 3)


class SquareBlock(Blocks):
    """The Squareblock tetramino"""
    def __init__(self):
        # inherit from base Block class and have the id set to 5
        super().__init__(id = 5)
        # dictionary holding each rotation for the block
        self.cells = {
            0 : [P(0,0), P(0,1), P(1,0), P(1,1)]
        }
        # initital position of the block on the screen
        self.move(0, 4)


class HBlock(Blocks):
    """The Hblock tetramino"""
    def __init__(self):
        # inherit from base Block class and have the id set to 6
        super().__init__(id = 6)
        # dictionary holding each rotation for the block
        self.cells = {
            0 : [P(0,1), P(1,1), P(1,2), P(2,2)],
            1 : [P(1,1), P(1,2), P(2,0), P(2,1)]
        }
        # initital position of the block on the screen
        self.move(0, 3)


class HInvertBlock(Blocks):
    """The HInvertblock tetramino"""
    def __init__(self):
        # inherit from base Block class and have the id set to 7
        super().__init__(id = 7)
        # dictionary holding each rotation for the block
        self.cells = {
            0 : [P(0,1), P(1,0), P(1,1), P(2,0)],
            1 : [P(1,0), P(1,1), P(2,1), P(2,2)]
        }
        # initital position of the block on the screen
        self.move(0, 4)


class ZBlock(Blocks):
    """The Zblock tetramino"""
    def __init__(self):
        # inherit from base Block class and have the id set to 8
        super().__init__(id = 8)
        # dictionary holding each rotation for the block
        self.cells = {
            0 : [P(0,0), P(0,1), P(1,1), P(1,2)],
            1 : [P(0,1), P(1,0), P(1,1), P(2,0)]
        }
        # initital position of the block on the screen
        self.move(0, 3)


class SBlock(Blocks):
    """The Sblock tetramino"""
    def __init__(self):
        # inherit from base Block class and have the id set to 9
        super().__init__(id = 9)
        # dictionary holding each rotation for the block
        self.cells = {
            0 : [P(0,1), P(0,2), P(1,0), P(1,1)],
            1 : [P(0,0), P(1,0), P(1,1), P(2,1)]
        }
        # initital position of the block on the screen
        self.move(0, 3)


class UBlock(Blocks):
    """The Sblock tetramino"""
    def __init__(self):
        # inherit from base Block class and have the id set to 10
        super().__init__(id = 10)
        # dictionary holding each rotation for the block
        self.cells = {
            0 : [P(0,0), P(0,2), P(1,0), P(1,1), P(1,2)],
            1 : [P(0,1), P(0,2), P(1,1), P(2,1), P(2,2)],
            2 : [P(1,0), P(1,1), P(1,2), P(2,0), P(2,2)],
            3 : [P(0,0), P(0,1), P(1,1), P(2,0), P(2,1)]
        }
        # initital position of the block on the screen
        self.move(0, 3)


class TridentBlock(Blocks):
    """The Tridentblock tetramino"""
    def __init__(self):
        # inherit from base Block class and have the id set to 11
        super().__init__(id = 11)
        # dictionary holding each rotation for the block
        self.cells = {
            0 : [P(0,0), P(0,2), P(1,0), P(1,1), P(1,2), P(2,1)],
            1 : [P(0,1), P(0,2), P(1,0), P(1,1), P(2,1), P(2,2)],
            2 : [P(0,1), P(1,0), P(1,1), P(1,2), P(2,0), P(2,2)],
            3 : [P(0,0), P(0,1), P(1,1), P(1,2), P(2,0), P(2,1)]
        }
        # initital position of the block on the screen
        self.move(0, 3)


class CrossBlock(Blocks):
    """The Crossblock tetramino"""
    def __init__(self):
        # inherit from base Block class and have the id set to 12
        super().__init__(id = 12)
        # dictionary holding each rotation for the block
        self.cells = {
            0 : [P(0,1), P(1,0), P(1,1), P(1,2), P(2,1)]
        }
        # initital position of the block on the screen
        self.move(0, 3)


class HlongBlock(Blocks):
    """The Hlongblock tetramino"""
    def __init__(self):
        # inherit from base Block class and have the id set to 13
        super().__init__(id = 13)
        # dictionary holding each rotation for the block
        self.cells = {
            0 : [P(0,0), P(1,0), P(1,1), P(1,2), P(2,2)],
            1 : [P(0,1), P(0,2), P(1,1), P(2,0), P(2,1)]
        }
        # initital position of the block on the screen
        self.move(0, 3)


class HIlongBlock(Blocks):
    """The Hinvertedlongblock tetramino"""
    def __init__(self):
        # inherit from base Block class and have the id set to 14
        super().__init__(id = 14)
        # dictionary holding each rotation for the block
        self.cells = {
            0 : [P(0,2), P(1,0), P(1,1), P(1,2), P(2,0)],
            1 : [P(0,0), P(0,1), P(1,1), P(2,1), P(2,2)]
        }
        # initital position of the block on the screen
        self.move(0, 3)