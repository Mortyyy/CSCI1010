# -*- coding: utf-8 -*-
"""
@author: Alex

Returns the number of values for all keys. 
For example for dict the answer is 5 because total values in both lists is 5. 

"""

dic =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']} 
counter = 0

for key in dic:
    counter += len(dic[key])
    
print(counter)
