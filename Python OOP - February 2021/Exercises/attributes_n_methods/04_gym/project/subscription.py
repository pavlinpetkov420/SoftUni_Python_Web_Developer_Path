class Subscription:
    last_id = 0

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        """
        creates an object which need 4 attributes upon initialization
        :param date:
        :param customer_id:
        :param trainer_id:
        :param exercise_id:
        """
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = Subscription.get_next_id()

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"

    @staticmethod
    def get_next_id():
        next_id = Subscription.last_id + 1
        Subscription.last_id = next_id
        return next_id
