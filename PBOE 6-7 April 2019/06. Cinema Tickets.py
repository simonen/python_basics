movie = input()
ticket_type = ""
standard = 0
student = 0
kid = 0
seats_taken = 0
percent_full = 0
total_tickets_sold = 0
is_finish = False
while movie != "Finish":
    seats_taken = 0
    free_seats = int(input())
    ticket_type = input()
    while ticket_type != "End":
        if ticket_type == "standard":
            standard += 1
        elif ticket_type == "student":
            student += 1
        elif ticket_type == "kid":
            kid += 1
        seats_taken += 1
        if seats_taken == free_seats:
            break
        ticket_type = input()
        if ticket_type == "Finish":
            is_finish = True
            break
    percent_full = seats_taken / free_seats * 100
    total_tickets_sold += seats_taken
    print(f"{movie} - {percent_full:.2f}% full.")
    if is_finish:
        break
    movie = input()

student_percent = student / total_tickets_sold * 100
standard_percent = standard / total_tickets_sold * 100
kid_percent = kid / total_tickets_sold * 100

print(f"Total tickets: {total_tickets_sold}")
print(f"{student_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kid_percent:.2f}% kids tickets.")