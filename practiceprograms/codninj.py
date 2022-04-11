n = int(input())

for i in range(n + 1):
    if i == n:
        print("-" * 24, end="")
        print("*" * (i - 1))

    else:
        print("\t\t" + ' ' * i + "*" * (i - 1))

for i in range(n + 1, 0, -1):
    if i == n + 1:
        print('', end="")
        print("*" * (i - 1))
    else:
        print("\t\t" + ' ' * i + "*" * (i - 1))