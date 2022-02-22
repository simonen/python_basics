computers = int(input())
sales = 0
total_sales = 0
rating_sum = 0

for computer in range(1, computers + 1):
    number = input()
    rating = int(number[-1])
    possible_sales = int(number[:2])
    if rating == 2:
        sales = 0
    elif rating == 3:
        sales = possible_sales * 0.5
    elif rating == 4:
        sales = possible_sales * 0.7
    elif rating == 5:
        sales = possible_sales * 0.85
    elif rating == 6:
        sales = possible_sales
    total_sales += sales
    rating_sum += rating

average_rating = rating_sum / computers
print(f"{total_sales:.2f}")
print(f"{average_rating:.2f}")