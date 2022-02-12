n = int(input())
left_sum = 0  # sum = 100
right_sum = 0
value = 0
for number in range(1, n + 1):
    value = int(input())
    left_sum += value
    # difference = sum_one - sum_two
for number in range(1, n + 1):
    value = int(input())
    right_sum += value
    # difference = sum_one - sum_two

if left_sum == right_sum:
    print(f"Yes, sum = {right_sum} ")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")
