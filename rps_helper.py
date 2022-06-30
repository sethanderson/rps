# Win conditions
from rps_game_state import get_game_states


TIE = "tie!!\n"
STEVE_WINS = "        STONE COLD WINS!!!\n"
ROCK_WINS = "        THE ROCK WINS!!!\n"
YOU_WIN = "YOU WIN!!!\n"

STEVE_NAME = "Stone Cold Steve Austin"
ROCK_NAME = 'Dwayne "The Rock" Johnson'

rps_game = get_game_states()
rps_choices = list(rps_game.keys())
last_rps_choice = rps_choices.pop()
PROMPT_USER = f"{', '.join(rps_choices)}, or {last_rps_choice}, baby? ".capitalize()
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
    print(ROCK_WINS)


# Steve Austin Won
def _steve_austin_wins():
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
    print(STEVE_WINS)


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
        print(
            f"You dumbass, you have to pick one of these: {', '.join(input_choices)}\n"
        )
        user_choice = input(user_prompt).casefold()

    return user_choice
