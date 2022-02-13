n = int(input())
# roof
for row in range(0, (n + 1) // 2):
    print("-" * ((n + 1) // 2 - row - 1), end="")
    if n % 2 == 0:
        print("*" * 2, end="")
    else:
        print("*", end="")
    for i in range(2, row + 2):
        print("*" * 2, end="")
    print("-" * ((n + 1) // 2 - row - 1), end="")
    print()

for row2 in range(0, n // 2):
    print("|" + "*" * (n - 2), end="")
    print("|", end="")
    print()
