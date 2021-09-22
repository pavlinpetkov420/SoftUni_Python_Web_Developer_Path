class Trainer:
    last_id = 0

    def __init__(self, name: str):
        self.name = name
        self.id = Trainer.get_next_id()

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        next_id = Trainer.last_id + 1
        Trainer.last_id = next_id
        return next_id
