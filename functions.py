"""Script with functions to tie together program for main"""


def player_creator(player_one, player_two) -> None:
    """Assigns name, num, and token to both players

    Args:
        player_one (object: Player class): first player.
        player_two (object: Player class]: second player.
    """
    tokens = ['X', 'O']

    name_one = input("Player 1, what is your name?: ")
    while True:
        token_one = input("Player 1, Choose a token (Either X or O)\nEnter here: ")
        if token_one.upper() in tokens:
            tokens.remove(token_one.upper())
            break
        print('Please choose either X or O\n')
    name_two = input("Player 2, what is your name?: ")
    token_two = tokens[0]
    print(f'Player 2 token: {token_two}')

    player_one.set_name(name_one)
    player_one.set_num(1)
    player_one.set_token(token_one)

    player_two.set_name(name_two)
    player_two.set_num(2)
    player_two.set_token(token_two)


def show_basic_rules(display, grid) -> None:
    """Prints the basic rules of the game and signifies start"""
    print('Use the numbers 1-9 to select where to place your token in the grid\n')
    display.show_possible_moves_grid(grid.get_internal_grid())
    input('Press enter to start: ')


def check_end_game(grid, display, current_player) -> bool:
    """Checks if game either tied or won
    
    Args:
        grid (object; instance of Grid class): Created in the beginning of main.
        current_player (object; instance of Player class): The player who's turn it is.
        display (object; instance of Display class): Created in the beginning of main.

    Returns:
        bool: False if game is over, True if ongoing. Directly passed to ongoing 
            variable to understand when to stop the game.
    """
    if grid.check_win():
        display.show_win(current_player)
        return False

    elif grid.check_tie():
        display.show_tie()
        return False

    return True


def play_turn(grid, player) -> None:
    """Executes everything needed for one turn/move

    Args:
        grid (object; instance of Grid class): The grid object created in the very beginning.
        player (object; instance of Player class): The player object created in the very beginning.
    """
    token: str = player.get_token()
    print(f"Player {player.get_num()}'s turn\n")

    while True:  # Player enters move, which is then validated.
        try:
            move: int = int(input('Enter your move here: '))
            if (move < 1) or (move > 9):  # Out of range.
                print('Please enter a number between 1 and 9\n')
                continue
            elif not grid.check_valid(move): # Check if token already placed there.
                print('Enter a valid move please!\n')
                continue
            else:
                break   
        except ValueError: # Value entered not an int.
            print('Enter a number please!\n')
            continue
    
    grid.set_internal_grid(move, token)  # Assigns token to position in grid.