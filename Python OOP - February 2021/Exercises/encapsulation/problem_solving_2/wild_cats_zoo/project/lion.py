class Lion:

	def __init__(self, name: str, gender: str, age: int or float):
		self.name = name
		self.gender = gender
		self.age = age

	@staticmethod
	def get_needs():
		money_to_tend = 50
		return money_to_tend

	def __repr__(self):
		return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'