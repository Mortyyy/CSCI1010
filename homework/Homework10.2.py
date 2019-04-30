# -*- coding: utf-8 -*-
"""

@author: Alex

Given the dictionary: squares = {1:1, 2:4, 3:9, 4:16,5:25}. 
Do the following operations (without using any built-in methods).

"""
squares = {1:1, 2:4, 3:9, 4:16,5:25}

# Part 1: Remove the item with key = 4
squares = {i:squares[i] for i in squares if i!=4}
print(squares)

# Part 2: Update squares to include square of 6
squares[6] = 36
print(squares)
