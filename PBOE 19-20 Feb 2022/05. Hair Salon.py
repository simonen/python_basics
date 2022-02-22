target = int(input())
price = 0
income = 0
service = input()
sub_service = ""

while service != "closed":

    if service == "haircut":
        sub_service = input()
        if sub_service == "mens":
            price = 15
        elif sub_service == "ladies":
            price = 20
        elif sub_service == "kids":
            price = 10
    elif service == "color":
        sub_service = input()
        if sub_service == "touch up":
            price = 20
        elif sub_service == "full color":
            price = 30
    income += price
    if income >= target:
        print(f"You have reached your target for the day!")
        break
    service = input()

difference = abs(target - income)
if target > income:
    print(f"Target not reached! You need {difference}lv. more.")
print(f"Earned money: {income}lv.")
