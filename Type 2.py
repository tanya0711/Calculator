# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 15:10:15 2022

@author: GDA
"""
import math            #to import the library to perform mathematical operations
calci = True           # to repeat the while loop to ask the user if he wants to run the calculator again
while calci == True:
    
    a = input(" Do you want to run the calculator again? \n y for yes, n for no \n")        #user need to answer y or n 
    if a == "y":                             # if user wants to run the calculator
        operation = True                     # to ask the user for the correct value of operation again
        while operation == True:
            z =  input("Enter the operation. s for sum, o for subtraction, m for multiplication, d for division, r for square root, p for power, i for sin, and c for cos \n")
            if z == "s" or z == "o" or z == "m" or z == "d" or z == "p":         #since they need two numbers from the user
                x = int(input("Enter first number: "))
                y = int(input("Enter second number: "))
                sum = x + y             #adds the two numbers
                sub = x - y             # subtracts second number from first number
                mul = x * y             # multiply the two numbers
                power = pow(x,y)        # raises first number to the power of second number
                
                
                if z == "s":            #if user wants addition
                    print(sum)
                    operation = False   #to leave the loop after printing the result
                elif z == "o":          #if user wants subtraction
                    print(sub)
                    operation = False
                elif z == "m":          #if user wants multiplication
                    print(mul)
                    operation = False
                elif z == "p":          #if user wants the power function
                    print(power)
                    operation = False
                elif z == "d":          #if user wants division
                    if y == 0:
                        print("The denominator can't be zero")
                        break
                    else:  
                        div = x / y
                        print(div)
                        operation = False

            elif z == "r" or z == "i" or z == "c":
                x = int(input("Enter the number: "))
                root = math.sqrt(x)     #to find square root
                sin = math.sin(x)       #to find the sine function
                cos = math.cos(x)       #to find the sine function
                
                if z == "r":            #if user wants square root
                    print(root)
                    operation = False
                elif z == "i":          #if user wants sine function
                    print(sin)
                    operation = False
                elif z == "c":          #if user wants ci=osine function
                    print(cos)
                    operation = False
                
    elif a == "n":                      #if user wants to end the calculator
        calci = False
    else:
        print("Please enter a valid option")        #if user enters any other operation choice
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        