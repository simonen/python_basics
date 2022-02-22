parcel_weight = float(input())  # kg
service = input()
distance = int(input())

km_price = 0
nadcenka = 0
if service == "standard":
    if parcel_weight < 1:
        km_price = 0.03
    elif 1 <= parcel_weight < 10:
        km_price = 0.05
    elif 10 <= parcel_weight < 40:
        km_price = 0.10
    elif 40 <= parcel_weight < 90:
        km_price = 0.15
    elif 90 <= parcel_weight < 150:
        km_price = 0.20
elif service == "express":
    if parcel_weight < 1:
        km_price = 0.03
        nadcenka = km_price * 0.8 * parcel_weight
    elif 1 <= parcel_weight < 10:
        km_price = 0.05
        nadcenka = km_price * 0.4 * parcel_weight
    elif 10 <= parcel_weight < 40:
        km_price = 0.10
        nadcenka = km_price * 0.05 * parcel_weight
    elif 40 <= parcel_weight < 90:
        km_price = 0.15
        nadcenka = km_price * 0.02 * parcel_weight
    elif 90 <= parcel_weight < 150:
        km_price = 0.20
        nadcenka = km_price * 0.01 * parcel_weight

cost = (km_price + nadcenka) * distance

print(f"The delivery of your shipment with weight of {parcel_weight:.3f} kg. would cost {cost:.2f} lv.")
