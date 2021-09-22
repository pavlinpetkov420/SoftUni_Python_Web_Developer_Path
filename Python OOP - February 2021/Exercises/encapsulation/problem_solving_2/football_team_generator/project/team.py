from problem_solving_2.football_team_generator.project.player import Player


class Team:

    def __init__(self, name: str, rating: int or float):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if isinstance(value, float or int):
            self.__rating = value

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        if isinstance(value, Player):
            self.__players.append(value)

    def add_player(self, player: Player):
        if player in self.players:
            return f'Player {self.name} has already joined'
        self.players.append(player)
        return f'Player {player.name} joined team {self.name}'

    def remove_player(self, player: Player):
        if player in self.players:
            self.players.remove(player)
            return player
        return f'Player {player.name} not found'

