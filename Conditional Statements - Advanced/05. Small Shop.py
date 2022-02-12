# product = input()
# city = input()
# quantity = float(input())
#
# price = float()
#
# # if product == "coffee" and city == "Sofia":
# #     price = 0.50
# # if product == "coffee" and city == "Plovdiv":
# #     price = 0.40
# # if product == "coffee" and city == "Varna":
# #     price = 0.45
# # if product == "water" and city == "Sofia":
# #     price = 0.80
# # if product == "water" and city == "Plovdiv":
# #     price = 0.70
# # if product == "water" and city == "Varna":
# #     price = 0.70
# # if product == "beer" and city == "Sofia":
# #     price = 1.20
# # if product == "beer" and city == "Plovdiv":
# #     price = 1.15
# # if product == "beer" and city == "Varna":
# #     price = 1.10
# # if product == "sweets" and city == "Sofia":
# #     price = 1.45
# # if product == "sweets" and city == "Plovdiv":
# #     price = 1.30
# # if product == "sweets" and city == "Varna":
# #     price = 1.35
# # if product == "peanuts" and city == "Sofia":
# #     price = 1.60
# # if product == "peanuts" and city == "Plovdiv":
# #     price = 1.50
# # if product == "peanuts" and city == "Varna":
# #     price = 1.55
#
# grand_total = price * quantity
#
# print(grand_total)

product = input()
city = input()
quantity = float(input())
price = float()

if product == "coffee":
    if city == "Sofia":
        price = 0.5
    elif city == "Plovdiv":
        price = 0.4
    elif city == "Varna":
        price = 0.45
elif product == "water":
    if city == "Sofia":
        price = 0.8
    elif city == "Plovdiv":
        price = 0.7
    elif city == "Varna":
        price = 0.7
elif product == "beer":
    if city == "Sofia":
        price = 1.2
    elif city == "Plovdiv":
        price = 1.15
    elif city == "Varna":
        price = 1.10
elif product == "sweets":
    if city == "Sofia":
        price = 1.45
    elif city == "Plovdiv":
        price = 1.30
    elif city == "Varna":
        price = 1.35
elif product == "peanuts":
    if city == "Sofia":
        price = 1.6
    elif city == "Plovdiv":
        price = 1.5
    elif city == "Varna":
        price = 1.55
grand_total = price * quantity

print(grand_total)
