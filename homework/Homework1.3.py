# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 18:26:40 2019

@author: Alex
"""

#A program that outputs the area of a circle given its radius = 3.7 inches.

import math

def circleArea(radius):
    a = math.pi*math.pow(radius,2)
    print(a)

circleArea(3.7)
