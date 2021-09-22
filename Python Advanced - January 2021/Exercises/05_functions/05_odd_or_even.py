def calculate_odds_formula(nums):
    odds = [el for el in nums if el % 2 != 0]
    result = sum(odds) * len(nums)
    return result


def calculate_evens_formula(nums):
    evens = [el for el in nums if el % 2 == 0]
    result = sum(evens) * len(nums)
    return result


def process_cmd_n_print_result(*args):
    ODD_CMD = 'Odd'
    EVEN_CMD = 'Even'
    command, nums = args
    if command == ODD_CMD:
        print(calculate_odds_formula(nums))
    elif command == EVEN_CMD:
        print(calculate_evens_formula(nums))


cmd = input()
numbers = [int(el) for el in input().split()]
process_cmd_n_print_result(cmd, numbers)
