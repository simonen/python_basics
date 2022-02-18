from math import ceil

people = int(input())
entrance_fee = float(input())
lounge_price = float(input())
shade_price = float(input())


shade_cost = ceil(people / 2) * shade_price
lounge_cost = ceil(people * 0.75 ) * lounge_price
cost = people * entrance_fee + lounge_cost + shade_cost

print(f"{cost:.2f} lv.")