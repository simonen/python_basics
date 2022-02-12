import sys

n = int(input())
max_number = -sys.maxsize
sum = 0
for number in range(1, n + 1):
    value = int(input())
    sum += value
    if value > max_number:
        max_number = value
# print("max number: " + str(max_number))
if sum == 2 * max_number:
    print("Yes")
    print(f"Sum = {sum - max_number}")
else:
    print("No")
    print(f"Diff = {abs(2 * max_number - sum)}")
