initial_number = int(input())
number = int(input())
total_sum = number

while initial_number > total_sum:
#    print("po malko, brat")
    number = int(input())
    total_sum += number
print(f"{total_sum}")
