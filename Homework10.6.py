# -*- coding: utf-8 -*-
"""
@author: Alex

A Python program to match key values in two different dictionaries.

"""

x = {'key1': 1, 'key2': 3, 'key3': 2} 
y = {'key1': 1, 'key2': 2} 

z = {}

for i in x:
    for j in y:
        if x[i] == y[j] and i == j:
            z[i] = x[i]

print(z)