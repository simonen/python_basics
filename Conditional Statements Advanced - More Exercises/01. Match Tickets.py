budget = float(input())
category = input()
fans = int(input())
transport_fees = 0
ticket_cost = 0
# Transport fees

if 1 <= fans < 5:
    transport_fees = 0.75 * budget
elif 5 <= fans < 10:
    transport_fees = 0.6 * budget
elif 10 <= fans < 25:
    transport_fees = 0.5 * budget
elif 25 <= fans < 50:
    transport_fees = 0.4 * budget
else:
    transport_fees = 0.25 * budget

tickets_money = budget - transport_fees

if category == "VIP":
    ticket_cost = fans * 499.99
elif category == "Normal":
    ticket_cost = fans * 249.99

difference = abs(tickets_money - ticket_cost)

if ticket_cost > tickets_money:
    print(f"Not enough money! You need {difference:.2f} leva.")
else:
    print(f"Yes! You have {difference:.2f} leva left.")