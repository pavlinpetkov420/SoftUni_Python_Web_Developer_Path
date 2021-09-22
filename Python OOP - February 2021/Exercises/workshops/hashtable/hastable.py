# Linear approach implementation of hashing

class HashTable:

    """
    Hashable represent a custom dictionary implementation
    where we use two private lists to achieve storing and hashing of
    key-value pairs functionality
    """

    def __init__(self):
        self.max_capacity = 4
        self.__keys = [None] * self.max_capacity
        self.__values = [None] * self.max_capacity

    def __getitem__(self, key):
        index = self.__keys.index(key)
        return self.__values[index]

    def __setitem__(self, key, value):
        if key in self.__keys:
            index = self.__keys.index(key)
            self.__values[index] = value
            return

        if self.actual_lenght == self.max_capacity:
            self.__resize()

        index = self.hash(key)

        if self.__keys[index] is None:
            self.__keys[index] = key
            self.__values[index] = value

    def __len__(self):
        return self.max_capacity

    def __repr__(self):
        result = [f"{self.__keys[index]}: {self.__values[index]}"
                  for index in range(len(self.__keys))
                  if self.__keys[index] is not None]
        return "{" + "{}".format(', '.join(result)) + "}"

    @property
    def actual_lenght(self):
        return len([el for el in self.__keys if el is not None])

    @property
    def keys(self):
        return self.__keys

    @property
    def values(self):
        return self.__values

    def __check_available_index(self, index):
        """
        Checks if there is empty slot on this index,
        if not implements linear approach when there is a collision
        between two hash indexes and returns the next available index
        :param index: int
        :return: int -> next/current available index
        """
        if index == len(self.__keys):
            return self.__check_available_index(0)
        if self.__keys[index] is None:
            return index
        return self.__check_available_index(index + 1)

    def hash(self, key):
        index = sum([ord(ch) for ch in key]) % self.max_capacity
        available_index = self.__check_available_index(index)
        return available_index

    def add(self, key: str, value):
        self[key] = value

    def get(self, key, default=None):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            return default

    def __resize(self):
        self.__keys = self.__keys + [None] * self.max_capacity
        self.__values = self.__values + [None] * self.max_capacity
        self.max_capacity *= 2


table = HashTable()
#
# table["name"] = "Peter"
# table["age"] = 25
# table["age"] = 24
# table['work'] = 'Community volunteer'
# table['eyes color'] = 'pink'
# table['hair color'] = 'grey'
# table['car'] = 'Tesla Model S'
# table['car color'] = 'DarkMatter'
table['favourite food'] = 'Duner Box from City Food <3'
# table['goat milk'] = 'Not great, not terrible'
# table.add('tattoos', False)
#
#
print(table)
# print(table['name'])
# print(table.get("name", 'Not in dict'))
# print(table["age"])
# print(len(table))
#
# print(table.actual_lenght)

