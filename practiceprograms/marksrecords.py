record={}
n=int(input('enter no. of students; '))
i=1
while i<=n:
    name=input('enter the name of the student: ')
    marks=input('enter the marks of te students: ')
    record[name]=marks
    i=i+1

print('name of the student','\t','% of marks')
for i in record:
    print('\t',i,'\t\t\t\t\t',record[i])
