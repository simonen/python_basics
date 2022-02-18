target_profit = float(input())
order = 0
income = 0

while target_profit > 0:
    drink = input()
    if drink == "Party!":
        break
    drink_count = int(input())
    drink_price = len(drink)
    order = drink_price * drink_count
    if order % 2 != 0:
        order *= 0.75
    target_profit -= order
    income += order

if target_profit > 0:
    print(f"We need {target_profit:.2f} leva more.")
else:
    print(f"Target acquired.")

print(f"Club income - {income:.2f} leva.")

