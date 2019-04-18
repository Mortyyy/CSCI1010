# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 19:15:52 2019

@author: Alex

If A = {1, 3, 5}, B = {3, 5, 6} and C = {1, 3, 7}. 
Show that A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C).

"""

A = {1, 3, 5}
B = {3, 5, 6}
C = {1, 3, 7} 

if (A or (B and C) == (A or B) and (A or C)):
    print("True")
else:
    print("False")