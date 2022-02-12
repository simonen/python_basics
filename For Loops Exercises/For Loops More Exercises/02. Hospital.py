days = int(input())
doctors = 7
treated = 0
untreated = 0
# total_untreated = 0
# total_treated = 0
for day in range(1, days + 1):
    patients_in = int(input())
    #    print(f"Day #{day}. Patients in: {patients_in}")
    if day % 3 == 0 and (untreated > treated):
        doctors += 1
    if patients_in > doctors:
        treated += doctors
        untreated += patients_in - doctors
    else:
        treated += patients_in
        untreated += 0

    # print(f"Doctors: {doctors}")
    # print(f"Treated: {treated}")
    # print(f"Untreated: {untreated}")
    # print()
    # print(f"Treated patients: {total_treated}")
    # print(f"Untreated patients: {total_untreated}")
print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")
