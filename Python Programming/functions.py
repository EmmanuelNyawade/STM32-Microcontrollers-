#!/usr/bin/ env python3

#This is a python code to demonstrate functions
#Date : 25th April 2024
#Author : Emmanuel Odongo
#Email address : itsmeemmanuel74@gmail.com



# a function is a block of code executed together
# function declaration
def print_info(name, age, fav_color, fav_fruit):
    print(name)
    print(age)
    print(fav_color)
    print(fav_fruit)
#function call
print_info("Emmanuel Odongo", "17", "Magenta", "Apples" )
print("\n")
print_info("Gabriel Opiyo", "17", "Green", "Grapes")



max_number = int(input("Enter the maximum number for your operation: "))
def sum_numbers(max_number):
    sum = 0
    for i in range(0,max_number):
        sum = sum  + i
    print(sum)
sum_numbers(max_number)





























