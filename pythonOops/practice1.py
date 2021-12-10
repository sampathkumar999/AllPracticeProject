
class Student:

    def __init__(self, name, rollNo, branch ):
        self.name = name
        self.rollNo = rollNo
        self.branch = branch


    def show_students(self):
        print('the name of the student is:',self.name)
        print('the roll number of the student is:',self.rollNo)
        print('the student belongs to the branch:', self.branch)


s1 = Student('Sampath', 121, 'ECE')
s1.show_students()
print( s1.name, s1.branch, s1.rollNo)