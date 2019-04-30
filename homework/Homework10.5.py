# -*- coding: utf-8 -*-
"""

@author: Alex

that takes a number as an input and returns the corresponding key as the output from my_dict. 
If the input value does not exist, then the program must return 'Key does not exist'. 

"""

my_dict = {"java": 100, "python": 112, "c": 11, "R": 131}

def get_key (search):
    for key, value in my_dict.items():  #Items method gives a tuple in format key, value.
        if value == search:
            return key
    return "Key does not exist."

print(get_key(100))    #java                      
print(get_key(131))    #R                      
print(get_key(140))    #Key does not exist 
