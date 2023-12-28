#Create a program to calculate the area and circumference of a circle. Ask the user for the radius.

# Area = pi x r^2
# Circumference = 2 x pi x r
import math

print("Today we'll be calculating the circumference and area of a circle. All I need from you is the radius.")
radius = input("Please enter the radius of your circle: ")

area = math.pi * (int(radius) ** 2)
circumference = (2 * math.pi * int(radius))
print("Area: ", round(area,2))
print("Circumference: ", round(circumference,2))