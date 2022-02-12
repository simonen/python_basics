from math import fabs
budget = float(input())
gpus = int(input())
cpus = int(input())
ram = int(input())

gpu_cost = gpus * 250
cpu_cost = gpu_cost * 0.35 * cpus
ram_cost = gpu_cost * 0.1 * ram
grand_total = gpu_cost + cpu_cost + ram_cost

if gpus > cpus:
    grand_total *= 0.85
if budget < grand_total:
    print(f"Not enough money! You need {grand_total - budget:.2f} leva more!")
else:
    print(f"You have {budget - grand_total:.2f} leva left!")



