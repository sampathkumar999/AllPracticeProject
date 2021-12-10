s=input('enter a string to remove duplicates: ')
output=''
for ch in s:
    if ch not in output:
        output=output+ch
print(output)

#second way
s=input('enter a string to remove duplicates: ')
s1=set(s)
print(''.join(s1))