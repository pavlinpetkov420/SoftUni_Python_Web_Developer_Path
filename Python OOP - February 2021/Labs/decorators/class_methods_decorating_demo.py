import functools


def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @uppercase
    def print_say_hello(self):
        return f'Hi! I am {self.name}'

    def print_say_hello2(self):
        return f'Hi! I am {self.name}'


p = Person('Jluch', 32)

print(p.print_say_hello())
print(p.print_say_hello2())
