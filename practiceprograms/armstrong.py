num=input("enter a number: ")
n=len(num)
number=int(num)
result = 0
for i in num:
    result = result + int(i)**n

if result == number:
    print('the given no. is armstrong')
else:
    print('the given no. is not an armstrong')
