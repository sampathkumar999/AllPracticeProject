n=int(input('enter no. of students:'))
d={}
for i in range(n):
    name=input('enter name:')
    marks=input('enter marks:')
    d[name]=marks
print(d)
while True:
    name=input('enter student name to get marks:')
    marks=d.get(name,-1)
    if marks ==-1:
        print('student not found.')
    else:
        print('the marks of',name,'are:',marks)
    option=input('do u want to check one more?[yes/no]')
    if option=='no':
        break
print('thanks for using app!')
            
