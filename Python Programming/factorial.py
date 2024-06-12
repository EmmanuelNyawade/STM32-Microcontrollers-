#!/usr/bin/ env python3

#This is a python code to  calculate factorials of numbers
#Date : 25th April 2024
#Author : Emmanuel Odongo
#Email address : itsmeemmanuel74@gmail.com



#factorial using for loop
def factorial(n):
    n_fact = 1
    for i in range(1,n+1):
        if n == 0:
            return 1
        elif  n >= 1:
            n_fact = n_fact * n
            n = n - 1                    
    return n_fact

print(factorial(8))


#factorial using while loop

def fact(k):
    factor = 1
    if k == 0:
        return 1
    while k >= 1:
        factor = factor * k
        k = k - 1
    return factor    
print(fact(5))







































