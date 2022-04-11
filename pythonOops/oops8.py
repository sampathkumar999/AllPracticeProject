class c1:

    A = 10

    def __init__(self, a, b,e,f):
        self.a = a
        self.b = b
        self.e = e
        self.f = f

    def m1(self):
        print('I am the first method')
        print('The first instance variable is:', self.a)

    def m2(self):
        print('I am the second method')
        print('The second instance variable is:', self.b)

    def m3(self):
        print('I am the third method')
        print('The only class variable in this class is:', c1.A)

    @classmethod
    def m4(cls, A, e, f):
        print(e, A, f)

    @staticmethod
    def m6():
        print()

class c2(c1):

    def __init__(self, c, d):
        super().__init__(1,2,3,4)
        self.c = c
        self.d = d


    B = 20

    def m5(self):
        print('Iam the only method in the class')
        print('The instance variables in this class are:', self.c, self.d)
        print('The only class variable in this class is:', c2.B)
        print(self.e, self.f)

c = c2(1,2)
c.m4(6,7,8)
c.m1()
c.m2()
c.m5()

