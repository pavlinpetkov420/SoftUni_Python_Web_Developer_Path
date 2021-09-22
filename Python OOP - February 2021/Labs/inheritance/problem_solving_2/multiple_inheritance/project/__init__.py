from problem_solving_2.multiple_inheritance.project.person import Person
from problem_solving_2.multiple_inheritance.project.employee import Employee
from problem_solving_2.multiple_inheritance.project.teacher import Teacher


p = Person()
e = Employee()
t = Teacher()

print(p.sleep(), type(p).__name__)
print(e.get_fired(), type(e).__name__)
print(t.sleep(), type(t).__name__)
print(t.get_fired(), type(t).__name__)
print(t.teach(), type(t).__name__)