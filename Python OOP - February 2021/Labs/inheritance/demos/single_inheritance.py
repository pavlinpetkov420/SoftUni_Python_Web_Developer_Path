
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello! I am {self.name} \/ {self.age} yo.')


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        # super(Employee, self).__init__(name, age) # old way
        # Person.__init__(self, name, age) # not a good practice -> only on emergencies cases
        self.salary = salary

    # overwriting 
    def say_hello(self):
        super().say_hello()
        print(f'My salary is {self.salary}')


emp = Employee('Callyou', 23, 100010101393214892)
emp.say_hello()
