"""

@author: Alex

Assignment: 
    Our goal is to make chocolates qwith a certain weight. As ingredients we have small sized bars (1 kilo) and big sized bars (5 kilos).
    Write a function that returns the number of small bars we will need. 
    Assume we will always use big bars before small bars. 
    Return -1 if it can't be done.

"""

def make_chocolate(small, big, goal):
    
    s_weight = small
    b_weight = big * 5
    
    #Calculates how much chocolate we have in total.
    if s_weight + b_weight < goal:
        return -1
    
    if b_weight == goal:
        return 0    #No small bars needed.
    else:
        return -(b_weight - goal)
        
    
s = int(input("Enter the number os]f small bars: "))
b = int(input("Enter the number of big bars: "))
g = int(input("Enter the number of candies you wish to make: "))

print(make_chocolate(s,b,g))
    