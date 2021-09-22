nums = input().split()

numbers_stack = []

for el in nums:
    numbers_stack.append(int(el))

while numbers_stack:
    print(numbers_stack.pop(), end=' ')
