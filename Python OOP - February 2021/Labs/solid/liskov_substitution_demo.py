from abc import ABC, abstractmethod


class Animal:

    def eat(self):
        pass


class SoundMakingAnimal(Animal, ABC):

    @abstractmethod
    def get_sound(self):
        pass


class Mole(Animal):

    def get_sound(self):
        raise TypeError("Moles cannot make sounds!!!")


class Cat(SoundMakingAnimal):
    sound = 'meow'

    def get_sound(self):
        return self.sound


class Dog(SoundMakingAnimal):
    sound = 'woof-woof'

    def get_sound(self):
        return self.sound


class Dragon(SoundMakingAnimal):
    sound = 'BURNIN\'!'

    def get_sound(self):
        return self.sound


def animal_sound(animals: list[SoundMakingAnimal]):
    for animal in animals:
        print(animal.get_sound())


def animals_eat(animals: list[Animal]):
    for animal in animals:
        print(animal.eat())


animals = [Cat(), Dog(), Dragon()]
animal_sound(animals)
animals_eat(animals + [Mole()])


