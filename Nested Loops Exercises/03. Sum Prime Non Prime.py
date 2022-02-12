number = input()
flag = False
prime_sum = 0
non_prime_sum = 0
#number_to_string = int(number)
while number != "stop":
    if int(number) < 0:
        print("Number is negative.")
    elif int(number) > 1:
        for i in range(2, int(number)):
            if int(number) % i == 0:
                non_prime_sum += int(number)
                flag = True
                break
        else:
            prime_sum += int(number)
    number = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")

