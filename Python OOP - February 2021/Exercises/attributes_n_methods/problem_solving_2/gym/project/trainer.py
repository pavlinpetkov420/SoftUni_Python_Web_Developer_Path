class Trainer:

	id = 0

	def __init__(self, name: str):
		self.id = Trainer.get_next_id()
		self.name = name

	@staticmethod
	def get_next_id():
		id = Trainer.id + 1
		Trainer.id = id
		return id

	def __repr__(self):
		return f'Trainer <{self.id}> on {self.name}'
