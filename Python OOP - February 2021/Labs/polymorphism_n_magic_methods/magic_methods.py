from abc import ABC, abstractmethod
import math


class Serializer(ABC):

    @abstractmethod
    def serialize(self, obj):
        pass


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

    # overriding magic method
    def __add__(self, other):
        return Square(self.width + other.width)


s1 = Square(3)
s2 = Square(4)

print(s1 + s2)

