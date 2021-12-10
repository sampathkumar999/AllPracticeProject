s=input('enter a string to count occurances of each char: ')
output = ''
for ch in s:
    if ch not in output:
        output=output+ch
for ch in sorted(output):
    print('{} occured {} times'.format(ch,s.count(ch)))