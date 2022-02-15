# With delivery
# Without delivery
# 90X130
frame_count = int(input())
frame_size = input()
delivery = input()

price = 0

if frame_size == "90X130":
    price = 110
    if 30 < frame_count <= 60:
        price *= 0.95
    elif frame_count > 60:
        price *= 0.92
elif frame_size == "100X150":
    price = 140
    if 40 < frame_count <= 80:
        price *= 0.94
    elif frame_count > 80:
        price *= 0.9
elif frame_size == "130X180":
    price = 190
    if 20 < frame_count <= 50:
        price *= 0.93
    elif frame_count > 50:
        price *= 0.88
elif frame_size == "200X300":
    price = 250
    if 25 < frame_count <= 50:
        price *= 0.91
    elif frame_count > 50:
        price *= 0.86

grand_total = price * frame_count

if delivery == "With delivery":
    grand_total += 60

if frame_count > 99:
    grand_total *= 0.96
if frame_count <= 10:
    print("Invalid order")
else:
    print(f"{grand_total:.2f} BGN")
