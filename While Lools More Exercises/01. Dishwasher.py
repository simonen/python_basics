detergent_bottles = int(input())
pots = 0
dishes = 0
count = 0
detergent = detergent_bottles * 750
while detergent * 750 >= 0:
    dirty_dish = input()
    if dirty_dish == "End":
        print("Detergent was enough!")
        print(f"{dishes} dishes and {pots} pots were washed.")
        print(f"Leftover detergent {detergent} ml.")
        break
    count += 1
    if count % 3 == 0:
        detergent -= int(dirty_dish) * 15
        pots += int(dirty_dish)
    else:
        detergent -= int(dirty_dish) * 5
        dishes += int(dirty_dish)

else:
    print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")
