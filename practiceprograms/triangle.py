print('for right angled triangle')


n=int(input('enter no. of rows'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='')
    print()

n=int(input('enter no. of rows:'))
for i in range(1,n+1):
    print('*'*i)



print('for equilateral triangle')


n=int(input('enter no. of rows'))
for i in range(1,n+1):
    print(' '*(n-i),end=' ')
    print('*'*i)
    
