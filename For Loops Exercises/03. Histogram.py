n = int(input())
value = 0
sum_p_one = 0
sum_p_two = 0
sum_p_three = 0
sum_p_four = 0
sum_p_five = 0
for number in range(1, n + 1):
    value = int(input())
    if value < 200:
        sum_p_one += 1
    elif 200 <= value < 400:
        sum_p_two += 1
    elif 400 <= value < 600:
        sum_p_three += 1
    elif 600 <= value < 800:
        sum_p_four += 1
    elif value >= 800:
        sum_p_five += 1

# print(f"P1 Count: {sum_p_one}")
# print(f"P1 Count: {sum_p_two}")
# print(f"P1 Count: {sum_p_three}")
# print(f"P1 Count: {sum_p_four}")
# print(f"P1 Count: {sum_p_five}")
print(f"{(sum_p_one / n * 100):.2f}%")
print(f"{(sum_p_two / n * 100):.2f}%")
print(f"{(sum_p_three / n * 100):.2f}%")
print(f"{(sum_p_four / n * 100):.2f}%")
print(f"{(sum_p_five / n * 100):.2f}%")
