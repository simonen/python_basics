exam_hour = int(input())
exam_minute = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

total_exam_minutes = exam_hour * 60 + exam_minute
# print(f"Total Exam Minutes {total_exam_minutes}")
total_minutes_of_arrival = hour_of_arrival * 60 + minute_of_arrival
# print(f"Total minutes of arrival {total_minutes_of_arrival}")

total_minute_difference = total_exam_minutes - total_minutes_of_arrival
# print(f"Total Minute Difference {total_minute_difference}")

hour_difference = abs(total_minute_difference) // 60
# print(f"Hour Difference {hour_difference}")

minute_difference = abs(total_minute_difference) % 60
# print(f"Minute Difference {minute_difference}")

if hour_difference == 0 and total_minute_difference == 0:
    print("On time")
elif hour_difference == 0 and total_minute_difference > 0 and minute_difference <= 30:
    print("On time")
    print(f"{minute_difference} minutes before the start")
elif hour_difference == 0 and total_minute_difference > 0:
    print("Early")
    print(f"{minute_difference} minutes before the start")
elif hour_difference > 0 and total_minute_difference > 0:
    print("Early")
    print(f"{hour_difference}:{minute_difference:02d} hours before the start")
elif hour_difference == 0 and total_minute_difference < 0:
    print("Late")
    print(f"{minute_difference} minutes after the start")
elif hour_difference > 0 and total_minute_difference < 0:
    print("Late")
    print(f"{hour_difference}:{minute_difference:02d} hours after the start")
