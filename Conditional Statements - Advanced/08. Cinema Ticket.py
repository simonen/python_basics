day = input()
price = int()

if day == "Wednesday" or day == "Thursday":
    price = 14
elif day == "Saturday" or day == "Sunday":
    price = 16
else:
    price = 12
print(price)