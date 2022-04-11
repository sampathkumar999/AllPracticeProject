def MinWindowSubstring(strArr):

  n = strArr[0]
  k = strArr[1]
  l = []
  for i in k:
    if i in n:
      l.append(n.index(i))

  l.sort()
  l = set(l)
  l = list(l)


  return n[l[0]:l[-1]]

# keep this function call here
print(MinWindowSubstring(['skdhsakjdhdakjd', 'jkhsdkjh']))