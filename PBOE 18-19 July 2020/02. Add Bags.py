bag_price = float(input())
total_weight = float(input())
days_until_flight = int(input())
bags_count = int(input())

bags_cost = bag_price

if total_weight < 10:
    bags_cost = bag_price * 0.2
elif 10 <= total_weight <= 20:
    bags_cost = bag_price * 0.5

if days_until_flight > 30:
    bags_cost *= 1.1
elif 7 <= days_until_flight <= 30:
    bags_cost *= 1.15
elif days_until_flight < 7:
    bags_cost *= 1.4

total_cost = bags_cost * bags_count

print(f"The total price of bags is: {total_cost:.2f} lv.")