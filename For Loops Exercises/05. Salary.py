import sys

tabs = int(input())
salary = int(input())

for tab in range(tabs, 0, -1):
    website = input()
    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50
    else:
        salary += 0
#    print(f"Current salary is: {salary}")
    if salary <= 0:
        break
if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)