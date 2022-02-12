# age = float(input())
# sex = input()
#
# title = ''
#
# if age < 16:
#     if sex == "m":
#         title = "Master"
#     elif sex == "f":
#         title = "Miss"
# else:
#     if sex == "m":
#         title = "Mr."
#     elif sex == "f":
#         title = "Ms."
#
# print(title)

age = float(input())
sex = input()

title = ''

if age < 16 and sex == "m":
    title = "Master"
elif age < 16 and sex == "f":
    title = "Miss"
if age >= 16 and sex == "m":
    title = "Mr."
elif age >= 16 and sex == "f":
    title = "Ms."

print(title)

if sex == "f":
    if age >= 16:
        title = "Ms."
    else:
        title = "Miss"
else:
    if age >= 16:
        title = "Mr."
    else:
        title = "Master"
print(title)