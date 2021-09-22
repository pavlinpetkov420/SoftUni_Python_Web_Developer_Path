"""
Everything must be open for extensions and closed for modifications!!!
Abstraction and Mixins are recommend for open/closed!!!
"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:

    def __init__(self, books):
        self.books = books

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, book):
        if book in self.books:
            return book


a = Book('a', 'A')

"""Example for monkey patching - NOT RECOMMENDED!!!
Monkey-patching is used for testing sometimes"""
Library.add_book = lambda self, book: self.books.append(book)
