from single_player import single_player_game
from two_player import two_player_game

def start_game(mode):
    if mode == "2-player":
        two_player_game()
    else:
        single_player_game(mode)
