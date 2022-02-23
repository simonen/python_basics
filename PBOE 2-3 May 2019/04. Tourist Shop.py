budget = float(input())
product = input()
is_stop = False
count = 0
cost = 0
while product != "Stop":
    count += 1
    price = float(input())
    if count % 3 == 0:
        price *= 0.5
    if budget < price:
        diff = abs(budget - price)
        print(f"You don't have enough money!")
        print(f"You need {diff:.2f} leva!")
        count -= 1
        is_stop = True
        break
    cost += price
    budget -= price

    product = input()

if not is_stop:
    print(f"You bought {count} products for {cost:.2f} leva.")