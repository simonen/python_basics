needed_money = float(input())
available_money = float(input())
spend_streak = 0
days = 0

while available_money < needed_money:
    action = input()
    amount = float(input())
    if action == "spend":
        available_money -= amount
        spend_streak += 1
        if amount > available_money:
            available_money = 0
    elif action == "save":
        available_money += amount
        spend_streak = 0
    days += 1
    if spend_streak == 5:
        print("You can't save the money.")
        print(days)
        break

else:
    print(f"You saved the money for {days} days.")