#!/usr/bin/ env python3

#This is a python code to show formatting of lists
#Date : 25th April 2024
#Author : Emmanuel Odongo
#Email address : itsmeemmanuel74@gmail.com


students = ["Joe", "Derrick", "Ishmael", "Philip", "Antony", "Benjamin"]
"""
count = 0

for student in students:
    name = input("Enter name of the student: ")
    students.append(name)
    count +=1

    if count == 5:
        break
  

for student in students:
    print(student)
"""
students.sort()
print(students)
students.reverse()
print(students)
students[2] = "Peter"
print(students)
students.pop()
print(students)