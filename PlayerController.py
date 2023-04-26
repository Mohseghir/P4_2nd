from Player import Player
from PlayerView import PlayerView
from utils import generate_players


class PlayerController:
    def __init__(self):
        self.view = PlayerView()

    def generate_players(self, num_players):
        players = generate_players(num_players)
        self.view.display_players(players)
