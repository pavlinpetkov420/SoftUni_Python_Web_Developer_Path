from validators import TypeValidator


class Utills:
    def __init__(self):
        self.validator = TypeValidator()

    def my_sum(self, numbers):
        type_validator = TypeValidator()
        [self.validator.validate_type(x, [int, float]) for x in numbers]
        return sum(numbers)
