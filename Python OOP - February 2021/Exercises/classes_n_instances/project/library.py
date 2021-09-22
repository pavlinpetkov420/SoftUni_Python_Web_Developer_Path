from project.user import User


class Library:

    user_records = []
    books_available = {}
    rented_books = {}

    @staticmethod
    def add_user(user: User):
        if user not in Library.user_records:
            Library.user_records.append(user)
        else:
            return f"User with id = {user} already registered in the library!"

    @staticmethod
    def remove_user(user: User):
        if user in Library.user_records:
            Library.rented_books.pop(user)
            Library.user_records.remove(user)
            return

        return f"User with id = {user.user_id} already registered in the library!"

    def change_username(self, user_id: int, new_username: str):
        instance_name = str(el.user_id for el in Library.user_records if el == user_id)
        if not instance_name.username == new_username:
            instance_name.username = new_username
            Library.rented_books
            return f"Username successfully changed to: {new_username} for userid: {user_id}"
