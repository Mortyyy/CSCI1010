# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 18:38:20 2019

@author: Alex
"""

#Finds the total surface area of a cylinder using its diameter.

import math

def surfaceAreaCyl(d, h):
    surfA = int((math.pi*d*h)+(2*math.pi*math.pow((d/2),2)))
    return surfA

diameter = int(input("Enter the cylinder's diameter: "))
height = int(input("Enter the height of the cylinder: "))

print("The surface area is: ", surfaceAreaCyl(diameter, height))
