target_money = int(input())
count = 0
card_count = 0
cash_count = 0
card_income = 0
cash_income = 0
while target_money > 0:
    transaction = input()
    if transaction == "End":
        print("Failed to collect required money for charity.")
        break
    if count % 2 == 0:
        if 0 < int(transaction) <= 100:  # cash only
            target_money -= int(transaction)
            cash_income += int(transaction)
            cash_count += 1
            print("Product sold!")
        else:
            print("Error in transaction!")
    elif int(transaction) > 10:  # card only
        target_money -= int(transaction)
        card_income += int(transaction)
        card_count += 1
        print("Product sold!")
    else:
        print("Error in transaction!")
    count += 1
else:
    if cash_income == 0:
        print(f"Average CS: {0}")
    else:
        print(f"Average CS: {(cash_income / cash_count):.2f}")
    if card_income == 0:
        print(f"Average CC: {0}")
    else:
        print(f"Average CC: {(card_income / card_count):.2f}")



