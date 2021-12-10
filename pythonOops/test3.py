class T1:
    a = 10

    def __init__(self):
        self.b = 20

    def m1(self):
        print('hi')

    def m2(self):
        self.m1()
        print('hello')


t = T1()
t.m1()

t.m2()
x = T1()
# print()


print(t.a, t.b)
print(x.a, x.b)
t.a = 888
t.b = 999
print('_--------')
print(t.a, t.b)
print(x.a, x.b)