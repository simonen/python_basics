days = int(input())
hours = int(input())
bill = 0
last_bill = 0
for day in range(1, days + 1):
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            bill += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            bill += 1.25
        else:
            bill += 1
    print(f"Day: {day} - {(bill - last_bill):.2f} leva")
    last_bill = bill
print(f"Total: {bill:.2f} leva")
