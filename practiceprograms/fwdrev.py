s = input('enter a sentence:')
print('forward direction:')
for i in s:
    print(i,end='')

print()
n = len(s)
print('reverse direction:')
i = -1
while(i>=-n):
    print(s[i],end = '')
    i -= 1
