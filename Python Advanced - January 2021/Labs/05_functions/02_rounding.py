def round_numbers(nums_list):
    result = [round(el) for el in nums_list]
    print(result)


nums = list(map(lambda x: float(x), input().split()))
round_numbers(nums)