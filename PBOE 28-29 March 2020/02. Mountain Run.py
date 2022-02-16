current_record = float(input())      #seconds
distance = float(input())   # meters to scale
speed = float(input()) # time to scale 1 meter
# S = V * T, V = 1 * meter / seconds * T => T = S / V = distance * seconds

delay = (distance // 50) * 30      # * 30 seconds

george = distance * speed + delay

difference = abs(george - current_record)

if george >= current_record:
    print(f"No! He was {difference:.2f} seconds slower.")
else:
    print(f" Yes! The new record is {george:.2f} seconds.")

