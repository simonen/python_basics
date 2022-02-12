month = input()
stay = int(input())
studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if 7 < stay < 14:
        studio = 50 * 0.95
    elif stay > 14:
        studio = 50 * 0.7
        apartment = 65 * 0.9
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if stay > 14:
        studio = 75.20 * 0.8
        apartment = 68.70 * 0.9
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    if stay > 14:
        apartment = 77 * 0.9

studio_cost = studio * stay
apartment_cost = apartment * stay
print(f"Apartment: {apartment_cost:.2f} lv.")
print(f"Studio: {studio_cost:.2f} lv.")
