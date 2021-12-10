class A:
    a = 10

    def __init__(self):
        self.b = 20

    def m1(self):
        print('sum', A.a + self.b)
        c = 30
        print('suml', A.a + c)
        print('sumi:', self.b + c)

    @classmethod
    def m2(cls):
        print('Class level method')

    @staticmethod
    def m3():
        print('Static method')


x = A()
x.m1()
x.m2()
x.m3()
A.m2()
A.m3()
