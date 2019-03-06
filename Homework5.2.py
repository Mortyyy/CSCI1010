# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 20:36:58 2019

@author: Alex
"""
""" PART A """

def Tens_swap(array):
    first = (array[0])//10
    last = (array[len(array)-1])//10
    
    if first == last:
        return True
    else:
        return False
    
#Test cases.  
Tens_swap([21,12,45,67,29])
Tens_swap([32, 45, 23])
Tens_swap([76,89,23,45,10,70])


""" PART B """

def Average_add(array):
    array.append(sum(array)//len(array))
    return array

#Test cases.
Average_add ([1,2,3]) 
Average_add ([7,1,4]) 
Average_add ([0,2,10])