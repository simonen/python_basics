inherited_money = float(input())
exit_year = int(input())
money_spent = 0
age = 17

for year in range(1800, exit_year + 1):
#    print(year)
    age += 1
    if year % 2 == 0:
        money_spent += 12000
    else:

        money_spent += 12000 + 50 * age
 #   print(f"Current age is: {age}")
 #   print(f"Money spent so far: {money_spent}")

if inherited_money >= money_spent:
    print(f"Yes! He will live a carefree life and will have {(inherited_money - money_spent):.2f} dollars left.")
else:
    print(f"He will need {abs(inherited_money - money_spent):.2f} dollars to survive.")