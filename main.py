from Player import Player
from PlayerView import PlayerView
from round_controller import RoundController
from utils import generate_players

def print_players(players):
    for player in players:
        print("Player ID: {}".format(player.id))
        print("First Name: {}".format(player.first_name))
        print("Last Name: {}".format(player.last_name))
        print("Birthday: {}".format(player.birthday))

def main():
    num_players = int(input("How many players do you want to create? "))
    players = generate_players(num_players)
    print("List of players:")
    print_players(players)

    round_controller = RoundController(round_num=1, players=players)
    round_controller.generate_matches()
    round_controller.display_matches()
    round_controller.input_scores()


if __name__ == '__main__':
    main()
