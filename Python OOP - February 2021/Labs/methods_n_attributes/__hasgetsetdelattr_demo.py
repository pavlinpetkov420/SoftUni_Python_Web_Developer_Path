class Person:
    def __init__(self, name):
        self.name = name

    def set_later_value(self):
        self.age = 18

    def set_dict_value(self):
        self.__dict__['something'] = 5

    def __repr__(self):
        return '; '.join(f'{k}={v}' for k, v in self.__dict__.items())


pesho = Person('Pesho')
print(pesho.__dict__)
pesho.age = 23
print(pesho.__dict__)
example = str(pesho)
print(example)