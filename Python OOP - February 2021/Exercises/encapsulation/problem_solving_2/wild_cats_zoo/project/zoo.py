from problem_solving_2.wild_cats_zoo.project.lion import Lion
from problem_solving_2.wild_cats_zoo.project.tiger import Tiger
from problem_solving_2.wild_cats_zoo.project.cheetah import Cheetah
from problem_solving_2.wild_cats_zoo.project.vet import Vet
from problem_solving_2.wild_cats_zoo.project.caretaker import Caretaker
from problem_solving_2.wild_cats_zoo.project.keeper import Keeper


class Zoo:

	def __init__(self, name: str, budget: float or int, animal_capacity: float or int, workers_capacity: float or int):
		self.name = name
		self.budget = budget
		self.animal_capacity = animal_capacity
		self.workers_capacity = workers_capacity
		self.animals = []
		self.workers = []

	@property
	def budget(self):
		return self.__budget

	@budget.setter
	def budget(self, value):
		if isinstance(value, int) or isinstance(value, float):
			self.__budget = value

	@property
	def animal_capacity(self):
		return self.__animal_capacity

	@animal_capacity.setter
	def animal_capacity(self, value):
		if isinstance(value, int):
			self.__animal_capacity = value

	@property
	def workers_capacity(self):
		return self.__workers_capacity

	@workers_capacity.setter
	def workers_capacity(self, value):
		if isinstance(value, int):
			self.__workers_capacity = value

	def add_animal(self, animal: Tiger or Cheetah or Lion, price):
		if len(self.animals) < self.animal_capacity:
			if self.budget >= price:
				self.animals.append(animal)
				self.budget -= price
				return f'"{animal.name} the {type(animal).__name__} added to the zoo'
			return 'Not enough budget'
		return 'Not enough space for animal'

	def hire_worker(self, worker: Keeper or Caretaker or Vet):
		if len(self.workers) < self.workers_capacity:
			self.workers.append(worker)
			return f"{worker.name} the {type(worker).__name__} hired successfully"
		return 'Not enough space for worker'

	def fire_worker(self, worker_name):
		worker = [w for w in self.workers if w.name == worker_name][0]
		if worker:
			self.workers.remove(worker)
			return f"{worker_name} fired successfully"
		return f"There is no {worker_name} in the zoo"

	def pay_workers(self):
		workers_salaries = sum([w.salary for w in self.workers])
		if self.budget >= workers_salaries:
			self.budget -= workers_salaries
			return f'You payed your workers. They are happy. Budget left: {self.budget}'
		return 'You have no budget to pay your workers. They are unhappy'

	def tend_animals(self):
		needed_money = sum([a.get_needs() for a in self.animals])
		if self.budget > needed_money:
			self.budget -= needed_money
			return f"You tended all the animals. They are happy. Budget left: {self.budget}"
		return "You have no budget to tend the animals. They are unhappy."

	def profit(self, amount):
		self.budget += amount

	def sort_animals_by_type(self):
		lions = [a for a in self.animals if type(a).__name__ == 'Lion']
		tigers = [a for a in self.animals if type(a).__name__ == 'Tiger']
		cheetahs = [a for a in self.animals if type(a).__name__ == 'Cheetah']

		return lions, tigers, cheetahs

	def animals_status(self):
		lions, tigers, cheetahs = self.sort_animals_by_type()
		animals_status = f'You have {len(self.animals)} animals\n' \
			f'----- {len(lions)} Lions:\n'
		for lion in lions:
			animals_status += f'{lion}\n'
		animals_status += f'----- {len(tigers)} Tigers:\n'
		for tiger in tigers:
			animals_status += f'{tiger}\n'
		animals_status += f'----- {len(cheetahs)} Cheetahs:\n'
		for cheetah in cheetahs:
			animals_status += f'{cheetah}\n'
		return animals_status.rstrip('\n')

	def sort_workers_by_type(self):
		keepers = [w for w in self.workers if type(w).__name__ == 'Keeper']
		caretakers = [w for w in self.workers if type(w).__name__ == 'Caretaker']
		vets = [w for w in self.workers if type(w).__name__ == 'Vet']
		return keepers, caretakers, vets

	def workers_status(self):
		keepers, caretakers, vets = self.sort_workers_by_type()
		workers_status = f'You have {len(self.workers)} workers\n' \
			f'----- {len(keepers)} Keepers:\n'
		for keeper in keepers:
			workers_status += f'{keeper}\n'
		workers_status += f'----- {len(caretakers)} Tigers:\n'
		for caretaker in caretakers:
			workers_status += f'{caretaker}\n'
		workers_status += f'----- {len(vets)} Cheetahs:\n'
		for vet in vets:
			workers_status += f'{vet}\n'
		return workers_status.rstrip('\n')
