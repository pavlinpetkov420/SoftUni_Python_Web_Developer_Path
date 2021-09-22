def compare_n_print_result(*args):
    n_sum, p_sum = args
    print(f"-{n_sum}", p_sum, sep='\n')
    if n_sum > p_sum:
        return "The negatives are stronger than the positives"
    elif n_sum < p_sum:
        return "The positives are stronger than the negatives"


def calculate_sums(*args):
    negatives, positives = args
    n_sum = sum(negatives)
    p_sum = sum(positives)
    return n_sum, p_sum


def separate_negative_n_positives(nums):
    negatives = []
    for el in nums:
        if el < 0:
            negatives.append(el)
    for el in negatives:
        if el in nums:
            nums.remove(el)
    negatives = [abs(el) for el in negatives]
    return negatives, nums


numbers = [int(x) for x in input().split()]
separated_nums = separate_negative_n_positives(numbers)
sums = calculate_sums(*separated_nums)
print(compare_n_print_result(*sums))
