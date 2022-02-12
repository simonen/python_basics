world_record = float(input())
distance_to_swim = float(input())
time_one = float(input())
#speed = 1 / time_one

time_to_swim = distance_to_swim * time_one
delay = distance_to_swim // 15 * 12.5
ivan_time = time_to_swim + delay

if world_record > ivan_time:
    print(f"Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {(ivan_time - world_record):.2f} seconds slower.")




