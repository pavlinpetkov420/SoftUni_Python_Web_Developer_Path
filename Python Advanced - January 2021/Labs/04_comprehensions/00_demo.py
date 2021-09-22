# COMPREHENSIONS

# - short way to construct a new sequence

# 4 types:
# - list comprehensions
# - dictionary comprehensions
# - set comprehensions
# - generator comprehensions

# BENEFITS:
# - less memory, shorten syntax, easier data manipulations, better performance
# - makes the code more expressive


def to_binary(number):
    bits = []
    while number:
        bits.append(number % 2)
        number //= 2
    return ''.join(map(str, bits[::-1]))


ll = [1, 2, 3, 4, 5, 6, 7, 14, 15]

print(
    [x for x in ll]
)

# gives us values of list +1
print(
    [x + 1 for x in ll]
)

# returns all even value with +1
print(
    [x + 1 for x in ll if x % 2 == 0]
)


print(
    [to_binary(x) for x in ll]
)

print(
    [x * x for x in ll]
)

# dictionary comprehension

print(
    {x: to_binary(x) for x in ll}
)

# NESTED COMPREHENSION

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3],
]

flat = [x for row in matrix for x in row]
print(matrix)
print(flat)

