s = input('enter a string::')
output = s[::-1]
print("reversed string is:",output)

#second way

s1 = input('enter a string:')
s2 = reversed(s1)
print(''.join(s2))

##Third way

s3 = input('enter a string:')
result = ''
i = len(s3)-1
while i>=0:
    result = result + s3[i]
    i = i-1
print('the reverse order of given string is:',result)

