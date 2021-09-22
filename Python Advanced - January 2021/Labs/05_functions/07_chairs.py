from itertools import combinations


def calculate_combinations(names, n, combs=[]):
    if len(combs) == n:
        print(", ".join(combs))
        return

    for i in range(len(names)):
        name = names[i]
        combs.append(name)
        calculate_combinations(names[i+1:], n, combs)
        combs.pop()


names = input().split(', ')
n = int(input())
calculate_combinations(names, n)

print(*combinations(names, n))
