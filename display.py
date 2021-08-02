"""Script for Display class"""

from typing import Tuple


class Display:
    _display_init = ['   |   |   \n', '-----------']

    def __init__(self, 
                 player: int = 1,
                 ongoing: bool = True,
                 ) -> None:
        self.player = player,
        self.ongoing = ongoing,
        self.display_grid: str = self._set_init_display()
    
    def _set_init_display(self) -> str:
        result = ''
        for i in range(1,12):
            if i == 4 or i == 8:
                result += self._display_init[1]
            else:
                result += self._display_init[0]
        return result
    
    def show_invalid_move(self) -> None:
        print(f'Sorry player {self.player}! that move is invalid. Try again!')
    
    def show_win(self) -> None:
        print(f'Player {self.player} has won the game!')
    
    def show_tie(self) -> None:
        print(f"Oh no! The game's a tie!")
    