judges = int(input())
presentation = input()
pres_count = 0
eval_sum = 0
while presentation != "Finish":
    pres_count += 1
    rates_sum = 0
    pres_eval = 0
    for num in range(0, judges):
        rate = float(input())
        rates_sum += rate
        pres_eval = rates_sum / judges
    print(f"{presentation} - {pres_eval:.2f}.")
    eval_sum += pres_eval
    presentation = input()
assessment = eval_sum / pres_count
print(f"Student's final assessment is {assessment:.2f}.")