"""Script with functions to tie together program for main"""


def player_creator(player_one, player_two) -> None:
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


def show_basic_rules() -> None:
    pass
