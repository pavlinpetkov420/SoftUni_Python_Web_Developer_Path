class countdown_iterator:

    def __init__(self, count):
        self.count = count
        self.value = self.count

    def __iter__(self):
        return self

    def __next__(self):
        if self.value < 0:
            raise StopIteration

        value = self.value
        self.value -= 1
        return value


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
