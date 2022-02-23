strawberry_price = float(input())
banana_kg = float(input())
orange_kg = float(input())
raspberry_kg = float(input())
strawberry_kg = float(input())

total_cost = strawberry_price * strawberry_kg + raspberry_kg * strawberry_price * 0.5 \
    + orange_kg * strawberry_price * 0.5 * 0.6 + banana_kg * strawberry_price * 0.5 * 0.2

print(total_cost)