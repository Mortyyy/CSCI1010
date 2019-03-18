# -*- coding: utf-8 -*-
"""
@author: Alex

This program takes a user input n and prints all
numbers that are multiples of 5 up to n.

"""

def multipleTo(n):
    n = int(n)
    multiples = []
    i = 5
    
    #Error case if number is smaller than 5.
    if i > n:
        return "No multiples."
    
    while i <= n:
        multiples.append(i)
        i+=5
        
    return multiples
    
number = input("Enter an upper limit: ")
print(multipleTo(number))
