"""Script for Grid class"""


from typing import List


class Grid:
    """Class for the display grid in the game.

    This class does not display anything directly in the command line.
    Its methods run in the background to validate moves, update the
    grid, and to check if the game has been won or tied.
    """
    def __init__(self,
                 _internal_grid: List[int] = list(range(9))) -> None:

        self._internal_grid = _internal_grid
        print('grid created!')
    
    def check_valid(self) -> bool:
        """Checks if the move the player tried to make is valid or not"""
        pass

    def set_int_grid(self):
        """Changes a number in the grid list to token of the player"""
        pass

    def check_win(self) -> bool:
        """Checks to see if either player has won the game"""
        pass

    def check_tie(self) -> bool:
        """Checks to see if the game has been tied"""
        pass