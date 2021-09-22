class ExercisePlan:

	id = 0

	def __init__(self, trainer_id: int, equipment_id: int, duration: int):
		self.id = ExercisePlan.get_next_id()
		self.trainer_id = trainer_id
		self.equipment_id = equipment_id
		self.duration = duration

	def __repr__(self):
		return f'Plan <{self.id}> with duration {self.duration} minutes'

	@staticmethod
	def get_next_id():
		id = ExercisePlan.id + 1
		ExercisePlan.id = id
		return id

	@classmethod
	def from_hours(cls, trainer_id: int, equipment_id: int, duration: int):
		return ExercisePlan(trainer_id, equipment_id, duration)
