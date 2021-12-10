s = input('enter a string:')
i = 0
for x in s:
    print('the character present at positive index{} and at negetive index{} is:{}'.format(i,i-len(s),x))
    i+=1
