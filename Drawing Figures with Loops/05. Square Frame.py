n = int(input())

for row in range(1):
    print("+", end=" ")
    for i in range(1, n - 1):
        print("-", end=" ")
    print("+")
for row2 in range(1, n - 1):
    print("|", end=" ")
    for k in range(1, n - 1):
        print("-", end=" ")
    print("|")
for row3 in range(1):
    print("+", end=" ")
    for i in range(1, n - 1):
        print("-", end=" ")
    print("+")