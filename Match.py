class Match:
    def __init__(self, player_1, player_2, score_1=None, score_2=None):
        self._player_1 = player_1
        self._player_2 = player_2
        self._score_1 = score_1
        self._score_2 = score_2

    def get_scores(self):
        return self._score_1, self._score_2

    def update_scores(self, score_1, score_2):
        self._score_1 = score_1
        self._score_2 = score_2

    # Getters
    def get_player_1(self):
        return self._player_1

    def get_player_2(self):
        return self._player_2

    def get_score_1(self):
        return self._score_1

    def get_score_2(self):
        return self._score_2

    # Setters
    def set_player_1(self, player_1):
        self._player_1 = player_1

    def set_player_2(self, player_2):
        self._player_2 = player_2

    def set_score_1(self, score_1):
        self._score_1 = score_1

    def set_score_2(self, score_2):
        self._score_2 = score_2
