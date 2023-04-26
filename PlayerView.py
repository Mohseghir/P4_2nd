class PlayerView:
    def display_players(self, players):
        print("List of all players:")
        for player in players:
            print(player.id, player.last_name, player.first_name, player.birthday)
