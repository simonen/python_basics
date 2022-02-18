drink = input()
sugar = input()
drink_count = int(input())

price = 0
if drink == "Espresso":
    if sugar == "Without":
        price = 0.90 * 0.65
    elif sugar == "Normal":
        price += 1
    elif sugar == "Extra":
        price += 1.20
    if drink_count >= 5:
        price *= 0.75
elif drink == "Cappuccino":
    if sugar == "Without":
        price = 1.00 * 0.65
    elif sugar == "Normal":
        price += 1.20
    elif sugar == "Extra":
        price += 1.60
elif drink == "Tea":
    if sugar == "Without":
        price = 0.50 * 0.65
    elif sugar == "Normal":
        price += 0.60
    elif sugar == "Extra":
        price += 0.70

cost = drink_count * price

if cost > 15:
    cost *= 0.8

print(f"You bought {drink_count} cups of {drink} for {cost:.2f} lv.")
