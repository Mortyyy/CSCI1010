# -*- coding: utf-8 -*-
"""
@author: Alex

This program takes a list and returns a new list with unique elements of the first list.

"""
def findUnique (elementlist):
    uniquelist = []
    
    #Cycle through the input list.
    for i in range(len(elementlist)):
        #Compare element to the container elements.
        if elementlist[i] not in uniquelist:
            uniquelist.append(elementlist[i])
    return uniquelist

print(findUnique([1,2,3,3,3,3,4,5]))