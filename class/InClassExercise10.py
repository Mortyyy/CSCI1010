# -*- coding: utf-8 -*-
"""

@author: Alex

Given a string, find if it's a permutation of a palindrome. 
Assume no spaces between characters of the given string.

"""
import collections

#Operates on the assumption that there is a mathematical limit to the number of characters in a palindrome.
def isPalindrome(letters):
    x = collections.Counter(letters)    #Dictionary of the string's letters and occurences.
    
    #Loop through dictionary for a short circuit evaluation.
    oddcount = 0    #If there is more than one number that occurs an odd number of times, it can't be a palindrome.
    for values in x.values():
        if values % 2 != 0:
            oddcount += 1  
          
    if oddcount != 1:
        return False
    else:
        return True
            

isPalindrome('xxxyy')       #True
isPalindrome('tactcoa')     #True
isPalindrome('runnurses')   #True
isPalindrome('omm')         #True
isPalindrome('mono')        #False
isPalindrome('table')       #False            
