
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Formatter:

    def format(self, student):
        pass


class NameFormatter:

    def format(self, student):
        return f'Name: {student.name}'


class NameAgeFormatter:

    def format(self, student):
        return f'Name: {student.name}, Age: {student.age}'


class StudentRegistry:

    def __init__(self):
        self.students = []

    def register(self, student):
        self.students.append(student)

    def unregister_student(self, student):
        self.students.pop(self.students.index(student))

    # dependency inversion
    def print_registered(self, formatter=NameFormatter()):
        for student in self.students:
            print(formatter.format(student))


sr = StudentRegistry()

sr.register(Student('Nikola', 19))
sr.print_registered()
sr.print_registered(NameAgeFormatter())