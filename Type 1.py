# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 14:07:45 2022

@author: GDA
"""

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
calci = True                    # to repeat the while loop to ask the user if he wants to run the calculator again
while calci == True:
    a = input(" Do you want to run the calculator again? \n y for yes, n for no \n")             #user need to answer y or n 

    if a == "y":                                    # if user wants to run the calculator

        x = int(input("Enter first number: "))                #first input from user
        y = int(input("Enter second number: "))               #second input from user
        sum = x + y             #adds the two numbers
        sub = x - y             # subtracts second number from first number
        mul = x * y             # multiply the two numbers
             
        operation = True
        
        while operation == True:
            z =  input("Enter the operation. s for sum, o for subtraction, m for multiplication, and d for division \n")
        
            if z == "s":            #if user wants addition
                print(sum)
                operation = False   #to leave the loop after printing the result
            elif z == "o":          #if user wants subtraction
                print(sub)
                operation = False
            elif z == "m":          #if user wants multiplication
                print(mul)
                operation = False
            elif z == "d":          #if user wants division
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
        calci = False                           #if user wants to end the calculator
    else:
        print("Please enter valid choice")      #if user enters any other operation choice
        