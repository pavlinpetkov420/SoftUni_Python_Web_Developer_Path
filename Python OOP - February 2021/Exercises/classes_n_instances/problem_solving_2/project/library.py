
class Library:

	def __init__(self):
		self.user_records = []
		self.books_available = {}
		self.rented_books = {}

	def add_user(self, user):
		if user not in self.user_records:
			return self.user_records.append(user)
		return f"User with id = {user.user_id} already registered in the library!"

	def remove_user(self, user):
		if user.user_id not in self.user_records:
			return "We could not find such user to remove!"
		self.user_records.remove(user)
		self.rented_books.pop(user.user_id)

	def find_user_through_id(self, user_id):
		for user in self.user_records:
			if user.user_id == user_id:
				return user

	def change_username(self, user_id: int, new_username: str):
		user = self.find_user_through_id(user_id)

		if not user:
			return f'There is no user with id = {user_id}!'

		if user.username == new_username:
			return "Please check again the provided username - it should" \
				" be different than the username used so far!"

		for user_record in self.user_records:
			if user.username == user_record.username:
				user_record.username = new_username
				if user.username in self.rented_books.keys():
					self.rented_books[new_username] = self.rented_books.pop(user.username)
				user.username = new_username
				return f"Username successfully changed to: {new_username} for userid: {user.user_id}"
