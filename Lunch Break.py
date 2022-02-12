import math
serial = str(input())
episode_length = int(input())
break_length = int(input())

rest_time = (break_length * 0.25)
break_length = (break_length * 0.875)
free_time = break_length - rest_time
minutes_needed = math.ceil(float(episode_length - free_time))
free_minutes = math.ceil(float(free_time - episode_length))

if free_time < episode_length:
    print(f"You don't have enough time to watch {serial}, you need {minutes_needed} more minutes.")
else:
    print(f"You have enough time to watch {serial} and left with {free_minutes} minutes free time.")

