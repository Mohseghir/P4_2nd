class Player:
    players_count = 0  # variable de classe pour le nombre de joueurs créés

    def __init__(self, id, first_name, last_name, birthday):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday

    @staticmethod
    def generate_id(first_name, last_name):
        Player.players_count += 1
        return f"{first_name[:2].upper()}{last_name[:2].upper()}{Player.players_count:05d}"

    # Getters
    def get_id(self):
        return self._id

    def get_last_name(self):
        return self._last_name

    def get_first_name(self):
        return self._first_name

    def get_birthday(self):
        return self._birthday

    # Setters
    def set_id(self, id):
        self._id = id

    def set_last_name(self, last_name):
        self._last_name = last_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_birthday(self, birthday):
        self._birthday = birthday
