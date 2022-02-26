from math import ceil

gpu_price = int(input())
adapter_price = int(input())
gpu_power = float(input())       #per day
gpu_profit = float(input())       #per day

gear_cost = gpu_price * 13 + adapter_price * 13 + 1000
daily_profit = (gpu_profit - gpu_power) * 13
break_even = ceil(gear_cost / daily_profit)

print(f"{gear_cost}")
print(f"{break_even}")
