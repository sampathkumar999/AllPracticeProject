from itertools import permutations
lst = ['a','e','i','o','u']
allstrings = permutations(lst)
print(type(allstrings))
for string in allstrings:
    print(''.join(string))

