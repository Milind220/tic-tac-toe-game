"""Script with functions to tie together program for main"""

import os
from typing import List


def player_creator(player_one, player_two) -> None:
    """Assigns name, num, and token to both players

    Args:
        player_one (object: Player class): first player.
        player_two (object: Player class]: second player.
    """
    tokens: List[str] = ["X", "O"]

    name_one: str = input("Player 1, what is your name?: ")
    while True:
        token_one: str = input("Player 1, Choose a token (Either X or O)\nEnter here: ")
        if token_one.upper() in tokens:
            tokens.remove(token_one.upper())
            break
        print("Please choose either X or O\n")
    clearscreen()
    name_two: str = input("Player 2, what is your name?: ")
    token_two: str = tokens[0]
    print(f"Player 2 token: {token_two}")

    player_one.name = name_one
    player_one.num = 1
    player_one.token = token_one

    player_two.name = name_two
    player_two.num = 2
    player_two.token = token_two
    input("Press enter to continue: ")
    clearscreen()


def show_basic_rules(display, grid) -> None:
    """Prints the basic rules of the game and signifies start"""
    num_char: int = 50
    text: str = "Tic-Tac-Toe: BASIC RULES"
    space_each_side: int = round((num_char - len(text)) / 2)

    print("-" * num_char)
    print(" " * space_each_side, text, " " * space_each_side)
    print("-" * num_char)
    print(
        "\n\n1) First player to get 3 tokens in a line in a row, column or diagonal wins!\n"
    )
    print("2) Use the numbers 1-9 to select where to place your token in the grid\n")
    display.show_possible_moves_grid(grid.internal_grid)
    input("Press enter to start: ")
    clearscreen()


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
    current_grid = grid.internal_grid
    if grid.check_win():
        # Show the grid one last time to the players.
        display.show_game_grid(current_grid)
        display.show_win(current_player)
        return False

    elif grid.check_tie():
        display.show_game_grid(current_grid)
        display.show_tie()
        return False

    return True


def play_turn(grid, player) -> None:
    """Executes everything needed for one turn/move

    Args:
        grid (object; instance of Grid class): The grid object created in the very beginning.
        player (object; instance of Player class): The player object created in the very beginning.
    """
    token: str = player.token
    print(f"Player {player.num}'s turn\n")

    while True:  # Player enters move, which is then validated.
        try:
            move: int = int(input("Enter your move here: "))
            if (move < 1) or (move > 9):  # Out of range.
                print("Please enter a number between 1 and 9\n")
                continue
            elif not grid.check_valid(move):  # Check if token already placed there.
                print("Enter a valid move please!\n")
                continue
            else:
                break
        except ValueError:  # Value entered not an int.
            print("Enter a number please!\n")
            continue

    grid.set_internal_grid(move, token)  # Assigns token to position in grid.
    clearscreen()


def clearscreen(numlines: int = 100) -> None:
    """Clear the console.

    numlines is an optional argument used only as a fall-back.
    Source: Steven D'Aprano, http://www.velocityreviews.com/forums
    """
    if os.name == "posix":  # Unix/Linux/MacOS/BSD/etc
        os.system("clear")
    elif os.name in ("nt", "dos", "ce"):  # DOS/Windows
        os.system("CLS")
    else:  # Fallback for other operating systems.
        print("\n" * numlines)
