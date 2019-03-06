# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:38:46 2019

@author: Alex
"""

def factor(n):
    i = 1
    factorlist = []
    while i < n:
        if (n%i) == 0:
            factorlist.append(i)
        elif i == n:
            break
        i+=1
    factorlist.append(n)
    print(factorlist)
        
factor(20)