# Types of projections ==>
projection = input()        #Premier = 12.00 Normal = 7.50, Discount = 5.00
rows = int(input())
cols = int(input())

is_projection_valid = 1
price = 0
total_seats = rows * cols

if projection == "Premiere":
    price = 12.00
elif projection == "Normal":
    price = 7.50
elif projection == "Discount":
    price = 5.00
else:
    is_projection_valid = 0

income = total_seats * price

print(f"{income:.2f} leva")




