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
REMATCH_PROMPT = "Yes or no you candyass jabroni?"

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
    user_choice = input(PROMPT_USER)
    print()  # adding additional space
    return user_choice.casefold()


def show_player_results(
    player_1_choice, player_1_name, player_2_choice, player_2_name="You"
):
    print(f"{player_1_name} picked: {str(player_1_choice)}!")
    print(f"{player_2_name} picked: {str(player_2_choice)}!")


def ask_for_rematch(rematch):
    print("Want a rematch?")
    rematch_choice = input(REMATCH_PROMPT)
    print()  # extra space to make little old seth happy 8=====D
    return rematch_choice.casefold()


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


def player_win(winner="You"):
    if winner == "You":
        _you_win()
    elif winner == ROCK_NAME:
        _the_rock_wins()
    elif winner == STEVE_NAME:
        _steve_austin_wins()
