import sys


class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.numbers = self.generate_numbers()
        self.index = 0

    def generate_numbers(self):
        nums = []
        for num in range(0, sys.maxsize, self.step):
            if len(nums) == self.count:
                return nums
            nums.append(num)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.numbers):
            raise StopIteration

        value = self.numbers[self.index]
        self.index += 1
        return value


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
