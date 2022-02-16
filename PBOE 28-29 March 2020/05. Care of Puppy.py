food_bank = int(input())
food_intake = int(input())
food_string = str(food_intake)
food_eaten = food_intake

while food_string != "Adopted":
    food_intake = input()
    if food_intake == "Adopted":
        break
    food_eaten += int(food_intake)

difference = abs(food_bank * 1000 - food_eaten)

if food_bank * 1000 >= food_eaten:
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    print(f"Food is not enough. You need {difference} grams more." )