load_count = int(input())
load = 0
busload = 0
truckload = 0
trainload = 0
price = 0
total_cost = 0
total_weight = 0
for number in range(0, load_count):
    tonage = int(input())
    if tonage <= 3:
        price = 200 * tonage
        busload += tonage
    elif 4 <= tonage <= 11:
        price = 175 * tonage
        truckload += tonage
    elif tonage >= 12:
        trainload += tonage
        price = 120 * tonage
    total_weight += tonage
    total_cost += price

average_ton_price = total_cost / total_weight
print(f"{average_ton_price:.2f}")
print(f"{(busload / total_weight * 100):.2f}%")
print(f"{(truckload / total_weight * 100):.2f}%")
print(f"{(trainload / total_weight * 100):.2f}%")
