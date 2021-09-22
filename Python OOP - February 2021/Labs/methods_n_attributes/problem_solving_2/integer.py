from math import floor


class Integer:

	def __init__(self, value: int):
		self.value = value

	@classmethod
	def from_float(cls, value):
		if not isinstance(value, float):
			return 'value us not a float'

		int_value = floor(value)
		return Integer(int_value)

	@classmethod
	def from_roman(cls, value):
		number = Integer.convert_roman_to_int(value)

		return Integer(number)

	@staticmethod
	def convert_roman_to_int(value):
		roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
				 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

		index = 0
		number = 0

		while index < len(value):
			if index + 1 < len(value) and value[index: index + 1] in roman:
				number += roman[value[index: index + 2]]
				index += 2
			else:
				number += roman[value[index]]
				index += 1

		return number

	@staticmethod
	def check_for_digits_only(value):
		digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
		try:
			for index in range(value):
				if value[index] in digits:
					continue
			return True
		finally:
			return False

	@classmethod
	def from_string(cls, value):
		if Integer.check_for_digits_only(value):
			return Integer(value)
		return 'wrong type'

	def add(self, integer):
		if isinstance(integer, Integer):
			return self.value + integer.value
		return 'number should be an Integer instance'


first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num.add(second_num))



