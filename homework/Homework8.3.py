# -*- coding: utf-8 -*-
"""

@author: Alex

This a function asks for an integer and prints the square of it. Use a while 
loop with a try, except, else block to account for incorrect inputs.

"""
while True:
    x = input("Enter a integer to square: ")
    
    try:
        y = int(x)**2
    except ValueError:
        print("ValueError")
    else:
        print(x,"squared is",y)
        break
    
    
