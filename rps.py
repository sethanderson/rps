import random
from rps_game_state import BEATS, get_game_states
from rps_helper import (
    tie_game,
    ask_to_play_winner,
    show_player_results,
    ask_for_rematch,
    ask_for_game_action,
    player_win,
    ROCK_NAME,
    STEVE_NAME,
)


RPS_GAME = get_game_states()
RPS_CHOICES = list(RPS_GAME.keys())

winner = ""
while not winner:
    the_rock, stone_cold = random.choice(RPS_CHOICES), random.choice(RPS_CHOICES)
    show_player_results(the_rock, ROCK_NAME, stone_cold, STEVE_NAME)

    if the_rock == stone_cold:
        tie_game()
        continue

    winner = ROCK_NAME if stone_cold in RPS_GAME[the_rock][BEATS] else STEVE_NAME
    player_win(winner)


# SECOND MATCH! THIS ONE IS FOR THE BELT
rematch = "yes"
face = ask_to_play_winner(winner)

while True:
    face, heel = ask_for_game_action(RPS_CHOICES), random.choice(RPS_CHOICES)
    show_player_results(heel, winner, face)

    if heel == face:
        tie_game()
        continue

    player_win() if heel in RPS_GAME[face][BEATS] else player_win(winner)

    rematch = ask_for_rematch()
    if rematch == "no":
        break
