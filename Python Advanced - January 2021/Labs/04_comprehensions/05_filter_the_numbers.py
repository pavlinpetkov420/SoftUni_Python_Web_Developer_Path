def create_range_list():
    (start, end) = (int(input()) for _ in range(2))
    return [x for x in range(start, end + 1)]


def is_valid(x):
    return any(x % i == 0 for i in range(2, 11))


range_numbers = create_range_list()
result = [x for x in range_numbers if is_valid(x)]
print(result)
