fruit = input()
day = input()
quantity = float(input())
is_fruit_valid = True
is_day_valid = True
price = 0
state = ""

if day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3.0
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20
    else:
        is_fruit_valid = False
    #     state = "error"
elif day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        price = 2.50
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85
    else:
        is_fruit_valid = False
else:
    is_day_valid = False
    # else:
    #     state = "error"
# else:
#     state = "error"

price *= quantity
if is_day_valid == True and is_fruit_valid == True:
    print(f"{price:.2f}")
else:
    print("error")
# if fruit == "banana" or fruit == "apple" or fruit == "orange" or fruit == "grapefruit" or fruit == "kiwi" \
#     or fruit == "pineapple" or fruit == "grapes":
#     print(f"{grand_total:.2f}")
# else:
#     state = "error"
#     print(state)

# if state == "error":
#     print(state)
# else:
#     print(f"{grand_total:.2f}")

hui = 1
putka = 2
