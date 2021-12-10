from array import *
a = array('i', [])
n = int(input('enter no. of elements'))
for i in range(n):
    x = int(input('enter the element'))
    a.append(x)
print(a)
k = 0
val = int(input('enter the element to be searched in the list'))
for i in a:
    if val == i:
        print('the element is found in the array')
        break
    k += 1
else:
    print('element is not there in the list')

#arraymaxmin

maxx = a[0]
for i in range(1,n):
    if a[i] > maxx:
        maxx = a[i]
print('the biggest element in the list is:',maxx)

minn = a[0]
for i in range(1,n):
    if a[i] < minn:
        minn = a[i]
print('the smallest element in the list is ',minn)
