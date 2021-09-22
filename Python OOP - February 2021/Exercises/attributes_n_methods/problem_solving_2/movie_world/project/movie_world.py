from problem_solving_2.movie_world.project.customer import Customer
from problem_solving_2.movie_world.project.dvd import DVD


class MovieWorld:

	def __init__(self, name: str):
		self.name = name
		self.customers = []
		self.dvds = []

	def __repr__(self):
		representation = ''
		for customer in self.customers:
			representation += repr(customer)
		for dvd in self.dvds:
			representation += repr(dvd)

		return representation

	@staticmethod
	def dvd_capacity():
		dvd_capacity = 15
		return dvd_capacity

	@staticmethod
	def customer_capacity():
		customer_capacity = 10
		return customer_capacity

	def find_customer(self, id):
		for customer in self.customers:
			if customer.id == id:
				return customer

	def find_dvd(self, id):
		for dvd in self.dvds:
			if dvd.id == id:
				return dvd

	def add_customer(self, customer: Customer):
		if len(self.customers) < self.customer_capacity():
			self.customers.append(customer)

	def add_dvd(self, dvd: DVD):
		if len(self.dvds) < self.dvd_capacity():
			self.dvds.append(dvd)

	def rent_dvd(self, customer_id: int, dvd_id: int):
		customer = self.find_customer(customer_id)
		dvd = self.find_dvd(dvd_id)

		if dvd in customer.rented_dvds:
			return f"{customer.name} has already rented {dvd.name}"
		elif dvd.is_rented:
			return 'DVD is already rented'
		elif dvd.age_restriction > customer.age:
			return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

		dvd.is_rented = True
		customer.rented_dvds.append(dvd)
		return f"{customer.name} has successfully rented {dvd.name}"

	def return_dvd(self, customer_id, dvd_id):
		customer = self.find_customer(customer_id)
		dvd = self.find_dvd(dvd_id)

		if dvd not in customer.rented_dvds:
			return f"{customer.name} does not have that DVD"

		customer.rented_dvds.remove(dvd)
		dvd.is_rented = False
		return f"{customer.name} has successfully returned {dvd.name}"


