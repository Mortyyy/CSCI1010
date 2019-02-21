"""

@author: Alex

This is a Python function that checks whether a passed string is palindrome or not.
"""

def isPalindrome(string):
    string.replace(" ", "") #Removes all whitespace.
    gnirts = string[::-1]   #Reverses the input string.
    
    if string == gnirts:
        return True
    else:
        return False
    
    

s = str(input("This program checks whether the input is palindromic. Enter the string: "))
print(isPalindrome(s))