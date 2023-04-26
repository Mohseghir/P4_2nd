import random

from Match import Match
from match_view import MatchView
from match_contoller import MatchController
from Player import Player
from utils import generate_players


class RoundController:
    def __init__(self, round_num, players):
        self.round_num = round_num
        self.players = players
        self.matches = []
        self.match_view = MatchView()

    def generate_matches(self):
        # Generate matches for the current round
        num_matches = len(self.players) // 2
        for i in range(num_matches):
            player1 = self.players[i * 2]
            player2 = self.players[i * 2 + 1]
            match = Match(player1, player2)
            self.matches.append(match)

        # Display the matches
        self.match_view.display_matches(self.matches, self.round_num)

    def input_scores(self):
        for match in self.matches:
            print(f"Enter scores for match: {match._player_1.id} vs {match._player_2.id}")
            score1 = int(input(f"Enter score for {match._player_1.first_name}: "))
            score2 = int(input(f"Enter score for {match._player_2.first_name}: "))
            match.update_scores(score1, score2)

        # Display the updated matches with scores
        self.match_view.display_matches(self.matches, self.round_num)

    def display_matches(self):
        print("\nMatches:")
        for match in self.matches:
            print(f"{match._player_1.id} vs {match._player_2.id}")

    def get_matches(self):
        return self.matches


"""
def generate_matches(self):
    player_ids = [player.id for player in self.players]
        num_players = len(player_ids)
        # Shuffle the player ids to randomize the matches
        shuffled_ids = player_ids[:]
        random.shuffle(shuffled_ids)
        for i in range(0, num_players, 2):
            player_1 = self.find_player_by_id(shuffled_ids[i])
            player_2 = self.find_player_by_id(shuffled_ids[i + 1])
            match = Match(player_1, player_2)
            self.matches.append(match)
        self.match_view.display_matches(self.matches, self.round_num)

    def find_player_by_id(self, player_id):
        for player in self.players:
            if player.id == player_id:
                return player
"""

