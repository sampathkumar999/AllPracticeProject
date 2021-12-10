s = input('enter a string to display occurences of each char:' )
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1

for k,v in sorted(d.items()):
    print('{} occured {} times'.format(k,v))
