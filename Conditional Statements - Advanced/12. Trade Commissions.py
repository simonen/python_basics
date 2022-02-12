city = input()
sales = float(input())
state = ""
commission = 0
is_city_valid = True
is_sales_valid = True



if 0 <= sales <= 500:
    if city == "Sofia":
        commission = 0.05
    elif city == "Varna":
        commission = 0.045
    elif city == "Plovdiv":
        commission = 0.055
elif 500 < sales <= 1000:
    if city == "Sofia":
        commission = 0.07
    elif city == "Varna":
        commission = 0.075
    elif city == "Plovdiv":
        commission = 0.08
elif 1000 < sales <= 10000:
    if city == "Sofia":
        commission = 0.08
    elif city == "Varna":
        commission = 0.1
    elif city == "Plovdiv":
        commission = 0.12
elif sales > 10000:
    if city == "Sofia":
        commission = 0.12
    elif city == "Varna":
        commission = 0.13
    elif city == "Plovdiv":
        commission = 0.145
if commission == 0:
    print("error")
else:
    grand_total = sales * commission
    print(f"{grand_total:.2f}")


#grand_total = sales * commission

#if (city == "Sofia" or city == "Varna" or city == "Plovdiv") and sales > 0: #and sales > 0:
#     print(f"{grand_total:.2f}")
# else:
#     print("error")