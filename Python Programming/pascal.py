#!/usr/bin/ env python3

#This is a python code to create Pascal's triangle
#Date : 25th April 2024
#Author : Emmanuel Odongo
#Email address : itsmeemmanuel74@gmail.com



#introduce the library factorial
from math import factorial
#enter the number that serves as the exponent
x = int(input("Enter your number: "))
#iterate upto specified integer
for i in range(x):
    print(' ' * (x-1), end = ' ')
    #computation
    coefficient = 1
    for k in range(0, i+1):
        print(coefficient, end = ' ')
        coefficient = coefficient * (i - k) // (k + 1)  
    print()

   

















