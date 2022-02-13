

is_pass_cracked = False
count = 0
control_number = int(input())
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d:
                    if a * b + c * d == control_number:
                        count += 1
                        if count == 4:
                            password = str(a) + str(b) + str(c) + str(d)
                            is_pass_cracked = True
                        print(f"{a}{b}{c}{d}", end=" ")

if is_pass_cracked:
    print()
    print(f"Password: {password}")
else:
    print()
    print("No!")
