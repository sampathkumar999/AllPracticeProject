class Student:
    age = 60

    def __init__(self):
        self.name = 'sampath'
        print(self.name)



    def talk(self):
        self.age=25
        return self.age


a = Student()
Student.mro()
Student.age
print(a)
print(a.name)
#print(a.__init__())
print(Student().age)
print(Student().talk())

