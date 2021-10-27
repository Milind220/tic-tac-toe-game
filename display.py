"""Script for Display class"""


from typing import List


class Display:
    """Class that displays the game in the command line

    Meant to be instantiated once. Directly displays the game in the 
    command line.

    Methods:
        show_invalid_move: Prints a line to inform a player that the move is invalid.
        show_win: Informs players that the game has been won.
        show tie: Informs the players that the game has been tied.
    """
    _display_init: List[str]= ['   |   |   \n', '-----------\n'] # The two 'lines' that are required to generate a grid.
 
    def __init__(self, 
                 player: int = 1,
                 ongoing: bool = True,
                 ) -> None:
        self.player = player,
        self.ongoing = ongoing,
    
    def show_invalid_move(self) -> None:
        """Prints a line to notify the player that the move is invalid.
        
        This can be displayed if the player tries to place a token in a
        grid-space that is already occupied, or if the player enters a 
        grid-space number outside of the range of possible spaces
        Ex: 19.
        """
        print(f'Sorry player {self.player}! that move is invalid. Try again!')
    
    def show_win(self, player) -> None:
        """Prints a line to notify the player that someone has won the game."""
        name: str = player.get_name()
        num: int = player.get_num()
        print(f'Player {num}, {name} has won the game!')
    
    def show_tie(self) -> None:
        """Prints a line to notify the player that the game has been tied."""
        print(f"Oh no! The game's a tie!")
    
    def show_possible_moves_grid(
        self,
        internal_grid: List[str]
        ) -> None:
        """Prints a grid with remaining possible moves shown by numbers

        Args:
            internal_grid (List[str]): A list of length 9. 
            Contains either token string or blank space string.
        """
        possible_moves_list: List[str] = []
        for index, value in enumerate(internal_grid):
            if value == ' ':
                possible_moves_list.append(str(index+1))
            else:
                possible_moves_list.append(' ')
        display_grid: str = self._make_grid_string(possible_moves_list)
        print(display_grid)

    def show_game_grid(
        self, 
        internal_grid: List[str] # This is internal_grid from Grid class
        ) -> None:
        """Prints the game grid when called

        Args:
            internal_grid (List[str]): A list of length 9. 
            Contains either token string or blank space string.
        """
        game_grid: str = self._make_grid_string(internal_grid)
        print(game_grid)

    def _make_grid_string(
        self,
        grid_list: List[str]
        ) -> str:
        """Makes a displayable grid with the contents of grid_list arg inserted into it.

        Args:
            grid_list (List[Union[str, int]]): A list of length 9 containing everything
            that has to be displayed in the grid

        Returns:
            str: The ready to display grid. Print to show.
        """
        grid: str = ''
        for line_num in range(1,12):
            if line_num in [4, 8]: # Rows with horizontal dividors.
                grid += self._display_init[1]

            elif line_num in [2, 6, 10]: # These are the rows where the grid can have tokens (X or O).
                corrector: int = [2, 6, 10].index(line_num) 
                # This ensures that tokens are taken from the correct three index 
                # positions depending on the row that we are in.

                spot_one: str = grid_list[line_num - (2+corrector)]
                spot_two: str = grid_list[line_num - (1+corrector)]
                spot_three: str = grid_list[line_num - corrector]
                # The lines above extract the information about what is in the internal 
                # grid and assigns it to three variables, corresponding with three 
                # available spaces in the row. 
                # for example, line_num = 2 is the first row which can contain tokens.
                # Here we'd want to insert the three tokens in the 0,1,2 index
                # positions from the internal_grid into the game_grid.

                grid += f' {spot_one} | {spot_two} | {spot_three} \n'
                # The complete row is then concatenated to the game_grid.
            
            else:
                grid += self._display_init[0] # Rows with vertical dividors and blank space.

        return grid
        