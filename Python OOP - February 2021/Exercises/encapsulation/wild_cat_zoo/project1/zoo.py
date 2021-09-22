from project1.caretaker import Caretaker
from project1.keeper import Keeper
from project1.vet import Vet
from project1.cheetah import Cheetah
from project1.tiger import Tiger
from project1.lion import Lion


class Zoo:

    __hired_workers = 0
    __added_animals = 0

    def __init__(self, name: str, budget: float, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    @staticmethod
    def update_current_capacity_counters(update_type: str, is_fired=None):
        if update_type == 'animal':
            Zoo.__added_animals += 1
        elif update_type == 'worker':
            Zoo.__hired_workers += 1
        elif update_type == 'worker' and is_fired:
            Zoo.__hired_workers -= 1

    def sum_money_for_animals(self):
        money_for_animals = 0
        for a in self.animals:
            money_for_animals += a.get_needs()
        return money_for_animals

    def sum_salaries(self):
        salaries = 0
        for w in self.workers:
            salaries += w.salary
        return salaries

    def check_budget(self, needed_money: float):
        return needed_money <= self.__budget

    def check_animal_space(self):
        return Zoo.__added_animals < self.__animal_capacity

    def check_workers_space(self):
        return Zoo.__hired_workers < self.__workers_capacity

    def check_for_worker(self, worker_name):
        if self.workers:
            filtered_workers = [w for w in self.workers if w.name == worker_name][0]
            if filtered_workers:
                return filtered_workers

    def add_animal(self, animal: Lion or Tiger or Cheetah, price: float):
        is_capacity = self.check_animal_space()
        is_budget = self.check_budget(price)
        if is_budget and is_capacity:
            self.animals.append(animal)
            self.__budget -= price
            Zoo.update_current_capacity_counters('animal')
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif is_capacity and not is_budget:
            return 'Not enough budget'
        elif not is_capacity:
            return 'Not enough space for animal'

    def hire_worker(self, worker: Keeper or Caretaker or Vet):
        if self.check_workers_space():
            self.workers.append(worker)
            Zoo.update_current_capacity_counters('worker')
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return 'Not enough space for worker'

    def fire_worker(self, worker_name):
        worker_instance = self.check_for_worker(worker_name)
        if worker_instance:
            self.workers.remove(worker_instance)
            Zoo.update_current_capacity_counters('worker', True)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = self.sum_salaries()
        if self.check_budget(salaries):
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_for_animals = self.sum_money_for_animals()
        if self.check_budget(money_for_animals):
            self.__budget -= money_for_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):

        lions = [l for l in self.animals if l.__class__.__name__ == 'Lion']
        tigers = [t for t in self.animals if t.__class__.__name__ == 'Tiger']
        cheetahs = [c for c in self.animals if c.__class__.__name__ == 'Cheetah']

        result = f'You have {len(self.animals)} animals\n' \
                 f'----- {len(lions)} Lions:\n'
        result += '{}'.format('\n'.join([repr(l) for l in lions])) + '\n'
        result += f'----- {len(tigers)} Tigers:\n'
        result += '{}'.format('\n'.join([repr(t) for t in tigers])) + '\n'
        result += f'----- {len(cheetahs)} Cheetahs:\n'
        result += '{}'.format('\n'.join([repr(c) for c in cheetahs]))

        return result

    def workers_status(self):

        keeper = [k for k in self.workers if k.__class__.__name__ == 'Keeper']
        caretaker = [t for t in self.workers if t.__class__.__name__ == 'Caretaker']
        vet = [c for c in self.workers if c.__class__.__name__ == 'Vet']

        result = f'You have {len(self.workers)} workers\n' \
                 f'----- {len(keeper)} Keepers:\n'
        result += '{}'.format('\n'.join([repr(k) for k in keeper])) + '\n'
        result += f'----- {len(caretaker)} Caretakers:\n'
        result += '{}'.format('\n'.join([repr(c) for c in caretaker])) + '\n'
        result += f'----- {len(vet)} Vets:\n'
        result += '{}'.format('\n'.join([repr(v) for v in vet]))

        return result
