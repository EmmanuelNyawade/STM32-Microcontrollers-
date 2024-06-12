#!/usr/bin/ env python3

#This is a python code to  demonstrate tuple and their formatting
#Date : 25th April 2024
#Author : Emmanuel Odongo
#Email address : itsmeemmanuel74@gmail.com





# tuples are immutable lists meaning items cannot be added or removed from it
vegs = ("Kales", "Sukumawiki", "Cabbage", "Potatoes", "Cassava", "Pomegranate",)
for veg in vegs:
    print(veg)

print(vegs[4])
print(type(vegs))

#converting a tuple into a list
new_vegs = list(vegs)
print(new_vegs)
fruits = ("Bananas", "Oranges", "Apples")
print(len(vegs))
print(max(vegs))
print(min(vegs))

rev = vegs[::-1]
print(rev)


#