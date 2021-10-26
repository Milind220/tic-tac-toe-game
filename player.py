"""Script for Player class"""


from typing import Tuple


class Player:
    """Class to represent a player in the game
    
    Meant to be instantiated twice in the game, once for each player.

    Methods:
        set_name: Sets the name attribute for the player.
        set_num: Sets the player number (either 1 or 2).
        set_token: Sets the token (X or O) for the player.
        set_move: Returns the grid space that the player has selected for the move (str).
        tell_grid: Tells the grid what token to place in what grid space.
    """
    def __init__(self) -> None:
        print('player created!')

    def set_name(self, name: str) -> None:
        """Sets the name of the player"""
        self.name = name

    def set_num(self, num: int) -> None:
        """Sets the player number"""
        self.num = num

    def set_token(self, token: str) -> None:
        """Sets the token for the player (Either X or O)"""
        self.token = token

    def set_move(self) -> str:
        """Takes the move that the player wants to make and returns it for the grid to use

        Returns:
            str: Grid-space that the player has chosen to place a token in.
        """
        move = str(input(f'Player {self.num}. Enter move grid space: '))
        return move

    def tell_grid(self, move: int) -> Tuple:
        """Tells the grid what token to place in what grid space

        Args:
            move (int): The grid space that the player wants to place a token in.

        Returns:
            Tuple: The token that the player chose.
        """
        return (move, self.token)
    
    def print_welcome_statement(self) -> None:
        print(f'Welcome! Player {self.num}, {self.name}, token: {self.token}\n')