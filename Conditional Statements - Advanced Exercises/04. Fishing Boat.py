budget = int(input())
season = input()
fishermen = int(input())

boat_cost = 0

if season == "Spring":
    boat_cost = 3000
elif season == "Summer" or season == "Autumn":
    boat_cost = 4200
elif season == "Winter":
    boat_cost = 2600
if fishermen <= 6:
    boat_cost *= 0.9
elif fishermen <= 11:
    boat_cost *= 0.85
else:
    boat_cost *= 0.75

if fishermen % 2 == 0 and season != "Autumn":
    boat_cost *= 0.95
difference = budget - boat_cost
if budget < boat_cost:
    print(f"Not enough money! You need {abs(difference):.2f} leva.")
else:
    print(f"Yes! You have {difference:.2f} leva left.")

# budget = int(input())
# season = input()
# fishermen = int(input())
#
# boat_cost = 0
#
# if 0 < fishermen <= 6:
#     if season == "Spring":
#         boat_cost = 3000 * 0.9
#     elif season == "Summer" or season == "Autumn":
#         boat_cost = 4200 * 0.9
#     elif season == "Winter":
#         boat_cost = 2600 * 0.9
# elif 7 <= fishermen <= 11:
#     if season == "Spring":
#         boat_cost = 3000 * 0.85
#     elif season == "Summer" or season == "Autumn":
#         boat_cost = 4200 * 0.85
#     elif season == "Winter":
#         boat_cost = 2600 * 0.85
# elif fishermen >= 12:
#     if season == "Spring":
#         boat_cost = 3000 * 0.75
#     elif season == "Summer" or season == "Autumn":
#         boat_cost = 4200 * 0.75
#     elif season == "Winter":
#         boat_cost = 2600 * 0.75
# if fishermen % 2 == 0 and season != "Autumn":
#     boat_cost *= 0.95
# difference = budget - boat_cost
# if difference < 0:
#     print(f"Not enough money! You need {abs(difference):.2f} leva.")
# else:
#     print(f"Yes! You have {difference:.2f} leva left.")
