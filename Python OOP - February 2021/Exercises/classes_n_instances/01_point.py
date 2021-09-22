from math import sqrt


class Point:
    """import coordinates(x, y) of point in a coordinate system"""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    """change x value"""
    def set_x(self, new_x: int):
        self.x = new_x

    """change y value"""
    def set_y(self, new_y: int):
        self.y = new_y

    """return the distance between instance point and the one in the parameters"""
    def distance(self, x2: int, y2: int):
        distance = sqrt(((self.x - x2)**2) + ((y2 - self.y)**2))
        return distance


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))
