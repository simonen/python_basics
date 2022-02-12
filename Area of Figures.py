figure = input()
from math import pi

if figure == "square":
    square_side = float(input())
    print(square_side * square_side)
if figure == "rectangle":
    rect_side_a = float(input())
    rect_side_b = float(input())
    print(rect_side_a * rect_side_b)
if figure == "circle":
    radius = float(input())
    print(float(pi * radius * radius))
if figure == "triangle":
    height = float(input())
    base = float(input())
    print(height * base / 2)

