lst = ['ca t', 'car', 'fea r', 'cente r']
lst2 = []
for i in lst:
  if ' ' in i:
    lst2.append(True)
  elif ' ' not in i:
    lst2.append(False)

print(lst2)

