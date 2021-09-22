from abc import ABC, abstractmethod

from problem_solving_2.wild_farm.project.food import Food


class Animal(ABC):

    @abstractmethod
    def __init__(self, name: str, weight: float, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food: Food):
        pass