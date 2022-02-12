total_balance = 0
operation = ''
deposit = input()

while deposit != "NoMoreMoney":
    increase = float(deposit)
    if increase < 0:
        print(f"Invalid operation!")
        break
    print(f"Increase: {increase :.2f}")
    deposit = input()
    total_balance += increase

print(f"Total: {total_balance:.2f}")