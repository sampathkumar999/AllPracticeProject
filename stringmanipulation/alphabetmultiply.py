s = input('enter alphabets and digits alternatively:')
output = ''
for ch in s:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        output = output + x*d

print(output)



