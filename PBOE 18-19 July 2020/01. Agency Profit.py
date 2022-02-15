airline = input()
tickets_seniors = int(input())
tickets_juniors = int(input())
ticket_price = float(input())
service_tax = float(input())

senior_cost = ticket_price + service_tax
junior_cost = ticket_price * 0.3 + service_tax


income = (senior_cost * tickets_seniors + junior_cost * tickets_juniors) * 0.2

print(f"The profit of your agency from {airline} tickets is {income:.2f} lv.")
