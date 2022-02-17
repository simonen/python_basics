movie = input()
projection = input()
tickets_sold = int(input())
ticket_price = 0

if movie == "A Star Is Born":
    if projection == "normal":
        ticket_price = 7.50
    elif projection == "luxury":
        ticket_price = 10.50
    elif projection == "ultra luxury":
        ticket_price = 13.50
elif movie == "Bohemian Rhapsody":
    if projection == "normal":
        ticket_price = 7.35
    elif projection == "luxury":
        ticket_price = 9.45
    elif projection == "ultra luxury":
        ticket_price = 12.75
elif movie == "Green Book":
    if projection == "normal":
        ticket_price = 8.15
    elif projection == "luxury":
        ticket_price = 10.25
    elif projection == "ultra luxury":
        ticket_price = 13.25
elif movie == "The Favourite":
    if projection == "normal":
        ticket_price = 8.75
    elif projection == "luxury":
        ticket_price = 11.55
    elif projection == "ultra luxury":
        ticket_price = 13.95

income = tickets_sold * ticket_price
print(f"{movie} -> {income:.2f} lv.")