fruit = input()
pack_size = input()
packs_ordered = int(input())
pack_price = 0
small = 2
big = 5
if fruit == "Watermelon":
    if pack_size == "small":
        pack_price = small * 56
    elif pack_size == "big":
        pack_price = big * 28.70
elif fruit == "Mango":
    if pack_size == "small":
        pack_price = small * 36.66
    elif pack_size == "big":
        pack_price = big * 19.60
elif fruit == "Pineapple":
    if pack_size == "small":
        pack_price = small * 42.10
    elif pack_size == "big":
        pack_price = big * 24.80
elif fruit == "Raspberry":
    if pack_size == "small":
        pack_price = small * 20
    elif pack_size == "big":
        pack_price = big * 15.20

order = packs_ordered * pack_price

if 400 <= order <= 1000:
    order *= 0.85
if order > 1000:
    order *= 0.5

print(f"{order:.2f} lv.")