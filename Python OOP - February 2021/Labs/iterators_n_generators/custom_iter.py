class custom_range:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.index = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.end:
            raise StopIteration
        value = self.index
        self.index += 1
        return value


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)

values = [1, 2, 3, 4, 5, 6, 7]

range_values = custom_range(0, len(values) - 1)
for i in range_values:
    print(f'Value {values[i]}')
