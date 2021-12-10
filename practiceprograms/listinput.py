list1=[]
len=int(input('enter the length of the list:'))

for i in range(len):
    data=int(input('enter the item'))
    list1.append(data)

print('the list you entered is',list1)

while True:
    item=int(input('enter the item:'))
    list1.append(item)
    choice=input('want to stop? if yes, press yes else, press any key')
    if (choice =='yes'):
        break

print('the list you entered is',list1)

print('the sum of elementa in list is',sum(list1))
