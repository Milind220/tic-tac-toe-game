"""Script for Player class"""


from typing import Tuple


class Player:
    '''Class to represent a player in the game
    '''
    def __init__(self) -> None:
        print('player created!')

    def set_name(self, name: str = ''):
        self.name = name

    def set_num(self, num: int):
        self.num = num

    def set_token(self, token: str):
        self.token = token

    def set_move(self) -> str:
        move = str(input('Grid space: '))
        return move

    def tell_grid(self, move: int) -> Tuple:
        return (move, self.token)