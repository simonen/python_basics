n = int(input())
sum_odd = 0
sum_even = 0

for number in range(0, n):
    value = int(input())
    if number % 2 == 0:
        sum_even += value
    else:
        sum_odd += value
#     print(f"Position #{number} = {value}")
#
# print(sum_odd)
# print(sum_even)
if sum_odd == sum_even:
    print(f"Yes")
    print(f"Sum = {sum_even}")
else:
    print(f"No")
    print(f"Diff = {abs(sum_odd - sum_even)}")
