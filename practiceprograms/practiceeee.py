A = input()

P = input()
c = 0
for i in A:
    for j in P:
        if i==j:
            c=c+1

print(c)