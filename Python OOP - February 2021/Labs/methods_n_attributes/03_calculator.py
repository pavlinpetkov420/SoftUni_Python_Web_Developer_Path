class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        nums = [n for n in args]
        res = nums.pop(0)

        for n in nums:
            res *= n
        return res

    @staticmethod
    def divide(*args):
        nums = [n for n in args]
        res = nums.pop(0)

        for n in nums:
            res /= n
        return res

    @staticmethod
    def subtract(*args):
        nums = [n for n in args]
        res = nums.pop(0)

        for n in nums:
            res -= n
        return res


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
