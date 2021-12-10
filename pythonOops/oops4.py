class Test:
    __a = 10

    def __m1(self):
        print(self.__a)
        print(Test.__a)
        return Test.__a, self.__a


t = Test()
# t.m1()
print(t._Test__m1())