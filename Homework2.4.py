"""

@author: Alex

This program takes input as a string. Replaces all occurrences of its first
character by "&" sign (except the first character itself). 
If the input is "rechargerr" then the output must be "recha&ge&&".

"""

def replaceLetter(s):
    char1 = s[0]
    segment = s[1:(len(s))]
    return char1+segment.replace(char1, "&")
    
string = str(input("Enter a string: "))
print(replaceLetter(string))