days = int(input())
food_bank = float(input())

food_eaten = 0
total_biscuits = 0
total_dog_food = 0
total_cat_food = 0

for day in range(1, days + 1):
    biscuits = 0
    dog_food = int(input())
    total_dog_food += dog_food
    cat_food = int(input())
    total_cat_food += cat_food
    daily_food = dog_food + cat_food
    if day % 3 == 0:
        biscuits = daily_food * 0.1
    total_biscuits += biscuits
    food_eaten += daily_food

percent_food = food_eaten / food_bank * 100
dog_percent = total_dog_food / food_eaten * 100
cat_percent = total_cat_food / food_eaten * 100

print(f"Total eaten biscuits: {round(total_biscuits)}gr.")
print(f"{percent_food:.2f}% of the food has been eaten.")
print(f"{dog_percent:.2f}% eaten from the dog.")
print(f"{cat_percent:.2f}% eaten from the cat.")