num=int(input('enter a number: '))
count=1

if (num<0):
    print('the factorial does not exist')
elif(num==0):
    print('the factorial of zero is 1') 


else:
    for i in range(1,num+1):
        count=count*i


    print('the factorial of given no. is:',count)

#recursive function

def factorial(n):
    return 1 if(n==0 or n==1) else n*factorial(n-1)
num=int(input('enter a number: '))
print('the factorial of',num,'is',factorial(num))
