class Customer:

    def __init__(self, name: str, age: int, id: int):
        self.id = id
        self.name = name
        self.age = age
        self.rented_dvds = []

    def __repr__(self):

        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} " \
               f"rented DVD's ({', '.join([m.name for m in self.rented_dvds])})"
