# -*- coding: utf-8 -*-
"""

@author: Alex

This program that prints all odd numbers in a given
range (both inclusive). For the range, read user provided input for the minimum
value and the maximum value.

"""
def OddRange():
    minimum = int(input("Enter the lower bound: "))
    maximum = int(input("Enter the upper bound: "))
    
    numbers = []
    if minimum % 2 == 0:
        i = minimum + 1
    else:
        i = minimum
    
    while i <= maximum:
        numbers.append(i)
        i += 2
    
    return numbers
