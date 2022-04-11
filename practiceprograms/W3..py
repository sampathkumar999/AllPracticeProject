def check_unique_elements(input_list):
    l = []
    for i in input_list:
        if i not in l:
            l.append(i)
    if len(input_list) == len(l):
        print('All items are unique')
    else:
        print('All items are not unique')

check_unique_elements([1,2,3,4,1,6])
