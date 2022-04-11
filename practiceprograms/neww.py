n = int(input('enter array length'))
l = []
for i in range(1,n+1):
    a = int(input('enter a number'))
    l.append(a)

maxx = l[0]

for i in l:
    if i>maxx:
        maxx = i

print('max=',maxx)


