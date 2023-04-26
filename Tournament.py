class Tournament:
    def __init__(self, name, place, start_date, end_date, rounds_list, current_round, registered_players, director_description):
        self._name = name
        self._place = place
        self._start_date = start_date
        self._end_date = end_date
        self._rounds_list = rounds_list
        self._current_round = current_round
        self._registered_players = registered_players
        self._director_description = director_description

    # Getters
    def get_name(self):
        return self._name

    def get_place(self):
        return self._place

    def get_start_date(self):
        return self._start_date

    def get_end_date(self):
        return self._end_date

    def get_rounds_list(self):
        return self._rounds_list

    def get_current_round(self):
        return self._current_round

    def get_registered_players(self):
        return self._registered_players

    def get_director_description(self):
        return self._director_description

    # Setters
    def set_name(self, name):
        self._name = name

    def set_place(self, place):
        self._place = place

    def set_start_date(self, start_date):
        self._start_date = start_date

    def set_end_date(self, end_date):
        self._end_date = end_date

    def set_rounds_list(self, rounds_list):
        self._rounds_list = rounds_list

    def set_current_round(self, current_round):
        self._current_round = current_round

    def set_registered_players(self, registered_players):
        self._registered_players = registered_players

    def set_director_description(self, director_description):
        self._director_description = director_description
