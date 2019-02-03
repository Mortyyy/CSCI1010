"""
@author: Alex

This program that adds 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
given string is less than 3, leave it unchanged.

"""

def strEdit(s):
    #Handles strings that are shorter than three characters.
    if len(s) < 3:
        raise Exception("This string is too short.")
    
    #Retrieves and evaluation of the last three characters.
    end = s[(len(s)-3):len(s)]
    if end == "ing":
        s = s + "ly"
    else:
        s = s + "ing"
    return s
    
string = str(input("Enter a string, should be three or more characters long: "))
print(strEdit(string))