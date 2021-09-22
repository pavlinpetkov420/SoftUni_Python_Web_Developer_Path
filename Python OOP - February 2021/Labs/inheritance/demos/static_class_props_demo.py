

class Person:

    MIN_AGE = 0
    MAX_AGE = 160

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # @staticmethod
    # def __validate_age(value):
    #     if value < MIN_AGE or MAX_AGE < value:
    #         raise ValueError('Age Error!')

    @classmethod
    def __validate_age(cls, value):
        if value < cls.MIN_AGE or cls.MAX_AGE < value:
            raise ValueError('Age Error!')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value

    def say_hello(self):
        print(f'Hello! I am {self.name} \/ {self.age} yo.')

    def __repr__(self):
        return ';\n'.join(f'{key} = {value}' for (key, value) in self.__dict__.items())


class Employee(Person):
    MIN_AGE = 16

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    # @staticmethod
    # def __validate_age(value):
    #     if value < MIN_AGE or MAX_AGE < value:
    #         raise ValueError('Employee Age Error!')

    # @property
    # def age(self):
    #     return self.__age
    #  this way makes the code to wun slowly
    # @age.setter
    # def age(self, value):
    #     self.__validate_employee_age(value)
    #     self.__age = value


emp = Employee('CallYou', 13, 1002103)
print(emp.age)
print(emp)
