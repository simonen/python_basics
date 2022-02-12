movie = input()
total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
is_finish = False
while movie != "Finish":
    seats = int(input())
    per_movie_tickets = 0
    ticket_type = input()
    free_seats = seats
    while ticket_type != "End":
        per_movie_tickets += 1
        percent_full = per_movie_tickets / seats * 100
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
        free_seats -= 1
        if free_seats == 0:
            break
        ticket_type = input()
        if ticket_type == "Finish":
            is_finish = True
            break
    total_tickets += per_movie_tickets
    print(f"{movie} - {percent_full:.2f}% full.")
    if is_finish:
        break
    movie = input()

print(f"Total tickets: {total_tickets}")
print(f"{(student_tickets / total_tickets * 100):.2f}% student tickets.")
print(f"{(standard_tickets / total_tickets * 100):.2f}% standard tickets.")
print(f"{(kid_tickets / total_tickets * 100):.2f}% kids tickets.")
