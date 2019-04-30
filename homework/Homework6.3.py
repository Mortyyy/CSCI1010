# -*- coding: utf-8 -*-
"""

@author: Alex

Takes two user inputs: an integer N, a Boolean.
If Boolean is True, then return all even integers up to N (less than or equal to)
else return all odd integers up to N (less than or equal to).

"""
def OddOrEven(number, boolean):
    
    integers = []
    
    if boolean == True:
        i = 2
    elif boolean == False:
        i = 1
    else:
        raise Exception("Invalid input.")
    
    while i <= number:
        integers.append(i)
        i+=2
        
    return integers

print(OddOrEven(10, True))
print(OddOrEven(10, False))
print(OddOrEven(13, False))
