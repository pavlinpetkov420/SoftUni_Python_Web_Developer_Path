def input_lines():
    tokens = input().split()
    count1, count2 = int(tokens[0]), int(tokens[1])
    lines1 = []
    for _ in range(count1):
        lines1.append(int(input()))

    lines2 = []
    for _ in range(count2):
        lines2.append(int(input()))

    return lines1, lines2


def print_numbers(unique_nums):
    for number in unique_nums:
        print(number)


def find_equal_elements(nums1, nums2):
    unique_nums = set()
    for el in nums1:
        if el in nums2:
            unique_nums.add(el)

    print_numbers(unique_nums)


nums1, nums2 = input_lines()

find_equal_elements(nums1, nums2)
