from abc import abstractmethod
from project.animals.animal import Animal
from project.food import Vegetable, Fruit, Meat, Seed


class Mammals(Animal):

    @abstractmethod
    def __init__(self, name, weight, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region


class Mouse(Mammals):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if isinstance(food, (Vegetable, Fruit)):
            self.weight += 0.10
            self.food_eaten += 1
            return
        return f"{__class__.__name__} does not eat {food.__class__.__name__}!"


class Dog(Mammals):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 0.40 * food.quantity
            self.food_eaten += food.quantity
            return
        return f"{__class__.__name__} does not eat {food.__class__.__name__}!"


class Cat(Mammals):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if isinstance(food, (Vegetable, Meat)):
            self.weight += 0.30 * food.quantity
            self.food_eaten += food.quantity
            return
        return f"{__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammals):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 1.00 * food.quantity
            self.food_eaten += food.quantity
            return
        return f"{__class__.__name__} does not eat {food.__class__.__name__}!"
