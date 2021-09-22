from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):

    def draw(self):
        print('Drawing Rectangle!')


class Circle(Shape):

    def draw(self):
        print('Drawing Circle!')




"""
VIOLATION!

class Shape(ABC):

    @abstractmethod
    def draw_circle(self):
        pass
        
    def draw_rectangle(self):
        pass


class Rectangle(Shape):
    def draw_circle(self):
        pass
        
    def draw_rectangle(self):    
        print('Drawing Rectangle!')


class Circle(Shape):

    def draw_circle(self):
        print('Drawing Circle!')

    def draw_rectangle(self):    
        pass
"""