# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 19:14:22 2019

@author: Alex
"""
import math

print("This program takes a value from the user and raises it to both 5 and a power determined by another input.")

a = int(input("Enter a number: "))
b = int(input("Enter a power to raise this to: "))

print("The number raised to", b, "is", math.pow(a,b))
print("The number raised to the fifth power is: ", math.pow(a,5))
