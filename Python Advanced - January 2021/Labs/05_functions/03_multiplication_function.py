from functools import reduce


def multiply_2(*args):
    return reduce(lambda g, r: g * r, args)


def multiply(*args):
    prod = 1

    for el in args:
        prod *= el

    return prod


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
