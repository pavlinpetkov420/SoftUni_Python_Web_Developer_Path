
class User:

	def __init__(self, user_id: int, username: str):
		self.user_id = user_id
		self.username = username
		self.books = []

	def get_book(self, author: str, book_name: str, days_to_return: int, library):
		if book_name not in library.books_available[author] and\
				book_name not in library.rented_books[self.username].keys():
			return

		if self.username in library.rented_books.keys():
			if book_name in library.rented_books[self.username].keys():
				return f'The book "{book_name}\" is already rented and will be' \
					f' available in {library.rented_books[self.username][book_name]} days!'

		self.books.append(book_name)
		library.books_available[author].remove(book_name)

		if self.username not in library.rented_books.keys():
			library.rented_books[self.username] = {book_name: days_to_return}
		else:
			library.rented_books[self.username] += {book_name: days_to_return}

	def return_book(self, author: str, book_name: str, library):
		if book_name in self.books:
			self.books.remove(book_name)
			del library.rented_books[self.username][book_name]
			library.books_available[author].append(book_name)

		return f"{self.username} doesn't have this book in his/her records!"

	def info(self):
		return ', '.join(self.books.sort())

	def __str__(self):
		return f'{self.user_id}, {self.username}, {self.books}'

