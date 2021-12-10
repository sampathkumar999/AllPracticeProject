def list_input(list,n):
    a=[]
    n=int(input('enter list size'))
    for i in range(n):
        item=int(input("enter the element"))
        a.append(item)
        print(a)

list_input(list,5)
