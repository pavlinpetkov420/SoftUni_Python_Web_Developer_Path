"""
Principles of OOP:
    1.Abstraction
    2.Inheritance
    3.Polymorphism
    4.Encapsulation
    ???5.Exceptions handling
"""

# - hide information
# in Python encapsulation is weak


class Person:
    """
    Example for class that needs encapsulation
    """
    MIN_AGE = 0
    MAX_AGE = 150

    def __init__(self, name: str, age: int):
        self.name = name
        self.set_age(age)

    # get_attr
    @property
    def name(self):
        return self.__name

    # set_attr
    @name.setter
    def name(self, new_name):
        if not new_name:
            raise ValueError("Name cannot be None!!!")
        self.__name = new_name

    # Access for encapsulated information (get and set methods)
    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age < Person.MIN_AGE or Person.MAX_AGE < new_age:
            raise ValueError(f"Error Message!")
        self.__age = new_age


pesho = Person("Pesho", 11)
print(pesho.__dict__)
print(pesho.get_age())

pesho.set_age(19)
print(pesho.__dict__)
print(pesho.get_age())

pesho.name = None
print(pesho.__dict__)
print(pesho.name)

# print(pesho.__age) is giving an ERROR





"""
3 ways for control access:
    - Using single underscore - shows the developers that it is not a good idea to change this 
                 (only if you know what you do) - convention
    - Using double underscore - hidden rename the attribute _class__attribute / if we try to change this value it creates
            a new one ('__var' = new value) 
    - Using getter and setter methods (Pythonic way)
"""

# class Person:
#     """
#     just an example :))
#     """
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self._age = age
#
#     def __setattr__(self, key, value):
#         if key.startswith('_') and len(key) > 1 and key[1] != '_':
#             key = f'{self.__class__.__name__}${key}'
#
#         return super().__setattr__(key, value)
#
#     def __getattr__(self, item):
#         return super().__getattribute__(item)


