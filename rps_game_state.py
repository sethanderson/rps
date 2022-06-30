# Game states
BEATS = "beats"
_ROCK = "rock"
_PAPER = "paper"
_SCISSORS = "scissors"
_LIZARD = "lizard"
_SPOCK = "spock"

# traditional RPS
# _RPS_GAME = {
#     _ROCK: {BEATS: [_SCISSORS]},
#     _PAPER: {BEATS: [_ROCK]},
#     _SCISSORS: {BEATS: [_PAPER]},
# }

# lizard spock RPS
_RPS_GAME = {
    _SCISSORS: {BEATS: [_PAPER, _LIZARD]},
    _PAPER: {BEATS: [_ROCK, _SPOCK]},
    _ROCK: {BEATS: [_LIZARD, _SCISSORS]},
    _LIZARD: {BEATS: [_SPOCK, _PAPER]},
    _SPOCK: {BEATS: [_SCISSORS, _ROCK]},
}


def get_game_states():
    return _RPS_GAME
