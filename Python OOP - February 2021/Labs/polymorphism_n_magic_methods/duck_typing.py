"""
alternative of polymorphism
2 classes with common method sound
there is no need of abstract class here
only a method which calls the common method for the current instance
"""


class Cat:

    def sound(self):
        print("MEOW!")


class Dog:

    def sound(self):
        print("BARK!")


def make_sound(animal):
    animal.sound()


cat = Cat()
dog = Dog()
make_sound(cat)
make_sound(dog)
