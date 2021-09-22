def check_parameters(*args):
    parameters = list(args)
    are_even = True

    for el in parameters:
        if (not isinstance(el, int)) or (not el % 2 == 0):
            are_even = False
            break

    return are_even


def even_parameters(func):
    def wrapper(*args):

        if check_parameters(*args):
            result = func(*args)
            return result
        return 'Please use only even numbers!'
    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))


