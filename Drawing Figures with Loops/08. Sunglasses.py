n = int(input())

# First row

for row in range(1):
    for i in range(0, n * 2):
        print("*", end="")
    for j in range(0, n):
        print(" ", end="")
    for i in range(0, n * 2):
        print("*", end="")
    print()

for row2 in range(0, n - 2):
    print("*", end="")
    for k in range(0, n * 2 - 2):
        print("/", end="")
    print("*", end="")
    if row2 == (n - 1) // 2 - 1:
        for m in range(0, n):
            print("|", end="")
    else:
        for l in range(0, n):
            print(" ", end="")
    print("*", end="")
    for o in range(0, n * 2 - 2):
        print("/", end="")
    print("*", end="")
    print()

for row in range(1):
    for i in range(0, n * 2):
        print("*", end="")
    for j in range(0, n):
        print(" ", end="")
    for i in range(0, n * 2):
        print("*", end="")
    print()
