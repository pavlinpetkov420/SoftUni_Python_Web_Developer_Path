"""
Mixins - classes that gives an extra functionality, which we can add to an already existing classes
(Mixins follows some rules by agreement to developers)
It shouldn't have init method (doesn't need initialization data) -> it should add a functionality to a class
"""


class DefaultReprMixin:

    def __repr__(self):
        return '; '.join(
            f'{key} = {value}'
            for (key, value)
            in self.__dict__.items()
        )


class Person(DefaultReprMixin):

    MIN_AGE = 0
    MAX_AGE = 160

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person, DefaultReprMixin):
    MIN_AGE = 16

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary


class Formatter(DefaultReprMixin):

    def __init__(self, format):
        self.format = format


print(Person('CallYou', 33))
print(Formatter('json'))
print(Employee('CallYou', 33, 1231))
