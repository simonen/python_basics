total_steps = 0
is_going_home = False
while not is_going_home and total_steps <= 10000:
    steps = input()
    if steps == "Going home":
        is_going_home = True
        steps = int(input())
    total_steps += int(steps)
if total_steps < 10000:
    print(f"{10000 - total_steps} more steps to reach goal.")
else:
    print(f"Goal reached! Good job!")
    print(f"{total_steps - 10000} steps over the goal!")
