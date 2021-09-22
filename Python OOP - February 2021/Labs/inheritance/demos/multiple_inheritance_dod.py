# dod - stands for diamond of dead

class GP:
    def f(self):
        print('GP')


class P1(GP):
    def f(self):
        print('P1')


class P2(GP):
    def f(self):
        print('P2')


class A(P1, P2):
    def f(self):
        print('A')
        super().f()


# user mro() often
print(A.mro())
print(A().f())