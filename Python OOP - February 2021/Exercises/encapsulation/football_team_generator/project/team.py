from project.player import Player


class Team:

    def __init__(self, name: str, rating: float):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        self.__players = value

    def find_instance(self, player_name):
        try:
            filtered_players = [p for p in self.__players if p.name == player_name][0]
            return filtered_players
        except IndexError:
            return

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        player_instance = self.find_instance(player_name)
        if not player_instance:
            return 'Player {} not found'.format(player_name)

        self.__players.remove(player_instance)
        return player_instance

