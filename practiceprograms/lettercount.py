#PROGGRAM TO FIND THE NUMBER OF OCCURENCES OF EACH LETTER IN A WORD

word=input('enter a word: ')
d={}
for x in word:
    d[x]=d.get(x,0)+1
for k,v in d.items():
    print(k,'occured',v,'times')
