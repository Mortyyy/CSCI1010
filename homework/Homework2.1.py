# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 18:36:33 2019

@author: Alex

This program returns the maximum of two numbers.

"""

def determineMax (a,b):
    if a > b:
        print("The first number is larger.")
    elif a < b: 
        print("The second number is larger.")
    else:
        print("These numbers are equal.")

n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))

determineMax(n,m)
