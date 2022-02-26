age = input()

kids = 0
adults = 0
toys = 0
sweaters = 0

while age != "Christmas":
    if int(age) <= 16:
        kids += 1
    elif int(age) > 16:
        adults += 1
    age = input()
toys_cost = kids * 5
sweaters_cost = adults * 15

print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {toys_cost}")
print(f"Money for sweaters: {sweaters_cost}")