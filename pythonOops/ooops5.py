class P:
    a = 10

    def __init__(self):
        self.b = 100

    def m1(self):
        print('Parent instance method')

    @classmethod
    def m2(cls):
        print('Parent class method')

    @staticmethod
    def m3():
        print('Parent static method')


class C(P):
    a = 60

    def __init__(self):
        super().__init__()
        self.d = 30
        print(P.a)

    @staticmethod
    def m3():
        print('Child static method')


c = C()
print(c.a)
print(c.d)
print(c.b)
c.m1()
c.m2()
c.m3()