n = int(input())

for row in range(0, n + 1):
    for i in range(n - row):
        print(" ", end="")
    for j in range(0, row):
        print("*", end="")
    print(" | ", end="")
    for k in range(0, row):
        print("*", end="")
    for p in range(n - row):
        print(" ", end="")
    print()
