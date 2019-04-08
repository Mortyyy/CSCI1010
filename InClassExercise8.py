# -*- coding: utf-8 -*-
"""

@author: Alex

You have two .txt files that have numbers in them, write a program to do the following:
    Find all the numbers that are common in both files and output/print them.
    Find how many numbers occur at least once in both the files.
    How many numbers occur in either of the files but not in both.
    
"""
#Opens both files.
file_one = open("One.txt")
file_two = open("Two.txt")

#Copies content of files into sets, which allows better comparison.
set_one = set(file_one.read().split())
set_two = set(file_two.read().split())
#Close the files at this point.
file_one.close()
file_two.close()

#Finds intersection of the two sets.
common = set_one & set_two
print("Intersection:", common)

print("The number of values that appear at least once in both is:", len(common))

#The numbers that appear in one but not both are in the symmetric difference.
print("Symmetric Difference:", set_one.symmetric_difference(set_two))