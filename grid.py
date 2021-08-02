"""Script for grid class"""

class Grid:
    def __init__(self,
                 _internal_grid = list(range(9))) -> None:
        self._internal_grid = _internal_grid
        print('grid created!')
    
    def check_valid(self) -> bool:
        pass

    def set_int_grid(self):
        pass

    def check_win(self) -> bool:
        pass

    def check_tie(self) -> bool:
        pass