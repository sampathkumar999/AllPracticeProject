s = input('enter a sentence:')
l = s.split()
l1 = []
for word in l:
    l1.append(word[::-1])
print('the reversed words of the sentence are:',' '.join(l1))