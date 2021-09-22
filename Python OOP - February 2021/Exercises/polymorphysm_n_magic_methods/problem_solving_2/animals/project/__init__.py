from problem_solving_2.animals.project.cat import Cat
from problem_solving_2.animals.project.dog import Dog
from problem_solving_2.animals.project.kitten import Kitten
from problem_solving_2.animals.project.tomcat import Tomcat


c1 = Cat('asd', 1, 'Male')
d1 = Dog('asd1', 2, 'Female')
t1 = Tomcat('asddasd', 1.5)
k1 = Kitten('asdasdgsdfea', 2)

print(c1)
print(d1)
print(t1)
print(k1)

print(c1.make_sound())
print(d1.make_sound())
print(t1.make_sound())
print(k1.make_sound())