class ValueCannotBeNegative(Exception):
    def __init__(self, value):
        super().__init__(f"{value} is negative")


for i in range(5):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative(number)
