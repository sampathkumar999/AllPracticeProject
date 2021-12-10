r=int(input('enter range upto which fibanocci is to be printed:'  ))

n1=0
n2=1

print(n1)
print(n2)

for i in range(2,r):
    sum=n1+n2
    print(sum)
    n1=n2
    n2=sum
