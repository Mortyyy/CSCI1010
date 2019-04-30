# -*- coding: utf-8 -*-
"""

@author: Alex

Prints all the letters in a nested list as a single string.

"""

def ListToStr (letterlist):
    letters = ""
    
    #Cycles through major list.
    for i in range(len(letterlist)):
        #Cycles through nested list.
        for j in range(len(letterlist[i])):
            letters = letters + (str(letterlist[i][j]))
    return letters

print(ListToStr([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]))
