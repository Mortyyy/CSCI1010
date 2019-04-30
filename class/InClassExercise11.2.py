# -*- coding: utf-8 -*-
"""
InClassExercise11.2.py

@author: Alex

Given 2 dictionaries called dict1 and dict2. 
Every value (in the key value pair) is a list of integers. 
Write a program that sorts each list (for every key value pair).

"""

dict1 ={ 
    "L1":[87, 34, 56, 12], 
    "L2":[23, 00, 30, 10], 
    "L3":[1, 6, 2, 9], 
    "L4":[40, 34, 21, 67] 
}

dict2 ={ 
    "L1":["Welcome", "to", "RPI"], 
    "L2":["A", "computer", "science"], 
    "L3":["course", "for", "everyone"], 
} 

def sortUp(x):
    for key, value in x.items():
        value.sort()
    print(x)
    
sortUp(dict1)
sortUp(dict2)
