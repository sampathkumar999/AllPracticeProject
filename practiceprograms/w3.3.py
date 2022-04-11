n = int(input('enter a number:'))
n1 = str(n)
l = []
for i in n1:
    l.append(int(i))


while int(n) > 0:
    n = n-(sum(l))
    print(n)
