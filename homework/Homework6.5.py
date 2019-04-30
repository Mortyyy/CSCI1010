# -*- coding: utf-8 -*-
"""

@author: Alex

A Python program to check if a user provided three-digit number is an
Armstrong number or not.

A positive integer is called an Armstrong number of order n if
abcd... = an + bn + cn + dn + ...

In case of an Armstrong number of 3 digits, the sum of cubes of each digits 
is equal to the number itself. 

For example:
153 = 1*1*1 + 5*5*5 + 3*3*3 // 153 is an Armstrong number.

"""
    
#Algorithm to determine if it's an Armstrong number.
def isArmstrong(number):
    digitcount = len(str(number))    
    i = 0                       #Iteration factor determined by the number of digits.
    result = 0                  #Will compare the content of this to the number.
    
    while i <= digitcount:
        result += (number//10**i % 10) ** digitcount
        i += 1
        
    if result == number:
        return True
    else:
        return False

isArmstrong(54748)
