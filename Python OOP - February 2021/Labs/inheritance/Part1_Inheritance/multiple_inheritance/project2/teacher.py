from project2.person import Person
from project2.employee import Employee


class Teacher(Person, Employee):

    def teaching(self):
        return 'teaching'

