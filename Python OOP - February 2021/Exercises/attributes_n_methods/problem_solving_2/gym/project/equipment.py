class Equipment:

	id = 0

	def __init__(self, name: str):
		self.id = Equipment.get_next_id()
		self.name = name

	@staticmethod
	def get_next_id():
		id = Equipment.id + 1
		Equipment.id = id
		return id

	def __repr__(self):
		return f'Equipment <{self.id}> {self.name}'
