N = int(input())
if N % 2 == 0:
    for i in range(N, 0, -1):
        if i % 2 == 0:
            print(i * '1')
        else:
            print(i * '0')

else:
    for i in range(N, 0, -1):
        if i % 2 == 0:
            print(i * '0')
        else:
            print(i * '1')
