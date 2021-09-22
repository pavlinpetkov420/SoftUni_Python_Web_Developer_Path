from math import pi

class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius


def get_values(obj, attr_names):
    return [getattr(obj, attr_name) for attr_name in attr_names]


pesho = Person('Pesho', 11, 'Sofia', 'Bulgaria')
print(get_values(pesho, ['city', 'country']))

circle = Circle(4)
print(get_values(circle, ['radius', 'area']))
area_method = get_values(circle, ['area'])[0]


print(getattr(circle, 'radius', None))
print(getattr(circle, 'diameter', None))


print(hasattr(circle, 'radius'))
print(hasattr(circle, 'diameter'))


