s='learning'
a=' python is'
m=' very easy'
print(s+a+m)
print(s*4)
print(len(s+a+m))
i=0
for i in (s+a+m):
    print(i,end='')
print()
subs=input('enter sub string')
if subs in s:
    print('found')
else:
    print('not found')

if s==a:
    print('equal')
elif(s<a):
    print('s is less than a')
else:
    print('s is greater than a')
            
