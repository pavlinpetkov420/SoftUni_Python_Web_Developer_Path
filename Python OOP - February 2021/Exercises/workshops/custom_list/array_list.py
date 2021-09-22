class ArrayList:

    initial_capacity = 4

    def __init__(self):
        self.capacity = self.initial_capacity
        self.values_count = 0
        self.values = [None] * self.capacity

    def append(self, value):
        self.__grow()
        self.values[self.values_count] = value
        self.values_count += 1
        return self

    def remove(self, index):
        self.__validate_index(index)

        value_to_return = self.values[index]
        self.values_count -= 1
        for i in range(index, min(self.values_count, self.capacity)):
            self.values[i] = self.values[i + 1]

        return value_to_return

    def get(self, index):
        self.__validate_index(index)

        return self.values[index]

    def extend(self, iterable):
        self.__validate_iterable(iterable)
        for x in iterable:
            self.append(x)

    def insert(self, index, value):
        self.__validate_index(index)
        self.__grow()

        for i in range(self.size() - 1, index - 1, -1):
            self.values[i + 1] = self.values[i]

        self.values[index] = value
        self.values_count += 1

    def pop(self):
        self.__validate_index(0)
        value_to_return = self.values[self.values_count - 1]
        self.values_count -= 1
        return value_to_return

    def clear(self):
        self.values_count = 0

    def index(self, value):
        for i in range(self.values_count):
            if self.values[i] == value:
                return i

        raise ValueError

    def count(self, value):
        count = 0
        for i in range(self.values_count):
            if self.values[i] == value:
                count += 1
        return count

    def reverse(self):
        return list(reversed(self))

    def copy(self):
        copied_list = ArrayList()
        [copied_list.append(x) for x in self]
        return copied_list

    def size(self):
        return self.values_count

    def add_first(self, value):
        pass

    def dictionize(self):
        pass

    def move(self, amount):
        pass

    def sum(self):
        pass

    def overbound(self):
        pass

    def underbound(self):
        pass

    def __grow(self):
        if self.values_count < self.capacity:
            return
        self.values += [None] * self.capacity
        self.capacity *= 2

    @staticmethod
    def __validate_iterable(iterable):
        if not getattr(iterable, '__iter__', False):
            raise ValueError

    def __validate_index(self, index):
        if self.values_count <= index:
            raise IndexError

    def __iter__(self):
        for i in range(self.values_count):
            yield self.values[i]

    def __reversed__(self):
        for i in range(self.values_count - 1, -1, -1):
            yield self.values[i]

