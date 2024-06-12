#!/usr/bin/ env python3

#This is a python code to  calculate a person's tax
#Date : 25th April 2024
#Author : Emmanuel Odongo
#Email address : itsmeemmanuel74@gmail.com



salary = int(input("Enter your income: "))
if  salary < 0:
    print("Salary cannot be negative")
elif salary <50000:
    tax = 15/100 * salary
    print("You should pay Ksh {} as tax".format(tax)) 
elif salary > 50000 and salary <= 70000:
    tax = 18/100 * salary
    print("You should pay Ksh {} as tax".format(tax))
else:
    tax = 20/100 * salary
    print("You should pay Ksh {} as tax".format(tax))
