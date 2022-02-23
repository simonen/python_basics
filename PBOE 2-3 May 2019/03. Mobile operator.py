contract_term = input()
contract_scope = input()
internet = input()
months = int(input())

price = 0

if contract_term == "one":
    if contract_scope == "Small":
        price = 9.98
    elif contract_scope == "Middle":
        price = 18.99
    elif contract_scope == "Large":
        price = 25.98
    elif contract_scope == "ExtraLarge":
        price = 35.99
elif contract_term == "two":
    if contract_scope == "Small":
        price = 8.58
    elif contract_scope == "Middle":
        price = 17.09
    elif contract_scope == "Large":
        price = 23.59
    elif contract_scope == "ExtraLarge":
        price = 31.79

if internet == "yes":
    if price <= 10:
        price += 5.5
    elif price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85

if contract_term == "two":
    price *= 0.9625

total = months * price

print(f"{total:.2f} lv.")