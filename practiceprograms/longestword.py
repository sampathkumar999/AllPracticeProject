def LongestWord(l):
  maxx = len(l[0])
  temp = l[0]
  for i in l:
    if len(l[i]) > maxx:
      maxx = len(l[i])
      temp = i

  return temp





l = ["one", "two", "third", "four"]

print(LongestWord(l))