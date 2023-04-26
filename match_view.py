class MatchView:
    def display_matches(self, matches, round_num):
        print(f"Round {round_num} Matches:")
        for match in matches:
            print(f"{match._player_1.first_name} {match._player_1.last_name} vs {match._player_2.first_name} {match._player_2.last_name}")
# ou par ID print(f"{match.player1.id} vs {match.player2.id}")