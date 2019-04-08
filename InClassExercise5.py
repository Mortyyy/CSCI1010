# -*- coding: utf-8 -*-
"""

@author: Alex

"""
    
def cat_dog (string):
    string = string.upper()
    countcat = 0
    countdog = 0
    
    for i in range(0, (len(string)-2)):
        if string[i:(i+3)] == "CAT":
            countcat+=1
        elif string[i:(i+3)] == "DOG":
            countdog+=1
    
    if countcat == countdog:
        return True
    else:
        return False
    
print(cat_dog("catdog"))
print(cat_dog("catcat"))
print(cat_dog("1cat1cadodog"))
