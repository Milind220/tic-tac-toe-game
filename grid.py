"""Script for Grid class"""


from typing import List

from display import Display


class Grid:
    """Class for the display grid in the game.

    This class does not display anything directly in the command line.
    Its methods run in the background to validate moves, update the
    grid, and to check if the game has been won or tied.

    attributes:
        internal_grid: contains the info regarding which spots in 
        the 3x3 grid are empty, and what token the none empty ones have.
    """
    def __init__(self,
                 internal_grid: List[str] = [' ' for x in range(9)]) -> None:
    # _internal_grid is what contains the info regarding which spots in
    # the 3x3 grid are empty, and what token the none empty ones have.
    # All the checks regarding game winning/ties, move validity, and 
    # placing of token in grid is done here. Displayed through 
    # show_game_grid() in Display class.

        self.internal_grid = internal_grid
        print('Debug: grid created!')
    
    def check_valid(self, position: int) -> bool:
        """Checks if the move the player tried to make is valid or not

        Args:
            position (int): position that player is trying to place a token in

        Returns:
            bool: true if empty position, false if already full.
        """
        # position -1 To get it in the range of 0-8 index positions
        return self.internal_grid[position - 1] == ' '

    def set_internal_grid(self, position: int, token: str) -> None:
        """Mutates a position in the grid list to player token
        
        Changes the internal_grid implicitly, does not return it to be
        reassigned
        """
        try:
            self.internal_grid[position-1] = token
        except Exception as err:
            print(f'Error: something went wrong!\n{err}')

    def check_win(self) -> bool:
        """Checks to see if either player has won the game
        
        Returns:
            bool: True if game won, False if not
        """
        grid = self.get_internal_grid()
        for i, value in enumerate(grid):
            if i in [0,3,6]:
                if value == grid[i+1] == grid[i+2] != ' ': # 3 in a row.
                    return True
            if i in [0,1,2]:
                if value == grid[i+3] == grid[i+6] != ' ': # 3 in a column.
                    return True
            if i == 0:
                if value == grid[4] == grid[8] != ' ': # 3 diagonally.
                    return True
            if i == 2:
                if value == grid[4] == grid[6] != ' ': # 3 diagonally other direction.
                    return True
        return False

    def check_tie(self) -> bool:
        """Checks to see if the game has been tied
        
        Returns:
            bool: True if tie, False if not a tie
        """
        return ' ' not in self.internal_grid  # Checks if game grid is full, ie, a tie.

    def get_internal_grid(self) -> List[str]:
        """Gets internal_grid attribute"""
        return self.internal_grid

