from problem_solving_2.hierarchical_inheritance.project.animal import Animal
from problem_solving_2.hierarchical_inheritance.project.cat import Cat
from problem_solving_2.hierarchical_inheritance.project.dog import Dog

c1 = Cat()
d1 = Dog()
a1 = Animal()

print(c1.meow())
print(c1.eat())
print(d1.bark())
print(d1.eat())
print(a1.eat())
