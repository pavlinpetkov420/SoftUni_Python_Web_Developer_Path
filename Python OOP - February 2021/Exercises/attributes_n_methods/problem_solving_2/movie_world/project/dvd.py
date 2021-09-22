class DVD:

	def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
		self.name = name
		self.id = id
		self.creation_year = creation_year
		self.creation_month = creation_month
		self.age_restriction = age_restriction
		self.is_rented = False

	def __repr__(self):
		return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction " \
			f"{self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}\n"

	@staticmethod
	def convert_int_to_str_month(month):
		months = {
			'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July',
			'08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'
		}

		return months[month]

	@classmethod
	def from_date(cls, id: int, name: str, date: str, age_restriction: int):
		month, year = date.split('.')[1:]
		month_str = DVD.convert_int_to_str_month(month)
		return DVD(name, id, year, month_str, age_restriction)
