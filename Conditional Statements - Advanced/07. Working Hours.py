hour = int(input())
day = input()

state = ""

if (10 <= hour <= 18) and day != "Sunday":
    state = "open"
else:
    state = "closed"
print(state)
