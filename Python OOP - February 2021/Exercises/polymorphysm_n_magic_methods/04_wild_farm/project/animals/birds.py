from abc import abstractmethod
from project.animals.animal import Animal
from project.food import Vegetable, Fruit, Meat, Seed


class Bird(Animal):
    @abstractmethod
    def __init__(self, name, weight, wing_size: float):
        super(Bird, self).__init__(name, weight)
        self.wing_size = wing_size


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super(Owl, self).__init__(name, weight, wing_size)

    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 0.25 * food.quantity
            self.food_eaten += food.quantity
            return
        return f"{__class__.__name__} does not eat {food.__class__.__name__}!"


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super(Hen, self).__init__(name, weight, wing_size)

    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

    def make_sound(self):
        return 'Cluck'

    def feed(self, food):
        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity
        return
