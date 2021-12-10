s=input('enter a string of alphabets followed by digits: ')
output=''
for ch in s:
    if ch.isalpha():
        x=ch
        output=output+ch
    else:
        d=int(ch)
        new=chr(ord(x)+d)
        output=output+new
print(output)
