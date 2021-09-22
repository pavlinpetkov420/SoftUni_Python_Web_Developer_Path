class vowels:
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']

    def __init__(self, items):
        self.items = vowels.filter_vowels(items)
        self.index = 0

    @staticmethod
    def filter_vowels(letters):
        items = []
        for _ in letters:
            if _.lower() in vowels.VOWELS:
                items.append(_)

        return items

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.items):
            raise StopIteration

        value = self.items[self.index]
        self.index += 1
        return value


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
