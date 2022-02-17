movie_count = int(input())

highest_rating = 0
lowest_rating = 10
top_movie = ""
garbage_movie = ""
rating_sum = 0

for movie in range(1, movie_count + 1):
    movie_title = input()
    rating = float(input())
    if rating > highest_rating:
        top_movie = movie_title
        highest_rating = rating
    if rating < lowest_rating:
        garbage_movie = movie_title
        lowest_rating = rating
    rating_sum += rating

average_rating = rating_sum / movie_count

print(f"{top_movie} is with highest rating: {highest_rating}")
print(f"{garbage_movie} is with lowest rating: {lowest_rating}")
print(f"Average rating: {average_rating:.1f}")
