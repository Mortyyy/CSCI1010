# -*- coding: utf-8 -*-
"""

@author: Alex

This algorithm gets the Fibonacci series between 0 to a user provided value.

"""

def fibonacci(n):
    sequence = [0, 1]
    while sequence[-1] < n:
        x = (sequence[-1] + sequence[-2])
        if x < n:
            sequence.append(x)
        else:
            break
    return sequence

number = int(input("Enter an upper limit for the Fibonacci finder: "))
print(fibonacci(number))
