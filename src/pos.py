"""Module for the BlockPosition class"""

class BlockPosition:
    """a class holding position of the current block"""
    def __init__(self, row, column):
        """initialization of the class
        Args
            row (int): the position of the block on the y axis
            column (int): the postiion of the block on the x axis
        """
        self.y = row
        self.x = column