from problem_solving_2.gym.project.customer import Customer
from problem_solving_2.gym.project.equipment import Equipment
from problem_solving_2.gym.project.exercise_plan import ExercisePlan
from problem_solving_2.gym.project.gym import Gym
from problem_solving_2.gym.project.subscription import Subscription
from problem_solving_2.gym.project.trainer import Trainer

customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))
