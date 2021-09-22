from problem_solving_2.multiple_inheritance.project.employee import Employee
from problem_solving_2.multiple_inheritance.project.person import Person


class Teacher(Person, Employee):

    def teach(self):
        return 'teaching...'

