from project.library import Library


class User:

    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library: Library):
        is_in_library = True if (author in library.books_available) and (book_name in library.books_available[author]) \
            else False
        if not is_in_library:
            return
        if book_name in library.rented_books:
            return f'The book "{book_name}" is already rented and will be available' \
                        f' in {library.rented_books[book_name]} days!'

        self.books.append(book_name)
        library.rented_books[book_name] = days_to_return
        library.books_available[author].remove(book_name)
        return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, library: Library):
        if book_name in library.rented_books[self.username]:
            library.books_available[author].append(book_name)
            library.rented_books[self.username].remove(book_name)
            return
        return f"{self.username} doesn't have this book in his/her records!"



