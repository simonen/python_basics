days = int(input())

sport = ""
result = ""
win_days = 0
lose_days = 0
wins = 0
losses = 0
daily_money = 0
total_money = 0
while days > 0:

    sport = input()
    if sport == "Finish":
        days -= 1
        if wins > losses:
            daily_money *= 1.1
            win_days += 1
        else:
            lose_days += 1
        wins = 0
        losses = 0
        total_money += daily_money
        daily_money = 0
        continue
    result = input()
    if result == "win":
        daily_money += 20
        wins += 1
    elif result == "lose":
        losses += 1

if win_days > lose_days:
    print(f"You won the tournament! Total raised money: {(total_money * 1.2):.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")