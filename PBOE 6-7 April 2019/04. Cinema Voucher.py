voucher_value = int(input())

cost = 0
movie_tickets = 0
others = 0

while voucher_value >= 0:
    purchase = input()
    if purchase == "End":
        break
    length = len(purchase)
    first_char = purchase[0]
    second_char = purchase[1]
    if length > 8:
        cost = ord(first_char) + ord(second_char)
        if cost <= voucher_value:
            movie_tickets += 1
    elif length <= 8:
        cost = ord(first_char)
        if cost <= voucher_value:
            others += 1
    voucher_value -= cost

print(f"{movie_tickets}")
print(f"{others}")
