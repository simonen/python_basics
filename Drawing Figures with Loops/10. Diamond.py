n = int(input())
for row in range(0, (n + 1) // 2):

    print("-" * ((n + 1) // 2 - row - 1), end="")
    # Top vertex
    if row == 0:
        if n % 2 == 0:
            print("*", end="")
        else:
            print("", end="")
    else:
        print("*", end="")
    # Inner body "-"
    if n % 2 == 0:
        print("-" * 2 * row, end="")
    else:
        print("-" * (2 * row - 1), end="")
    # Outer right body
    print("*", end="")
    print("-" * ((n + 1) // 2 - row - 1), end="")
    print()

for row2 in range(1, (n + 1) // 2):
    # Outer left body
    print("-" * row2, end="")
    print("*", end="")
    # Inner body
    print("-" * (n - 2 * row2 - 2), end="")
    # Bottom vertex
    if row2 == (n + 1) // 2 - 1:
        if n % 2 == 0:
            print("*", end="")
        else:
            print("", end="")
    else:
        print("*", end="")
    # Outer right body
    print("-" * row2, end="")
    print()
