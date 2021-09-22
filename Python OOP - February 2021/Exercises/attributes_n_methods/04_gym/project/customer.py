class Customer:
    last_id = 0

    def __init__(self, name: str, address: str, email: str):
        """
        upon initialization are needed 3 arguments
        :param name:
        :param address:
        :param email:
        and auto incremented id parameter
        """

        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.get_next_id()

    def __repr__(self):
        """return string representation of the object"""
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @staticmethod
    def get_next_id():
        next_id = Customer.last_id + 1
        Customer.last_id = next_id
        return Customer.last_id
