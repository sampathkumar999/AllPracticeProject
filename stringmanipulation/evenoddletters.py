s = input('enter a string- ')
print('the characters present at the even positions are:')
i = 0
while i < len(s):
    print(s[i])
    i = i + 2

print('the characters present at the odd positions are:')
i = 1
while i < len(s):
    print(s[i])
    i = i + 2



#second way
s1 = s
print('the characters present at the even positions are:', s1[::2])
print('the characters present at the odd positions are:', s1[1::2])