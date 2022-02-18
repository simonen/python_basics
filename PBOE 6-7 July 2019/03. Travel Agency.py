import sys

town = input()
package = input()
vip_discount = input()
days_count = int(input())

price = 0
is_invalid = False

if days_count <= 0:
    print("Days must be positive number!")
    sys.exit()
elif town == "Bansko" or town == "Borovets":
    if package == "withEquipment":
        price = 100
        if vip_discount == "yes":
            price *= 0.9
    elif package == "noEquipment":
        price = 80
        if vip_discount == "yes":
            price *= 0.95
    else:
        is_invalid = True
elif town == "Varna" or town == "Burgas":
    if package == "withBreakfast":
        price = 130
        if vip_discount == "yes":
            price *= 0.88
    elif package == "noBreakfast":
        price = 100
        if vip_discount == "yes":
            price *= 0.93
    else:
        is_invalid = True
else:
    is_invalid = True

total = days_count * price

if days_count > 7:
    total = (days_count - 1) * price

if not is_invalid:
    print(f"The price is {total:.2f}lv! Have a nice time!")
else:
    print("Invalid input!")
