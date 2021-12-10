88
a=int(input('enter first no.'))
b=int(input('enter second no.'))
min=a if a<b else b
print('smallest no. is',min)



a=int(input('enter first no'))
b=int(input('enter second number'))
c=int(input('enter third no.'))
min=a if a<b and a<c else b if b<c else c
print('minimum value:',min)

a=int(input('enter first no'))
b=int(input('enter second number'))
print('equal'if a==b else 'second no. is greater' if a<b else 'first no is greater')


