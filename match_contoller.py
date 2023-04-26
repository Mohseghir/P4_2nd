class MatchController:
    def __init__(self, match, match_view):
        self.match = match
        self.match_view = match_view

    def input_scores(self):
        score_1 = None
        while score_1 is None:
            score1_str = input(
                f"Enter score for {self.match.player_1[0].first_name} {self.match.player_1[0].last_name}: ")
            try:
                score_1 = float(score1_str)
            except ValueError:
                print("Invalid input. Score must be a number.")

        score_2 = None
        while score_2 is None:
            score_2_str = input(
                f"Enter score for {self.match.player_2[0].first_name} {self.match.player_2[0].last_name}: ")
            try:
                score2 = float(score_2_str)
            except ValueError:
                print("Invalid input. Score must be a number.")

        self.match.score_1 = score_1
        self.match.score_2 = score_2
