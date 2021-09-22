"""
Iterators - give us opportunity to iterate over an objects
iterators must implement two methods(iterator protocol):
    - __iter__() - returns us iterator object
    - __next__() - give us the next value in the iterator object
"""


ll = [1, 2, 3, 4, 5]
for x in ll:
    print(x)

print([[x + 1] for x in ll])

"""
low level iteration 
iter()
next()
"""
ll_iter_1 = iter(ll)
ll_iter_2 = iter(ll)

# print(ll_iter_1)
#
# print(f'Iter1: {next(ll_iter_1)}')
# print(f'Iter1: {next(ll_iter_1)}')
# print(f'Iter1: {next(ll_iter_1)}')
# print(f'Iter1: {next(ll_iter_1)}')
# print(f'Iter1: {next(ll_iter_1)}')
# print(f'Iter2: {next(ll_iter_2)}')
#
# # when there isn't other things to iterate we receive StopIteration Exception
# # print(next(ll_iter))
#
# print(f'Iter2: {next(ll_iter_2)}')
# print(f'Iter2: {next(ll_iter_2)}')
# print(f'Iter2: {next(ll_iter_2)}')
# print(f'Iter2: {next(ll_iter_2)}')
# print(f'Iter2: {next(ll_iter_2)}')
# print(f'Iter2: {next(ll_iter_2)}')


# low-level iterator
while True:
    try:
        print(next(ll_iter_1))
    except StopIteration:
        print()
        break


"""
CUSTOM RANGE ITERATOR
"""


class custom_range:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = start

    def __iter__(self):
        return self.iterator(self)

    def __reversed__(self):
        return self.reversed_iterator(self)

    class iterator:
        """
        This class is made because with him
        we can use 1 custom_range object on 2 or more iterators
        """

        def __init__(self, custom_range_obj):
            self.custom_range_obj = custom_range_obj
            self.value = self.custom_range_obj.start

        def __iter__(self):
            return self

        def __next__(self):
            if self.value > self.custom_range_obj.end:
                raise StopIteration
            value = self.value
            self.value += 1
            return value

    class reversed_iterator:
        """
        Class for reversed iteration over iter_objects
        """

        def __init__(self, custom_range_obj):
            self.custom_range_obj = custom_range_obj
            self.value = self.custom_range_obj.end

        def __iter__(self):
            return self

        def __reversed__(self):
            return self

        def __next__(self):
            if self.value < self.custom_range_obj.start:
                raise StopIteration
            value = self.value
            self.value -= 1
            return value


cr = custom_range(1, 10)

for x in cr:
    print(f'Iter1: {x}')

for x in cr:
    print(f'Iter2: {x}')

for x in reversed(cr):
    print(f'Reversed Iter: {x}')






class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


# class Person its not iterable
# for x in Person('ConCho', 14):
#     print(x)
