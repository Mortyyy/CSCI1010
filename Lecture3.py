# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 18:17:55 2019

@author: Alex
"""
#Compares two numbers, if they're equal the program outputs TRUE. 
def numCompare():
    number1=float(input("Enter the first number."))
    number2=float(input("Enter the second number."))

    print((number1>=number2))


#Takes user's name and greets them.
def greetMachine():
    name = str(input("What's your name? "))
    print("Hi, ", name, "! Nice to meet you.")
    