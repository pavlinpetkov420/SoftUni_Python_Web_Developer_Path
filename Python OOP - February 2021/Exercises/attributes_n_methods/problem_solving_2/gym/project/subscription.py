class Subscription:

	id = 0

	def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
		self.id = Subscription.get_next_id()
		self.date = date
		self.exercise_id = exercise_id
		self.trainer_id = trainer_id
		self.customer_id = customer_id


	@staticmethod
	def get_next_id():
		id = Subscription.id + 1
		Subscription.id = id
		return id

	def __repr__(self):
		return f'Subscription <{self.id}> on {self.date}'
