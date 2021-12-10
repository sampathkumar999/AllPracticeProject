print('is and is not operator')

a=10
b=20
print('Is a is b?',a is b)

a=True
b=False
print(a is b)


a='durga'
b='durga'
print(id(a))
print(id(b))
print(a is b)


list1=[1,2,3,'one','two','sampath']
list2=[1,2,3,'one','two','sampath']
print(id(list1))
print(id(list2))
print(list1 is list2)
print(list1 is not list2)
print(list1[1] is list2[1])
print(list1==list2)

print('in and not in operator')

x='hello, Learning python is very easy'

print('h' in x)
print('s' in x)
print('hello' in x)
print('hello' not in x)

mylist=[1,2,3,'sampath','python','kishan']
print(1 in mylist)
print(2 not in mylist)
print('sampath' in mylist)
print('kishan' not in mylist)
