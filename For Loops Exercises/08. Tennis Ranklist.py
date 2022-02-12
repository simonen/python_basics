import math

import math

tournaments = int(input())

starting_points = int(input())
points = 0
points_earned = 0
total_tournaments = 0
tournaments_won = 0
for number in range(1, tournaments + 1):
    t_outcome = input()
    if t_outcome == "W":
        points += 2000
        tournaments_won += 1
#        print(f"Winner + {2000} points")
    elif t_outcome == "F":
        points += 1200
#        print(f"Finalist + {1200} points")
    elif t_outcome == "SF":
        points += 720
        #print(f"Semi Finalist + {720} points")
    #points_earned += points
    #print(f"Tournament #{number}: Points earned {points}")
    total_tournaments += 1
   # print(f"Tournaments played: {total_tournaments}")
   # print(f"Tournaments Won: {tournaments_won}")

average_points = points / total_tournaments
print(f"Final points: {points + starting_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{(tournaments_won / total_tournaments * 100):.2f}%")









#tournaments = int(input())
# starting_points = int(input())
# points = 0
# points_earned = 0
# total_tournaments = 0
# tournaments_won = 0
# for number in range(1, tournaments + 1):
#     t_outcome = input()
#     if t_outcome == "W":
#         points += 2000
#         tournaments_won += 1
#         print(f"Winner + {2000} points")
#     elif t_outcome == "F":
#         points += 1200
#         print(f"Finalist + {1200} points")
#     elif t_outcome == "SF":
#         points += 720
#         print(f"Semi Finalist + {720} points")
#     #points_earned += points
#     print(f"Tournament #{number}: Points earned {points}")
#     total_tournaments += 1
#     print(f"Tournaments played: {total_tournaments}")
#     print(f"Tournaments Won: {tournaments_won}")
#
# average_points = points / total_tournaments
# print(f"Final points: {points + starting_points}")
# print(f"Average points: {math.floor(average_points)}")
# print(f"Success rate: {(tournaments_won / total_tournaments * 100):.2f}%")
#
#
