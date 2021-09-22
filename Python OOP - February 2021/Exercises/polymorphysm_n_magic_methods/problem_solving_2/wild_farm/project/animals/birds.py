from problem_solving_2.wild_farm.project.animals.animal import Animal
from problem_solving_2.wild_farm.project.food import Meat


class Bird(Animal):

    def __init__(self, name, weight, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        pass

    def make_sound(self):
        pass


class Owl(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight:.01f}, {self.food_eaten}]"

    def make_sound(self):
        return 'Hoot Hoot'

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 0.25 * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

    def make_sound(self):
        return 'Cluck'

    def feed(self, food):
        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity

