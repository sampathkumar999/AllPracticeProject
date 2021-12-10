n=int(input('enter nof of rows: '))
for row in range(n):
    for col in range(n):
        if col==0 or row==(n-1) or row==col:
            print('*', end='')
        else:
            print(end=' ')
    print()


#star pattern with filled stars

n=int(input('enter no. of rows: '))
for i in range(n):
    print('*'*i)
