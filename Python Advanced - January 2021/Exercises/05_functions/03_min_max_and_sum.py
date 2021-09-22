def return_sum_of_numbers(nums):
    return sum(nums)


def return_max_number(nums):
    return max(nums)


def return_min_number(nums):
    return min(nums)


numbers = [int(el) for el in input().split()]
print(f"The minimum number is {return_min_number(numbers)}")
print(f"The maximum number is {return_max_number(numbers)}")
print(f"The sum number is {return_sum_of_numbers(numbers)}")
