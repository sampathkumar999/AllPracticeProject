s = input('enter a string to display occurences of vowels:' )
d={}
v=['a','e','i','o','u']
for ch in s:
    if ch in v:
         d[ch]=d.get(ch,0)+1

for k,v in sorted(d.items()):
    print('{} occured {} times'.format(k,v))
