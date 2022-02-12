destination = input()
while destination != "End":
    # if destination == "End":
    #     break
    budget = float(input())
    saved_money = 0
    while budget > saved_money:
        money_in = float(input())
        saved_money += money_in
    print(f"Going to {destination}!")
    destination = input()