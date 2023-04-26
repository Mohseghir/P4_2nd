import random
import string
from datetime import date, timedelta
from Player import Player


def generate_players(num_players):
    first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Julia']
    last_names = ['Smith', 'Johnson', 'Brown', 'Taylor', 'Jones', 'Garcia', 'Davis', 'Rodriguez', 'Wilson', 'Martinez']
    players = []
    for i in range(num_players):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        year = random.randint(1950, 2005)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        birthday = date(year, month, day)
        id_letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        id_digits = ''.join(random.choices(string.digits, k=5))
        player_id = f"{id_letters}{id_digits}"
        player = Player(id=player_id, first_name=first_name, last_name=last_name, birthday=birthday)
        players.append(player)
    return players

def print_players(players):
    for player in players:
        print("Player ID: {}".format(player.id))
        print("First Name: {}".format(player.first_name))
        print("Last Name: {}".format(player.last_name))
        print("Birthday: {}".format(player.birthday))