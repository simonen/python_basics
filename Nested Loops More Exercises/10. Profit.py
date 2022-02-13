coins1 = int(input())
coins2 = int(input())
notes5 = int(input())
bill = int(input())

for ones in range(coins1 + 1):
    for twos in range(coins2 + 1):
        for fives in range(notes5 + 1):
            if (ones * 1 + twos * 2 + fives * 5) == bill:
                print(f"{ones} * 1 lv. + {twos} * 2 lv. + {fives} * 5 lv. = {bill} lv.")
