# -*- coding: utf-8 -*-
"""

@author: Alex

A program that reads a text file from your computer. The text
file must have at least 5 lines of text (content). Write the contents of this file
into a new file and give this new file a title.

"""
in_file = open("fivelines.txt", "r")
out_file = open("newfivelines.txt", "w")
lines = in_file.readlines()

if len(lines) >= 5:
    for i in range(len(lines)):
        out_file.write(lines[i])
        i+=1
else:
    print("Not enough lines.")

in_file.close()
out_file.close()


