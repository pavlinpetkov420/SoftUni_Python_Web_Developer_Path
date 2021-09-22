def extract_even_nums(nums):
    return list(filter(lambda x: x % 2 == 0, nums))


numbers = [int(el) for el in input().split(' ')]
print(extract_even_nums(numbers))
