#!/usr/bin/ env python3

#This is a python code to demonstrate creation of lists
#Date : 25th April 2024
#Author : Emmanuel Odongo
#Email address : itsmeemmanuel74@gmail.com



#lists are like dynamic arrays in other languages
#they are mutable and sequenced data types
#when we say they are mutable - it means we can change the contents of list values
numbers = [1, 4, 9, 16, 25, 36]
print(numbers)
print(type(numbers))
# functions related to lists
# 1. append() - adds items to the end of the list

numbers.append(88)
print(numbers)

# 2. extend() - adds an item of one list to another list

odd = [7 ,13 ,33, 99, 67, 45]
numbers.extend(odd)
print(numbers)

# 3. index() - it returns the position of the item in the list

print(numbers.index(13))


# 4. list[] - returns the item of the specified index

print(numbers[6])

# 5. insert(index, value) - inserts an item at the specified index

numbers.insert(5,21)
print(numbers)

# 6. pop() - removes an item at the specified index from the list
numbers.pop(2)
print(numbers)

# 7. remove()- removes the first occurence of the value from the list
numbers.remove(99)
numbers.remove(45)
numbers.remove(67)
print(numbers)

#8. reverse()- reverses the order of the list
numbers.reverse()
print(numbers)

#9. count()- counts the occurence of a value
numbers.append(21)
print(numbers.count(21))

























