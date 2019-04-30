#Author: Alex

#This Program takes a user input and if the number is divisible:
#   by 3 and 5, program outputs "YES"
#   by 3 or 5, program outputs "NO"
#Otherwise, the  program outputs "UNKNOWN".

def evaluate (n):
    if (n%3==0) and (n%5==0):
        print("Yes.")
    elif (n%3==0) or (n%5==0):
        print("No.")
    else:
        print("Unknown.")
        
number = int(input("Enter a number: "))
evaluate(number)
