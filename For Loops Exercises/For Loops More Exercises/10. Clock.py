import sys

n = int(input())
even_sum = 0
odd_sum = 0
even_min = 1000000000
even_max = -1000000000
odd_min = 1000000000
odd_max = -1000000000

for i in range(1, n + 1):
    numbers = float(input())
#    print(f"Pos #{i}: {numbers}")
    if i % 2 != 0:
        odd_sum += numbers

        if numbers > odd_max:
            odd_max = numbers
        if numbers < odd_min:
            odd_min = numbers

    else:
        even_sum += numbers
        if numbers > even_max:
            even_max = numbers
        if numbers < even_min:
            even_min = numbers
    # print(f"even sum: {even_sum}")
    # print(f"odd sum: {odd_sum}")
    # print(f"EvenMin={even_min:.2f},")
    # print(f"OddMin={odd_min:.2f},")

print(f"OddSum={odd_sum:.2f},")
if odd_min == 1000000000:
    print(f"OddMin=No,")
else:
    print(f"OddMin={odd_min:.2f},")
if odd_max == -1000000000:
    print(f"OddMax=No,")
else:
    print(f"OddMax={odd_max:.2f},")
print(f"EvenSum={even_sum:.2f},")
if even_min == 1000000000:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={even_min:.2f},")
if even_max == -1000000000:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={even_max:.2f}")
