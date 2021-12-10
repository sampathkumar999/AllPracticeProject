from array import *
a=array('i',[])
n=int(input('enter the length of the array'))
for i in range(n):
    x=int(input('enter the array element'))
    a.append(x)
print('the array you entered is',a)

val=int(input('enter a value to search in th array'))
k=0
for e in a:
    if val==e:
        print('the value is present in the array')
        break
    k+=1
else:
    print('the value is not present in the array')

