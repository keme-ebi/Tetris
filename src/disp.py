"""This module has a class Display to display texts to the game screen"""


class Display:
    """A class Display that holds methods to display texts to the game screen"""
    def __init__(self, screen):
        """Initialization of the Display class
        Args:
            screen (obj): screen display setup
        """
        self.screen = screen

    def display(self, text, pos):
        """Displays texts to the screen
        Args:
            text (obj): the text to display, also carries the color of the text
            pos (tup): a tuple of coordinates to setup the message position on the screen
        """
        self.screen.blit(text, pos)