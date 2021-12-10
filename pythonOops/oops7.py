class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def getinfo(self):
        print("Car Name:{} , Model:{} and Color:{}".format(self.name, self.model, self.color))


class Employee:
    def __init__(self, ename, eno, car):
        self.ename = ename
        self.eno = eno
        self.d = Car('i', '2', 'g')
        print(type(self.d))
        self.car = car
        print(type(self.car))

    def empinfo(self):
        print("Employee Name:", self.ename)
        print("Employee Number:", self.eno)
        print("Employee Car Info:")
        print(self.d.color)
        print(type(self.d.color))
        # self.car.getinfo()
        print(type(self.car.getinfo()))


c = Car("Innova", "2.5V", "Grey")
print(type(c))
e = Employee('Durga', 10000, c)

e.empinfo()