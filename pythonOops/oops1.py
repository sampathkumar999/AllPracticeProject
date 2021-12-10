class Employee:
    def __init__(self, name, num, sal):
        self.name = name
        self.age = num
        self.sal = sal

    def myinfo(self):
        print('Name is:', self.name)
        print('Age is:', self.age)
        print('Salary is:', self.sal)


class Test:
    def info2(emp):
        emp.sal = emp.sal + 10000
        emp.myinfo()


e = Employee('sampath', 27, 15000)
print(e.__init__)
Test.info2(e)