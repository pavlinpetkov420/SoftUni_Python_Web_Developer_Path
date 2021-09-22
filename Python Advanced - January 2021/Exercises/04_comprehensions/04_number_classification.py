
numbers = [int(x) for x in input().split(', ')]

print("Positive: ", end="")
print(*[n for n in numbers if n >= 0], sep=', ')
print("Negative: ", end="")
print(*[n for n in numbers if n < 0], sep=', ')
print("Even: ", end="")
print(*[n for n in numbers if n % 2 == 0], sep=', ')
print("Odd: ", end="")
print(*[n for n in numbers if n % 2 != 0], sep=', ')

