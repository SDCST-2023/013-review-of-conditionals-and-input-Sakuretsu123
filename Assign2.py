#!python3
import math
"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""

x = float(input("Enter a number : "))
y = float(input("Enter another number : "))
question = str(input("Is one of the number the hypothenuse of a right triangle ? (type yes or no)"))

if "yes" in question and x > y:
    square_z = x*x - y*y
    square_z = math.sqrt(square_z)
if "yes" in question and y > x: 
    square_z = y*y - x*x
    square_z = math.sqrt(square_z)
if "no" in question: 
    square_z = y*y + x*x
    square_z = math.sqrt(square_z)

square_z = round(square_z, 1)
print(f"{square_z} is the lenghth of the missing side")



