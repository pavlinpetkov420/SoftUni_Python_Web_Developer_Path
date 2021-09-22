class Customer:

	id = 0

	def __init__(self, name: str, address: str, email: str):
		self.id = Customer.get_next_id()
		self.name = name
		self.address = address
		self.email = email

	@staticmethod
	def get_next_id():
		id = Customer.id + 1
		Customer.id = id
		return id

	def __repr__(self):
		return f'Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}'

