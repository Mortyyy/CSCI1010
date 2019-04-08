# -*- coding: utf-8 -*-
"""

@author: Alex

This checks if a number is perfect or not.

A positive integer is perfect if it's equal to the sum of its
proper positive divisors. Equivalently, a perfect number is a number that is
half the sum of all of its positive divisors (including itself).

The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6.
Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 

"""

def isPerfect (number):
    divsum = 0  #Container for the sum of the divisors.
    
    #Finds proper divisors.
    i = 1
    while i <= number:
        if number%i == 0:
            divsum += i
        i+=1
    
    if divsum//2 == number:
        return True
    else:
        return False
