from concurrent.futures import thread
import random
from rps_helper import (
    tie_game,
    you_win,
    steve_austin_wins,
    the_rock_wins,
    ask_to_play_winner,
    show_player_results,
)

# testicles = [1, 3, 5, 7, 45]

# print( "the complete list of testes is: " + str(testicles))

# random_teste = random.choice(testicles)

# print ("The randomly selected testicle is : " + str(random_teste))

STEVE_NAME = "Stone Cold Steve Austin"
ROCK_NAME = 'Dwayne "The Rock" Johnson'

# Game states
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
RPS = [ROCK, PAPER, SCISSORS]

winner = 0

while winner == 0:
    the_rock = random.choice(RPS)
    stone_cold = random.choice(RPS)
    show_player_results(the_rock, ROCK_NAME, stone_cold, STEVE_NAME)

    if the_rock == stone_cold:
        tie_game()
    elif the_rock == PAPER:
        if stone_cold == SCISSORS:
            steve_austin_wins()
            winner = STEVE_NAME
        else:
            the_rock_wins()
            winner = ROCK_NAME
    elif the_rock == SCISSORS:
        if stone_cold == ROCK:
            steve_austin_wins()
            winner = STEVE_NAME
        else:
            the_rock_wins()
            winner = ROCK_NAME
    elif the_rock == ROCK:
        if stone_cold == PAPER:
            steve_austin_wins()
            winner = STEVE_NAME
        else:
            the_rock_wins()
            winner = ROCK_NAME

# SECOND MATCH! THIS ONE IS FOR THE BELT

face = ask_to_play_winner(winner)
heel = random.choice(RPS)
show_player_results(heel, winner, face)

if heel.lower() == face.lower():
    tie_game()
elif heel.lower() == PAPER:
    if face.lower() == SCISSORS:
        you_win()
    else:
        print(f"{str(winner)} WINS!!!")

elif heel == SCISSORS:
    if face == ROCK:
        you_win()
    else:
        print(f"{str(winner)} WINS!!!")

elif heel == ROCK:
    if face == PAPER:
        you_win()
    else:
        print(f"{str(winner)} WINS!!!")
