class Vet:

	def __init__(self, name: str, age: int or float, salary: int or float):
		self.name = name
		self.age = age
		self.salary = salary

	def __repr__(self):
		return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'
