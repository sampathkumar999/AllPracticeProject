from array import *
a=array('i',[])
n=int(input('enter the length of the array'))
for i in range(n):
    x=int(input('enter the array element'))
    a.append(x)
print('the array you entered is',a)

print('the sum of the elements in the array is',sum(a))
    

