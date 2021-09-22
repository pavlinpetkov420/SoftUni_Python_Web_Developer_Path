class RhombusOfStars:

	def __init__(self, number: int):
		self.number = number

	def create_rhombus(self):
		for r in range(self.number):
			print(' ' * (self.number-r-1) + '* ' * (r+1))
		for p in range(self.number - 1, 0, -1):
			print(' ' * (self.number - p) + '* ' * p)


number = int(input('Insert rhombus size: '))

r = RhombusOfStars(number)
r.create_rhombus()