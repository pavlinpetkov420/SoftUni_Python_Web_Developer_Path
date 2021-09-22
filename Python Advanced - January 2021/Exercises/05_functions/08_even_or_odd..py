def even_odd(*args):
    numbers, command = args[0: len(args) - 1], args[-1]
    EVEN_CASE = 'even'
    ODD_CASE = 'odd'
    if command == EVEN_CASE:
        return list(filter(lambda x: x % 2 == 0, numbers))
    elif command == ODD_CASE:
        return list(filter(lambda x: x % 2 != 0, numbers))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))