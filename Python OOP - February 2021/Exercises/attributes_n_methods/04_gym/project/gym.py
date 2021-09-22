from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.subscription import Subscription
from project.exercise_plan import ExercisePlan


class Gym:

    def __init__(self):
        """
        no parameters upon initialization
        attributes in this class are references to all objects
        in other classes
        """

        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def get_needed_ids(subs_instance):
        customer_id = subs_instance.customer_id
        trainer_id = subs_instance.trainer_id
        exercise_id = subs_instance.exercise_id
        return customer_id, trainer_id, exercise_id

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def find_instances(self, ids):
        c_id, t_id, e_id = ids
        instances = []
        for _ in range(1):
            instances.append([c for c in self.customers if c.id == c_id][0])
            instances.append([t for t in self.trainers if t.id == t_id][0])
            instances.append([e for e in self.equipment if e.id == e_id][0])
            instances.append([p for p in self.plans if (p.trainer_id == t_id) and (p.equipment_id == e_id)][0])

        return instances

    def get_subs_instance(self, s_id):
        return [s for s in self.subscriptions if s.id == s_id][0]

    def subscription_info(self, subscription_id: int):
        info = ""
        instances = []
        subs_instance = self.get_subs_instance(subscription_id)
        instances.append(subs_instance)
        ids = self.get_needed_ids(subs_instance)
        instances += self.find_instances(ids)

        for el in instances:
            info += f"{repr(el)}\n"
        print(info)

        return info
