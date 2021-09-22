"""
Usage of an object(from class that inherits other) though the interface of their base(Parent) class.
Example: Circle inherits Shape, so circle instance
can be user from an instance of type Shape.
"""
import math
from abc import ABC, abstractmethod


class Shape:
    def perimeter(self):
        pass

    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * self.radius * math.pi

    def area(self):
        return (self.radius ** 2) * math.pi


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class Serializer(ABC):

    @abstractmethod
    def serialize(self, obj):
        pass


class JsonSerializer(Serializer):

    def serialize(self, obj):
        pass


class TextSerializer(Serializer):

    def serialize(self, obj):
        pass


def get_serializer(type):
    if type == 'json':
        return JsonSerializer()
    else:
        return TextSerializer()


type = 'json'
get_serializer(type)\
    .serialize(Square(3))


circle = Circle(10)
rect = Rectangle(5, 4)
square = Square(4)

print(isinstance(circle, Circle))
print(isinstance(circle, Shape))
print(isinstance(circle, object))


def print_shape(s: Shape):
    print(s.perimeter())
    print(s.area())


def print_shapes(shapes: [Shape]):
    for s in shapes:
        print_shape(s)


print_shapes([circle, Shape(), rect, square])


print(dir(Square))



s1 = Square(3)
s2 = Square(4)

print(Serializer.serialize(s1 + s2))
