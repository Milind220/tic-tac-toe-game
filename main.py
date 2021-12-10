"""Main script for the tic tac toe game. Run to play game."""


from display import Display
from grid import Grid
from player import Player
import functions


def main() -> None:
    grid = Grid()
    display = Display()

    player_one = Player()
    player_two = Player()
    functions.player_creator(player_one, player_two)  # Assigns name, num, token

    functions.show_basic_rules(display, grid)

    ongoing: bool = True
    round_counter: int = 1

    while ongoing:  # Each loop through is one turn.
        if round_counter % 2 != 0:
            current_player = player_one
        else:
            current_player = player_two

        current_grid = grid.get_internal_grid()
        display.show_possible_moves_grid(current_grid)
        display.show_game_grid(current_grid)

        functions.play_turn(grid, current_player)
        ongoing = functions.check_end_game(grid, display, current_player)
        round_counter += 1


if __name__ == "__main__":
    main()
