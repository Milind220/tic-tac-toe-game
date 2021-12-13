"""Script for Player class"""


class Player:
    """Class to represent a player in the game
    
    Meant to be instantiated twice in the game, once for each player.

    Methods:
        get_name: Gets the name attribute for the player.
        set_num: Sets the player number (either 1 or 2).
        get_num: Gets the player number.
        set_token: Sets the token (X or O) for the player.
        get_token: Gets the token of the player.
        print_welcome_statement: Prints the welcome statement to acknowledge player.
    """

    def __init__(self, name: str = "", num: int = 1, token: str = ""):
        self.name = name
        self.num = num
        self.token = token

    def print_welcome_statement(self) -> None:
        """Prints statement to acknowledge the player"""
        print(f"Welcome! Player {self.num}, {self.name}, token: {self.token}\n")
