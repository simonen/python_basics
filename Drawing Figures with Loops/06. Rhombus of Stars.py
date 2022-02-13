# @    *
# @   * *
# @  * * *
# @ * * * *
# * * * * * *

n = int(input())

for row in range(1, n + 1):  # 1
    for col in range(n - row):
        print("", end=" ")
    for col2 in range(1, row + 1):
        print("*", end=" ")
    print()

for row2 in range(2, n + 1):  # r#aw = 2
    for col3 in range(1, row2):
        print("", end=" ")
    for col4 in range(n - row2 + 1):
        print("*", end=" ")
    print()
