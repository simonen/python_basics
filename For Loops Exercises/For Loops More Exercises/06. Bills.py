months = int(input())
water = 20
internet = 15
el_bill = 0
bill = 0
other = 0
for month in range(0, months):
    electricity = float(input())
    #water += 20
    #internet += 15
    other += (electricity + water + internet) * 1.2
    el_bill += electricity
    bill += electricity + other
    #print(f"Electricity: {el_bill} lv.")
    #print(f"Water: {water} lv.")
    #print(f"Internet: {internet} lv.")
    #print(f"Other monthly: {other} lv.")
    #print(f"Bill for month #{month}: {bill}")

average = (el_bill + water * months + internet * months + other) / months

print(f"Electricity: {el_bill:.2f} lv")
print(f"Water: {(water * months):.2f} lv")
print(f"Internet: {(internet * months):.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {average:.2f} lv")
#print(f"Total bill: {bill}")
