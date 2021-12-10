for x in range(10):
    print('hello')



for x in range(10):
    print(x)


for x in range(20):
    if x%2==0:
       print(x)

mylist=eval(input('enter a list:'))
sum=0
for i in mylist:
    sum=sum+i;
print('sum:',sum)


n=int(input('enter a number:'))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print('the sum of first',n,'natural no.s is',sum)
