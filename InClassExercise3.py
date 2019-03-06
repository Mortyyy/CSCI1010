# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 18:49:40 2019

@author: Alex

Given two int arrays, return a new array length two containing their middle elements.
If the length if the array is an even number, then return the average of the two
middle numbers.

"""
def middle_way(a, b):
    if len(a) % 2 == 0:
        middleA = int((len(a)/2))
    else:
        middleA = int((len(a)/2)) + 1
    if len(b) % 2 == 0:
        middleB = int((len(b)/2))
    else:
        middleB = int((len(b)/2)) + 1
    
    #Averages the middle elements for all lists. If the list is odd, nothing happens.
    # Both of the values being added are the same, so the average is...
    x = (a[middleA-1] + a[-middleA]) / 2
    y = (b[middleB-1] + b[-middleB]) / 2
    
    return [x,y]

#Test cases.
print(middle_way([1,2,3,4],[4,5,6]))    #[2.5, 5]
print(middle_way([7,7,7], [3,8,0,5]))   #[7,4]
print(middle_way([5,2,9],[1,4,5]))      #[2,4]
print(middle_way([1,4,2,5,8],[2,4]))    #[2,3]