number = int(input())
state = ""

if (100 <= number <= 200) or number == 0:
    state = ""
else:
    state = "invalid"
print(state)
