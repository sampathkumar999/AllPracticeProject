s = input('enter a string of repeated alphabets:')
previous = s[0]
c = 1
i = 1
output = ''
while i < len(s):
    if s[i] ==previous:
        c = c + 1
    else:
        output = output + str(c) + previous
        previous = s[i]
        c = 1
    if i == len(s) - 1:
        output = output + str(c) + previous
        i = i + 1
print(output)
