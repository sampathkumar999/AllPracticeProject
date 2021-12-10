class Test:
    def __init__(self):
        self.name = 'sampath'
        self.age = 25

    def m1(self):
        self.no = 2000
        return print(self.no)


t = Test()
print(t.__dict__)
t.m1()
print(t.__dict__)