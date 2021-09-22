from math import sqrt


def is_prime(number):
    for x in range(2, int(sqrt(number)) + 1):
        if number % x == 0:
            return False

    return True


ll = [x for x in range(5)]

print(ll)

gg = (x for x in range(50) if is_prime(x))
print(gg)


