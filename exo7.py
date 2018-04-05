n = int(input())
if n < 0:
    print("Input positive value")
elif n == 0:
    print("+")
else:
    print('+', end="")
    for _ in range(n):
        print(3*'-', end="")
    print('+')

    for i in range(n):
        print('|', end="")
        for _ in range(n):
            print(3*" ", end="")
        print('|')

    print('+', end="")
    for _ in range(n):
        print(3*'-', end="")
    print('+')

