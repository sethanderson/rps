from concurrent.futures import thread
import random
from rps_helper import (
    tie_game,
    ask_to_play_winner,
    show_player_results,
    ask_for_rematch,
    player_win,
    ROCK_NAME,
    STEVE_NAME,
)

# testicles = [1, 3, 5, 7, 45]

# print( "the complete list of testes is: " + str(testicles))

# random_teste = random.choice(testicles)

# print ("The randomly selected testicle is : " + str(random_teste))

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
            winner = STEVE_NAME
        else:
            winner = ROCK_NAME
        player_win(winner)
    elif the_rock == SCISSORS:
        if stone_cold == ROCK:
            winner = STEVE_NAME
        else:
            winner = ROCK_NAME
        player_win(winner)
    elif the_rock == ROCK:
        if stone_cold == PAPER:
            winner = STEVE_NAME
        else:
            winner = ROCK_NAME
        player_win(winner)


# SECOND MATCH! THIS ONE IS FOR THE BELT
rematch = "yes"
face = ask_to_play_winner(winner)
heel = random.choice(RPS)
show_player_results(heel, winner, face)

while True:
    if heel == face:
        tie_game()
    elif heel == PAPER:
        if face.lower() == SCISSORS:
            player_win()
        else:
            player_win(winner)

    elif heel == SCISSORS:
        if face == ROCK:
            player_win()
        else:
            player_win(winner)

    elif heel == ROCK:
        if face == PAPER:
            player_win()
        else:
            player_win(winner)
    rematch = ask_for_rematch(rematch)
    if rematch == "yes":
        continue
    else:
        break
