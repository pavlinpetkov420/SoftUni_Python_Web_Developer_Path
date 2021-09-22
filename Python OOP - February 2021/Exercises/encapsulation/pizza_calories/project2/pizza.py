from project2.topping import Topping
from project2.dough import Dough


class Pizza:

    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.__name = name
        self.__dough = dough
        self.__toppings = {}
        self.__toppings_capacity = toppings_capacity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, new_dough):
        self.__dough = new_dough

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, new_capacity):
        self.__toppings_capacity = new_capacity

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, new_topping_info):
        self.__toppings = new_topping_info

    def add_topping(self, topping: Topping):
        if len(self.__toppings) < self.__toppings_capacity:
            if topping.topping_type not in self.__toppings.keys():
                self.__toppings[topping.topping_type] = topping.weight
            else:
                self.__toppings[topping.topping_type] += topping.weight
        else:
            raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self):
        pizza_weight = 0
        pizza_weight += self.dough.weight
        for tt, w in self.__toppings.items():
            pizza_weight += w

        return pizza_weight
