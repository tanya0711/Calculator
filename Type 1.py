# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 14:07:45 2022

@author: GDA
"""

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
calci = True
while calci == True:
    a = input(" Do you want to run the calculator again? \n y for yes, n for no \n")

    if a == "y":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        sum = x + y
        sub = x - y
        mul = x * y
        
        operation = True
        
        while operation == True:
            z =  input("Enter the operation. s for sum, st for subtraction, m for multiplication, and d for division \n")
        
            if z == "s":
                print(sum)
                operation = False
            elif z == "st":
                print(sub)
                operation = False
            elif z == "m":
                print(mul)
                operation = False
            elif z == "d":
                if y == 0:
                    print("The denominator can't be zero")
                    break
                else:  
                    div = x / y
                    print(div)
                    operation = False
            else:
                print("Please enter valid choice")
    elif a == "n":
        calci = False
    else:
        print("Enter valid choice")
        