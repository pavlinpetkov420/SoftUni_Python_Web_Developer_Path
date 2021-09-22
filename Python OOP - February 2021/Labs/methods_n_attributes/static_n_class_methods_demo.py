class Person:
    max_age =140

    def __init__(self, name, age):
        self.validate_age(age)
        self.name = name
        self.age = age

    @staticmethod
    def validate_age(age):
        if age < 0 or Person.max_age < age:
            raise ValueError('Age is invalid')


Person.validate_age(5)
# Person.validate_age(166)

print(Person("asd", 11))
print(Person("asd", 1111))