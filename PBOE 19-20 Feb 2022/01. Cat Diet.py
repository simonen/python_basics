fats = int(input())                     #percent
protein = int(input())                  #percent
carbs = int(input())                    #percent
calories = int(input())                 #percent
water = int(input())                    #percent

fats_gram = (fats * calories / 900)
protein_gram = (protein * calories / 400)
carbs_gram = (carbs * calories / 400)

food_gram = fats_gram + protein_gram + carbs_gram
calories_per_gram = calories / food_gram
real_calories = calories_per_gram * (1 - water / 100)

print(f"{real_calories:.4f}")
