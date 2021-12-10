s = input('enter a sentence:')
l = s.split()
l1 = []
n = len(l)
for x in range(n):
    if x%2 == 0:
        l1.append(l[x])
    else:
        l1.append(l[x][::-1])

print('the alternative reversed word form of given sentence is- ',' '.join(l1))