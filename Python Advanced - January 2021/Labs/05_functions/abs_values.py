# comprehension solution
def convert_iterable_to_absolute(nums_list):
    return [abs(el) for el in nums_list]


# map solution
def take_absolute_values2(nums2_list):
    result = list(map(lambda x: abs(x), nums2_list))
    return result


numbers = [float(el) for el in input().split()]
absolute_values = convert_iterable_to_absolute(numbers)
print(absolute_values)

numbers2 = list(map(float, input().split()))
abs_values2 = take_absolute_values2(numbers2)
print(abs_values2)
