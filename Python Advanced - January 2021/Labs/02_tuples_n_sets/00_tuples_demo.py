"""tuples - like lists but:
 - immutable data collection
 - t = ()
 - little faster than lists -> because are not changeable
 - if we make tuple of lists - inside object list is mutable so elements are mutable"""

# tt = (1, 2, 3)
# print(tt)
#
# print(tt[0], tt[-1])
#
# for x in tt:
#     print(x)
#
# # single element tuple
# tt1 = (1, )
# print(tt1)
#
# tt_empty = ()
# print(tt_empty)
#
#
# def find_min_max(numbers):
#     min_number = min(numbers)
#     max_number = max(numbers)
#
#     return (min_number, max_number)
#
#
# (min_num, max_num) = find_min_max((1, 2, 3, 4, 5, 6, 7, 8))
# print(min_num, max_num)
#
# tt2 = (5, 6, 7, 8)
# tt_res = tt + tt2
# print(tt_res)

# t.count -> how many times is a value in the tuple
# t.index -> on which index is the value in the parameter


def get_indices(values, value):
    index = 0
    indices = []
    while True:
        try:
            new_index = values.index(value, index)
            indices.append(new_index)
            index = new_index + 1
        except ValueError:
            break
    return indices


t_nums = (1, 2, 1, 3, 2, 1)
# print(t_nums.index(1))

# second parameter search the element after the given index
# print(t_nums.index(1, 3))

# if we give invalid element in tuple.index -> value error exception
# print(t_nums.index(19))

# UNPACKING
t3 = (1, 2, 3)
a, b, c = t3
print(a, b, c)
print(*t3)

# *rest -> unpack as list
zero_i, *rest = t3
print(zero_i, rest)
print(type(rest))

print(get_indices(t_nums, 1))

t_of_lists = ([1, 2], [3, 4, 5], [6, 7])

print(t_of_lists)
t_of_lists[-1].append(-12)
print(t_of_lists)

