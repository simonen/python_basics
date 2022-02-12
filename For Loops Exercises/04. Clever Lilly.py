age = int(input())
washer_price = float(input())
toy_price = int(input())
money = 0
toys = 0
money_received = 0
money_stolen = 0      #brother steals 1 lv each time Lilly gets cash
for year in range(1, age + 1):
    if year % 2 == 0:
        money += 10
        money_received += money
        money_stolen += 1
    else:
        toys += 1
total_money = money_received - money_stolen + toys * toy_price
if washer_price <= total_money:
    print(f"Yes! {(total_money - washer_price):.2f}")
else:
    print(f"No! {(washer_price - total_money):.2f}")



# money = 10 + 10 * 0 = 10, 10 * 10 * 1 = 20

# from math import ceil
#
# age = int(input())
# washer_price = float(input())
# toy_price = int(input())
#
# even_bds = 0
# odd_bds = 0
# saved_money = 0
#
# # 10 // 2 = 5 -> 4 4etni rd = 5 * 9 lv = 45 lv
# # 3 // 2 =  2 - ne4etni rd = 5 igra4ki * x leva
# # 1i 2p 3i 4p 5i 6p 7i 8p 9i 10p 11i
#
#
# even_bds = age // 2
#
# odd_bds = ceil(age / 2)
#
# # print(f"Even Bdds: {even_bds}")
# # print(f"Odd Bdds: {odd_bds}")
# saved_money = (even_bds / 2) * (2 * 10 + (even_bds - 1) * 10)
# # print(f"Saved_money: {saved_money} ")
# # print(f"Prihodi ot igra4ki: {toy_price * odd_bds}")
#
# total_money = saved_money + toy_price * odd_bds - even_bds
# # print(f"Total Cash: {total_money}")
# if washer_price <= total_money:
#     print(f"Yes! {(total_money - washer_price):.2f}")
# else:
#     print(f"No! {abs(washer_price - total_money):.2f}")
