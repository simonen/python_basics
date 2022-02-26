locations = int(input())

for location in range(1, locations + 1):
    gold_per_location = 0
    average_gold_mined = 0
    expected_gain = float(input())
    mining_days = int(input())
    for day in range(1, mining_days + 1):
        gold_mined = float(input())
        gold_per_location += gold_mined
    average_gold_mined = gold_per_location / mining_days
    diff = abs(average_gold_mined - expected_gain)
    if average_gold_mined >= expected_gain:
        print(f"Good job! Average gold per day: {average_gold_mined:.2f}.")
    else:
        print(f"You need {diff:.2f} gold.")