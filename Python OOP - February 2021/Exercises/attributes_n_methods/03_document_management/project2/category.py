class Category:
    """
    class Category with 2 attribute upon initialization - id, name
    2 methods:
        edit - change the name of the category
        repr - return string repr in following format: "Category {id}: {name}"
    """

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Category {self.id}: {self.name}"

    def kill(self):
        del self

    def edit(self, new_name: str):
        self.name = new_name
