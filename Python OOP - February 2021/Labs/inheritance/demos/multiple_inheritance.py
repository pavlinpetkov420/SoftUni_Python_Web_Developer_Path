class A:
    def __init__(self, value):
        self.value_a = value

    def func_a(self):
        print(f'I am from A: {self.value_a}')


class B:
    def __init__(self, value):
        self.value_b = value

    def func_b(self):
        print(f'I am from B: {self.value_b}')


class C(A, B):
    # inheritance order matters
    def __init__(self, a_value, b_value):
        A.__init__(self, a_value)
        B.__init__(self, b_value)


c = C('C', 'C0')
c.func_a()
c.func_b()

# mro - method resolution order

print(C.mro())

