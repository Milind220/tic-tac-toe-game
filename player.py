"""Script for Player class"""


class Player:
    """Class to represent a player in the game
    
    Meant to be instantiated twice in the game, once for each player.

    Methods:
        set_name: Sets the name attribute for the player.
        get_name: Gets the name attribute for the player.
        set_num: Sets the player number (either 1 or 2).
        get_num: Gets the player number.
        set_token: Sets the token (X or O) for the player.
        get_token: Gets the token of the player.
        print_welcome_statement: Prints the welcome statement to acknowledge player.
    """
    def __init__(self) -> None:
        print('player created!')

    def set_name(self, name: str) -> None:
        """Sets the name of the player"""
        self.name = name
    
    def get_name(self) -> str:
        """Returns the name of the player"""
        return self.name

    def set_num(self, num: int) -> None:
        """Sets the player number"""
        self.num = num

    def get_num(self) -> int:
        """returns the player number"""
        return self.num

    def set_token(self, token: str) -> None:
        """Sets the token for the player (Either X or O)"""
        self.token = token

    def get_token(self) -> str:
        """Returns the token for the player"""
        return self.token
    
    def print_welcome_statement(self) -> None:
        """Prints statement to acknowledge the player"""
        print(f'Welcome! Player {self.num}, {self.name}, token: {self.token}\n')