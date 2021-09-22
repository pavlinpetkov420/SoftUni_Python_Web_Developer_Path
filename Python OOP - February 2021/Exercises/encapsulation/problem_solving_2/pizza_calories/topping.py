class Topping:

	def __init__(self, topping_type: str, weight: float):
		self.topping_type = topping_type
		self.weight = weight

	@property
	def topping_type(self):
		return self.__topping_type

	@topping_type.setter
	def topping_type(self, value):
		if isinstance(value, str):
			self.__topping_type = value

	@property
	def weight(self):
		return self.__weight

	@weight.setter
	def weight(self, value):
		if isinstance(value, float):
			self.__weight = value
