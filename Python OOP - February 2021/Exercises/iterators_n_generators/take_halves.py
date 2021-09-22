def solution():
    def integers():

        number = 1
        while True:
            yield number
            number += 1

    def halves():

        for i in integers():
            yield i / 2

    def take(n, seq):
        nums = []
        for i in seq:
            nums.append(i)
            if len(nums) == n:
                return nums

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

# TODO understand the algorithm
