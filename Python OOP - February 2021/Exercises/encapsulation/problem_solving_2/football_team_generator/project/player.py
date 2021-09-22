class Player:

    def __init__(self, name: str, endurance: int or float, sprint: int or float, dribble: int or float,
                 passing: int or float, shooting: int or float):
        self.__name = name
        self.__endurance = endurance
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value

    @property
    def endurance(self):
        return self.__endurance

    @endurance.setter
    def endurance(self, value):
        if isinstance(value, float or int):
            self.__endurance = value

    @property
    def sprint(self):
        return self.__sprint

    @sprint.setter
    def sprint(self, value):
        if isinstance(value, float or int):
            self.__sprint = value

    @property
    def dribble(self):
        return self.__dribble

    @dribble.setter
    def dribble(self, value):
        if isinstance(value, float or int):
            self.__dribble = value

    @property
    def passing(self):
        return self.__passing

    @passing.setter
    def passing(self, value):
        if isinstance(value, float or int):
            self.__passing = value

    @property
    def shooting(self):
        return self.__shooting

    @shooting.setter
    def shooting(self, value):
        if isinstance(value, float or int):
            self.__shooting = value

    def __str__(self):
        return f'Player: {self.name}\n' \
               f'Endurance: {self.endurance}\n' \
               f'Sprint: {self.sprint}\n' \
               f'Dribble: {self.dribble}\n' \
               f'Passing: {self.passing}\n' \
               f'Shooting: {self.shooting}\n'
