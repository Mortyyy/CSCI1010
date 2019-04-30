"""

@author: Alex

This program calculates the surface area of a right circular cylinder.
It takes both the cylinder's radius and height as user input. 
"""

import math

#Calculates area of a circle using radius.
def circleArea(radius):
    area = math.pi*math.pow(radius,2)
    return area

#Calculates surface area of right circular cylinder.
def cylinderSurfaceArea(radius, height):
    surfaceArea = 2*math.pi*radius*height + 2*circleArea(radius)
    return surfaceArea

r = int(input("Enter the cylinder's radius: "))
h = int(input("Enter the cylinder's height: "))

print("The surface area of this cylinder is", str(cylinderSurfaceArea(r,h)))
