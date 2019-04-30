# -*- coding: utf-8 -*-
"""

@author: Alex

Create a function that takes an integer as an argument and generates a
dictionary that contains the numbers (between 1 and n) in the form (x,x*x).

"""

def squareTo(n):
    squares = {} 
    i = 1
    while i <= n:
        squares[i] = i * i
        i += 1    
    print(squares)

squareTo(5)
