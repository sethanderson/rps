import random

# Game states
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
RPS = [ROCK, PAPER, SCISSORS]

# Win conditions
TIE = "tie!!\n"
STEVE_WINS = "STONE COLD WINS!!!\n"
ROCK_WINS = "THE ROCK WINS!!!\n"
YOU_WIN = "YOU WIN!!!\n"

STEVE_NAME = "Stone Cold Steve Austin"
ROCK_NAME = 'Dwayne "The Rock" Johnson'

PROMPT_USER = "Rock, paper, or scissors baby? "
WANT_REMATCH = "Want a rematch?"
REMATCH_PROMPT = "Yes or no you candyass jabroni? "

# Tie game
def tie_game():
    print(TIE)


# You won
def _you_win():
    print(YOU_WIN)


# The Rock Won
def _the_rock_wins():
    print(ROCK_WINS)
    print(
        """
        ⣶⣿⣾⣷⣷⣾⣿⣿⣿⠋⠀⠀⠀⢠⣾⣿⣿⣿⣶⣤⣤⡀⠀⠀⢀⠀⢹⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣷⣸⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⡿⡟⠀⠀⠀⠀⢿⣿⣿⣿⢷⣿⣿⣿⣿⣿⣿⣿⠿⠁⠃⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⡄⡘⣤⠀⢀⣾⣿⣻⡿⢿⣿⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⡉⣩⠀⣦⡙⠟⠟⠛⢓⠀⠙⢿⣿⣿⣿⣿⡧⠀⠀⣾⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⢿⣯⣿⢸⣿⣷⡗⠀⠀⠁⠒⠠⢀⢰⡿⠻⠼⠓⠂⠘⢿⣿⣿⣿
        ⣻⣿⡟⣯⣿⢋⣯⡟⣿⠏⠿⣿⣧⠀⠀⠀⠀⠀⠀⣨⡇⠀⠀⠀⠀⠀⣈⣿⣿⣿
        ⣿⣿⠿⣟⣻⣿⣿⣇⡟⡀⠀⣹⣿⣷⣦⣤⣤⣦⣾⣿⠇⠀⠀⠀⠀⢀⣾⣿⣿⣿
        ⣿⠃⠐⢩⣿⣿⢟⠟⠃⠀⠀⢸⣿⣿⣿⣿⡟⠿⢿⣿⡄⢰⡆⠀⢀⣿⣿⣿⣿⣿
        ⡏⡄⠀⠀⢻⡁⠀⠀⠀⠀⠐⠅⢻⣿⣿⣿⣿⣶⡄⠀⠀⠀⠁⢀⣾⣿⣿⣿⣿⣿
        ⠔⠀⠀⠀⠈⢟⢄⠀⠀⠀⠀⠈⠘⠛⢷⡄⠀⠭⠉⠁⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿
        ⢵⠀⠀⠀⠀⠈⢉⣦⠀⠀⠀⠀⠀⢱⣶⣿⣶⣶⡄⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿
        ⢀⡐⠀⠀⠀⠀⠈⢼⢅⠀⠀⠀⠀⠀⠈⠉⠛⠛⠁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⠐⠀⠠⡀⠀⠀⠀⠈⠛⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⠉⠉⠉⠙⠻⠿⠿⣿⣿
        ⠓⠄⡀⠈⠢⠀⠀⠐⢤⣄⡀⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀⠣⡄⠀⠀⠀⠀⠀⠀⠀
    """
    )


# Steve Austin Won
def _steve_austin_wins():
    print(STEVE_WINS)
    print(
        """
        ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⠟⠋⠉⠛⠛⠫⢍⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⢿⣻⣿⣿⢿⠀⠀
        ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠹⣟⢿⣿⣿⣿⣿⣿⣿⣿⠏⠁⠈⠉⠉⠉⠉⠉⠉⠘⠛⠀
        ⢨⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡴⠀⢿⣿⣿⣿⣿⣿⡷⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⢨⣿⣿⣿⣷⣿⣿⣿⣷⣷⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣢⡸⢤⠀⢻⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⣼⣯⣦⠠⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣷⣯⠀
        ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠘⠓⣿⢲⡣⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⣿⣿⣿⣿⣿⣿⠛⠀
        ⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⢹⠀⠀⠀⠀⠀⠀⠀⡀⠀⡔⢰⠃⢀⢀⣩⣶⡷⣝⢾⠟⣛⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⡿⣀⠀
        ⢠⣿⣿⣿⣿⣿⣿⣿⡿⠟⠿⣿⣿⣞⣄⠀⠀⠄⢈⣀⣀⣀⠁⣠⣶⣾⣗⡿⢿⣽⡿⠃⢹⣾⡼⢿⢹⣿⣿⣿⣿⠓⣿⣿⣿⣿⣿⡇⡏⠀
        ⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢻⣟⠻⠈⢿⣯⣼⠿⡟⡿⠃⠀⠸⡿⡉⠐⠒⠉⠁⠀⢀⣾⡯⣿⣞⣾⣿⣿⣿⣿⣤⣿⣿⣿⣿⣿⡇⡇⠀
        ⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢸⣏⠍⣇⠀⠁⠉⠈⠉⠀⢀⠀⠀⠹⣗⡀⠀⠀⠀⢀⡼⠁⢧⣏⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⡇⠀
        ⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣻⣿⡄⠸⠦⡀⠀⠀⠀⡰⣈⣄⠀⣤⣧⡯⠢⠀⠀⢾⡇⠀⢸⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⡿⠀
        ⢸⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣼⣿⣿⣄⠇⠁⠊⠀⢠⠃⣸⣩⢻⣟⢿⣿⣴⢤⣄⠈⢇⠀⠈⣇⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
        ⢸⣿⣿⣿⡿⠛⠛⠃⠀⠀⠀⣿⣯⠉⣿⣿⣦⠈⢲⢨⣿⣿⣼⠽⡯⠽⠷⠟⢻⣿⣆⡋⢀⡼⠏⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
        ⢨⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⢰⣿⢿⣦⣠⢸⡿⠁⠀⢀⣖⣶⡤⡄⠒⣈⣿⣇⣾⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀
        ⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⢠⢇⡆⣴⣿⠇⠀⢻⣧⡙⢷⣄⡀⠀⠀⠐⠀⣠⣄⢼⣿⣿⡿⠇⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
        ⢸⣿⣿⠀⠀⠀⡸⠀⠀⠀⡸⢾⣽⣿⣻⠇⠀⠀⡇⠉⢿⣿⣼⣳⣆⣾⣯⣿⣿⣾⣿⡿⡟⠀⠀⠀⡌⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀
        ⢸⣿⡇⠀⠀⠐⠁⠀⠀⠀⠃⠀⠈⠙⡟⠀⠀⢀⣽⢀⠀⠈⠙⣿⠿⡿⣿⣿⣿⡿⠋⠉⠀⠀⠀⣀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⠀
        ⢸⣿⣧⡀⠀⢀⣀⠀⠀⠀⠀⠀⠀⡜⠀⡀⠀⣴⣹⡼⡈⠑⠒⠄⠀⠡⢄⡀⣀⣤⠄⠄⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⠀
        ⢸⣿⣿⣿⣷⣄⣀⣑⡞⠳⠀⢐⣧⢷⠞⡥⢚⣱⣿⠂⢱⣤⣄⣈⣀⣀⣀⣴⣦⣥⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
        ⢰⣿⣿⣿⣿⣿⣿⣍⠋⠓⠢⢐⣟⣐⡂⠠⡋⠈⠁⢠⡎⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
        ⢸⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⡀⠀⣁⠬⡥⢂⣠⣾⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀
        ⢠⣿⣿⣿⣿⣿⣿⣿⣿⣷⠰⠄⢄⡢⠔⡿⠃⠈⡐⡼⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀
        ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⢈⠓⠘⣁⣴⠀⣈⡭⢿⠁⢊⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⠁
        ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠂⠉⠀⠀⠁⢠⣾⠄⠘⣾⣿⣿⣿⣿⣿⣿⣿⣟⣿⠽⠿⠭⠭⠿⢽⣛⣿⣿⣿⣿⣿⣿⡿⠋⠘⣿⣿⠀
        ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢀⢠⡟⠁⠀⠀⢻⡯⠿⣿⠻⣿⣿⡿⡇⠀⠀⠀⢸⠀⠀⠀⢀⡈⠙⡟⠻⣿⣟⡅⠀⠀⢹⣿⠀
        ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠐⠠⠞⠁⠀⠠⠀⢴⡇⠀⠀⡄⠀⠀⠀⠣⡀⠀⠀⠈⠀⠀⡜⢉⡠⠀⡇⠀⠈⠻⢵⡀⠀⣽⣗⠀
        ⢘⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⣺⣷⣶⣶⡆⠀⠰⣤⢴⠁⣶⡢⣠⣄⡜⣰⣿⣷⡄⠳⡄⠀⠀⠀⠀⠀⣿⣿⠀
        ⢰⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠸⣹⣿⡇⠀⠀⢿⣯⣷⡙⢿⡧⠀⢴⡿⣛⣉⠄⣸⡄⠀⠀⢤⣀⠀⣹⡿⠄
        ⢸⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⢰⡯⠀⡏⣿⡇⠀⠀⠘⣻⣻⢠⣀⠠⣿⣆⠦⣀⣤⣀⢹⣣⠀⠀⠘⣵⣯⣿⣷⠀
        ⢰⣿⣿⣿⣿⣿⣿⣿⢏⠀⠀⠀⠀⠀⠀⠀⣰⠁⠀⠀⠈⠇⠀⡗⢹⡇⠀⠀⠀⣿⣷⡧⡉⠟⡀⢤⣺⠩⠛⣩⣽⡿⡀⠀⣰⣿⣿⣿⡿⠀
        ⢸⣿⣿⣿⣿⣿⣿⡟⠀⠄⠀⠀⠀⠀⠀⠀⢽⠀⠀⠀⠀⢩⢠⡗⠸⣷⡀⣠⣶⣿⣿⣿⣿⡄⠿⣿⡟⠀⠰⣷⣿⣿⣧⣾⣿⣿⣿⣿⣿⠀
        ⢸⣿⣿⣿⣿⣿⣿⡇⠀⠆⠀⠀⠀⠀⠀⠼⠏⠀⠀⠄⠀⣷⠋⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣳⣀⠀⠀⢀⣠⣷⣿⣿⣿⣿⣿⣿⣿⣿⡷⠀
        ⢸⣿⣿⣿⣿⣿⣿⠻⠀⡀⠀⠀⠀⠀⠀⠐⢛⠀⢀⡃⠈⢯⠐⠠⣄⡿⠛⠉⢹⣿⣿⣿⣿⡷⣾⣭⣿⣿⣿⣿⡿⠋⣾⣿⣿⣿⣿⣿⡵⠀
        ⢸⣿⣿⣿⣿⣿⡏⢀⡇⡘⢦⡀⠀⠀⠀⢠⡆⢀⣚⡼⠃⢹⠠⢸⣋⡄⠀⠀⠸⣽⣿⣟⠁⠀⠹⣿⣿⣿⣿⣏⡀⠀⣿⣿⣿⣿⣿⣿⡳⠀
        ⢸⣿⣿⣿⣿⣿⣧⡘⣞⡪⠢⣁⠀⠀⢠⡿⠀⠀⠈⡤⢠⠟⡀⢸⢿⣧⡆⢀⣴⣿⣿⡏⠀⠀⡀⠈⢻⣿⣇⡆⠀⠀⡿⣿⣿⣿⣿⣿⡇⠀
        ⢘⣿⣿⣿⣿⣿⣿⣷⡿⣙⡽⢖⠀⠤⠬⠅⡄⠀⠋⠠⣢⡞⣩⣟⣿⣿⣿⣿⣿⣿⣿⠀⠀⢢⣷⡀⠀⢻⣿⢃⠀⠀⢹⣿⣿⣿⣿⣿⣿⠀
        ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣄⠱⡀⠁⠢⣀⡀⠀⠠⠴⠛⡹⢮⣱⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢸⣿⣷⠀⠈⣿⣿⠀⠀⢸⣿⡿⠟⠻⣿⣯⠄
        ⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣏⡀⣀⠄⣈⡀⡀⣄⢀⠀⢁⣿⣟⣻⣻⣛⣿⣻⣿⣿⣲⡶⣮⡿⡟⠖⢶⣾⣟⡷⢲⠶⠳⠴⢶⠆⣿⡿⠁
    """
    )


def ask_to_play_winner(winner):
    print(f"Want to square off with {str(winner)}?")
    print()  # adding additional space


def show_player_results(
    player_1_choice, player_1_name, player_2_choice, player_2_name="You"
):
    print(f"{player_1_name} picked: {str(player_1_choice)}!")
    print(f"{player_2_name} picked: {str(player_2_choice)}!")


def ask_for_rematch():
    print(WANT_REMATCH)
    return _ask_for_input(REMATCH_PROMPT, ["yes", "no"])


def ask_for_game_action(input_choices):
    return _ask_for_input(PROMPT_USER, input_choices)


def player_win(winner="You"):
    if winner == "You":
        _you_win()
    elif winner == ROCK_NAME:
        _the_rock_wins()
    elif winner == STEVE_NAME:
        _steve_austin_wins()


def _ask_for_input(user_prompt, input_choices):
    user_choice = input(user_prompt).casefold()
    while user_choice not in input_choices:
        print(f"You dumbass, you have to pick one of these: {', '.join(input_choices)}\n")
        user_choice = input(user_prompt).casefold()

    return user_choice


# want to see if you can make the whole game into a function
def round1():
    winner = 0

    while winner == 0:
        the_rock = random.choice(RPS)
        stone_cold = random.choice(RPS)
        show_player_results(the_rock, ROCK_NAME, stone_cold, STEVE_NAME)

        if the_rock == stone_cold:
            tie_game()
        elif the_rock == PAPER:
            if stone_cold == SCISSORS:
                _steve_austin_wins()
                winner = STEVE_NAME
            else:
                _the_rock_wins()
                winner = ROCK_NAME
        elif the_rock == SCISSORS:
            if stone_cold == ROCK:
                _steve_austin_wins()
                winner = STEVE_NAME
            else:
                _the_rock_wins()
                winner = ROCK_NAME
        elif the_rock == ROCK:
            if stone_cold == PAPER:
                _steve_austin_wins()
                winner = STEVE_NAME
            else:
                _the_rock_wins()
                winner = ROCK_NAME
