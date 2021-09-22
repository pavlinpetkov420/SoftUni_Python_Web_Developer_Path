class ExercisePlan:
    last_id = 0

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        """
        3 attributes upon initialization
        :param trainer_id: int -> id from Trainer object
        :param equipment_id: int -> id from Equipment object
        :param duration: int in minutes
        and auto increment id
        """
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.get_next_id()

    def __repr__(self):
        """
        :return: string repr -> "Plan <{id}> with duration {duration} minutes"
        """
        return f"Plan <{self.id}> with duration {self.duration} minutes"

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        """
        create new object of this class
        :param trainer_id:
        :param equipment_id:
        :param hours:
        :return:
        """
        minutes_training = hours * 60
        return cls(trainer_id, equipment_id, minutes_training)

    @staticmethod
    def get_next_id():
        """
        auto increment id of an object
        :return: int
        """
        next_id = ExercisePlan.last_id + 1
        ExercisePlan.last_id = next_id
        return next_id
