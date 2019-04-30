# -*- coding: utf-8 -*-
"""
InClassExercise11.1.py

@author: Alex

We are playing a game in which we create words. 
Each letter of the alphabet has some points assigned to it, 
given in the dictionary score. Takes a word as an input and 
calculates the score.

"""

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def Word_Score (word):
    points = 0
    for letter in list(word.lower()):   #Converts the word to a list containing the characters. Loops through.
        if letter not in score.keys():
            return "Invalid input."
        points += score[letter]         #Looks up the point value associated with the letter and adds it in,
    return points

Word_Score('Tod8y')     #Should be 9.
Word_Score('Elephant')  #Should be 13.
