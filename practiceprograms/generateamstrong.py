k = int(input('Enter interval to generate amstrong numbers: '))
for i in range(1,k):
    s = 0
    n = str(i)
    l = len(n)
    for j in range(0,l):
        s = s+int(n[j])**l
    if s == i:
        print(i)

