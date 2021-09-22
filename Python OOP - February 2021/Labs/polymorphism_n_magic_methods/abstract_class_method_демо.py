import json
import math

from abc import ABC, abstractmethod
# look abc library - necessary for abstract classes n methods ;)


class Serializer(ABC):
    def __init__(self, print_func):
        self.print_func = print_func

    @abstractmethod
    def serialize(self, obj):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

    def print(self, obj):
        self.print_func(self.serialize(obj))


class JsonSerializer(Serializer):
    def serialize(self, obj):
        return json.dumps(obj.__dict__)


class Shape:

    def __init__(self):
        if type(self) == Shape:
            raise TypeError("Shape is abstract")

    def area(self):
        raise TypeError('area() is abstract')


class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius * self.__radius


# print(Shape())
# print(Circle(7))

JsonSerializer(print)\
    .print(Circle(10))

Serializer(print)