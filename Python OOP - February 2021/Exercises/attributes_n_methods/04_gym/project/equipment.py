class Equipment:
    last_id = 0

    def __init__(self, name: str):
        """
        class equipment needs name upon initialization
        :param name:
        and auto incremented id methods
        """
        self.name = name
        self.id = Equipment.get_next_id()

    def __repr__(self):
        """
        string representation of the object
        :return: "Equipment <{id}> {name}"
        """
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        """
        auto increment an current_id and set current_id upon initialization
        :return: int
        """
        next_id = Equipment.last_id + 1
        Equipment.last_id = next_id
        return next_id
