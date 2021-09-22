"""
Generator - simple way to make iterators
It is a function that returns object(iterator) & values one by one
keyword yield - similar to return(stops the function until its executed again),
used for pause in the function and after new calling of the generator object it continues
execution from the previous state(index) + 1

It is useful when we have huge amount of data, but don't need them at once
"""

# def values_gen(n):
#     index = 0
#     while index < n:
#         yield index
#         index += 1
#
#
# gen = values_gen(5)
# for x in gen:
#     print(x)
#
#
# class values_iter:
#
#     def __init__(self, end):
#         self.end = end
#         self.index = 0
#
#     def __iter__(self):
#         index = 0
#         while index < self.end:
#             yield index
#             index += 1
#
#     def __next__(self):
#         index = self.index
#         self.index += 1
#         return index
#
#
# for x in values_iter(5):
#     print(f'Gen in iter: {x}')
from math import sqrt

"""    Generator Primes!    """


def is_prime(number):
    for x in range(2, int(sqrt(number)) + 1):
        if number % x == 0:
            return False

    return True


def primes_gen(max_num):
    num = 1
    while num < max_num:
        if is_prime(num):
            yield num
        num += 1


primes_1 = primes_gen(100)

print(next(primes_1))
print(next(primes_1))


