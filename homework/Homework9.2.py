# -*- coding: utf-8 -*-
"""

@author: Alex

Verify the following:
    A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
    A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)

"""

A = {"a", "b", "d", "e"}
B = {"b", "c", "e", "f"}
C = {"d", "e", "f", "g"}

print([A and (B or C)] == [(A and B) or (A and C)]) #Evaluates as True.
print([A or (B and C)] == [(A or B) and (A or C)])  #Evaluates as True.
