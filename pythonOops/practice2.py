class Employee:

    def __init__(self, name, age, designation, package):
        self.name = name
        self.age = age
        self.designation = designation
        self.package = package
        print('Iam the constructor of the class')


    def show_details(self):
        print('The name of the employee is: ', self.name)
        print('The age of the employee is: ', self.age)
        print('The designation of the employee is: ', self.designation)
        print('The package of the employee is: ', self.package)



E1 = Employee('sampath', 33, 'sweeper', 30000)
E1.show_details()
