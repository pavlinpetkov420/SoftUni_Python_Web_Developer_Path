from problem_solving_2.gym.project.customer import Customer
from problem_solving_2.gym.project.equipment import Equipment
from problem_solving_2.gym.project.trainer import Trainer
from problem_solving_2.gym.project.subscription import Subscription
from problem_solving_2.gym.project.exercise_plan import ExercisePlan


class Gym:

	def __init__(self):
		self.customers = []
		self.equipment = []
		self.trainers = []
		self.plans = []
		self.subscriptions = []

	def add_customer(self, customer: Customer):
		if customer not in self.customers:
			self.customers.append(customer)

	def add_trainer(self, trainer: Trainer):
		if trainer not in self.trainers:
			self.trainers.append(trainer)

	def add_equipment(self, equipment: Equipment):
		if equipment not in self.equipment:
			self.equipment.append(equipment)

	def add_plan(self, plan: ExercisePlan):
		if plan not in self.plans:
			self.plans.append(plan)

	def add_subscription(self, subscription: Subscription):
		if subscription not in self.subscriptions:
			self.subscriptions.append(subscription)

	def subscription_info(self, subscription_id: int):
		subs_info = ''

		for subs in self.subscriptions:
			if subs.id == subscription_id:
				subs_info += f'{subs}\n'
			for customer in self.customers:
				if subs.customer_id == customer.id:
					subs_info += f'{customer}\n'
				for trainer in self.trainers:
					if subs.trainer_id == trainer.id:
						subs_info += f'{trainer}\n'
					for plan in self.plans:
						if plan.trainer_id == subs.trainer_id:
							subs_info += f'{plan}\n'
						for equipment in self.equipment:
							if plan.equipment_id == equipment.id:
								subs_info += f'{equipment}'

		return subs_info
