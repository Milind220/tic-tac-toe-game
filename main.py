"""Main script for the tic tac toe game. Run to play game."""


from display import Display
from grid import Grid
from player import Player
import functions


def main() ->  None:
    grid = Grid()
    display = Display()
    
    # main while loop begins. Each iteration of this loop is 'one game'.
    game_counter: int = 1
    game: bool = True
    while game:

        player_one = Player()
        player_two = Player()
        functions.player_creator(player_one, player_two) # Assigns name, num, token

        functions.show_basic_rules(display, grid)
        
        ongoing = True
        while ongoing:
        # game_turns while loop begins. each loop through is one turn.
            
            # maybe make a play_turn function w player 1 or 2 as arg

            ## grid is displayed
            ## player is asked to enter turn
            ## turn validity is checked
            ## turn is accepted and grid updated
            ## loop ends, next turn begins from top of loop
            pass
        pass


if __name__ == '__main__':
    main()