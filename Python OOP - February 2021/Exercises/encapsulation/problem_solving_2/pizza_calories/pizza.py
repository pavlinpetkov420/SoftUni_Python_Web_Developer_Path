from problem_solving_2.pizza_calories.dough import Dough
from problem_solving_2.pizza_calories.topping import Topping


class Pizza:

    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.name = name
        self.dough = dough
        self.toppings = {}
        self.toppings_capacity = toppings_capacity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if isinstance(value, Dough):
            self.__dough = value

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, value):
        self.__toppings = value

    def add_topping(self, topping: Topping):
        if len(self.toppings) >= self.toppings_capacity:
            raise ValueError('Not enough space for another topping')
        if topping.topping_type in self.toppings.keys():
            self.toppings[topping.topping_type] += topping.weight
            return
        self.toppings[topping.topping_type] = topping.weight
        return

    def calculate_total_weight(self):
        total_weight = self.dough.weight
        total_weight += sum([w for tt, w in self.toppings.items()])
        return total_weight
