class Test:
    a = 10

    def __init__(self):
        self.g = 70
        Test.b = 20

    def m1(self):
        Test.c = 30

    @classmethod
    def m2(cls):
        cls.d = 40
        Test.e = 50

    @staticmethod
    def m3():
        Test.f = 60


t = Test()

print()
t.m1()
Test.b = 999
t.m2()
print(t.__dict__)
print(Test.__dict__)

# print(t.f)
'''
#t=Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)
t.m2()
print(Test.__dict__)
Test.m2()
print('ref',Test.__dict__)
print(Test.__dict__)'''