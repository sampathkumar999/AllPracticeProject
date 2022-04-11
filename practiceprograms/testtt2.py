F1 = [('u1','u2'),
      ('u3','u4'),
      ('u1','u5'),
      ('u2','u1'),
      ('u3','u4')]
f2 = []
for i in F1:
      if i not in f2 and i[::-1] not in f2:
            f2.append(i)

print(f2)