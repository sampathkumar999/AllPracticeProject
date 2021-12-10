s = input('enter alphabets and numbers alternatively:')
alphabets = []
digits = []
for l in s:
    if l.isalpha():
        alphabets.append(l)
    else:
        digits.append(l)

print(''.join(sorted(alphabets) + (sorted(digits))))


