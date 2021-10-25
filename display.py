"""Script for Display class"""


from typing import Tuple


class Display:
    """Class that displays the game in the command line

    Meant to be instantiated once. Directly displays the game in the 
    command line.

    Methods:
        show_invalid_move: Prints a line to inform a player that the move is invalid.
        show_win: Informs players that the game has been won.
        show tie: Informs the players that the game has been tied.
    """
    _display_init = ['   |   |   \n', '-----------\n'] # These are the only two 'lines' that are required to generate a grid

    def __init__(self, 
                 player: int = 1,
                 ongoing: bool = True,
                 ) -> None:
        self.player = player,
        self.ongoing = ongoing,
        self.display_grid: str = self._set_init_display()
    
    def _set_init_display(self) -> str:
        """Creates the initial display

        Returns:
            str: The display grid, as a string printed in multiple lines in the command line.
        """
        result = ''
        for line_number in range(1,12):
            if line_number == 4 or line_number == 8: # These are the lines where the grid has dividors.
                result += self._display_init[1]
            else:
                result += self._display_init[0]
        return result
    
    def show_invalid_move(self) -> None:
        """Prints a line to notify the player that the move is invalid.
        
        This can be displayed if the player tries to place a token in a
        grid-space that is already occupied, or if the player enters a 
        grid-space number outside of the range of possible spaces
        Ex: 19.
        """
        print(f'Sorry player {self.player}! that move is invalid. Try again!')
    
    def show_win(self) -> None:
        """Prints a line to notify the player that someone has won the game."""
        print(f'Player {self.player} has won the game!')
    
    def show_tie(self) -> None:
        """Prints a line to notify the player that the game has been tied."""
        print(f"Oh no! The game's a tie!")
    