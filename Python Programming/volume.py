#!/usr/bin/ env python3

#This is a python code to  calculate the volume of a sphere
#Date : 25th April 2024
#Author : Emmanuel Odongo
#Email address : itsmeemmanuel74@gmail.com



# volume of a sphere
# volume of a cylinder
#surface area of a sphere
#surface area of a cylinder
pi = 3.142
def sph():
   radius = int(input("Enter radius "))
   radius_cube = radius * radius * radius
   sph_vol = 4/3 * pi * radius_cube
   radius_square = radius * radius
   sph_area = 4 * pi * radius_square
   print("Your sphere's surface area is", sph_area)

   print("Your sphere's volume is " ,sph_vol)


def cyl_area_closed():
   radius = int(input("Enter radius"))
   height = int(input("Enter height"))
   d = 2 * radius
   radius_square = radius * radius 
   cyl_area_closed = (2 * pi * radius_square) + (pi * d * height)
   radius_square = radius * radius
   cyl_vol = pi * radius_square
   print("Your cylinder's volume is", cyl_vol)

   print(" Your closed cylinder's surface area is", cyl_area_closed)

def cyl_area_open():
   radius = int(input("Enter radius"))
   height = int(input("Enter height"))
   d = 2 * radius
   radius_square = radius * radius
   cyl_area_open = (pi * radius_square) + (pi * d * height)
   radius_square = radius * radius
   cyl_vol = pi * radius_square
   print("Your cylinder's volume is", cyl_vol)

   print("Your open cylinder's surface area is", cyl_area_open)

def cyl_area_hollow():
   radius = int(input("Enter radius"))
   height = int(input("Enter height"))
   d = 2 * radius
   cyl_area_hollow = pi * d * height
   radius_square = radius * radius
   cyl_vol = pi * radius_square
   print("Your cylinder's volume is", cyl_vol)

   print("Your hollow cylinder's surface area is", cyl_area_hollow)
 
shape = input("Sphere or Cylinder")
if shape == "Sphere":
   sph()
else:  
    if shape == "Cylinder":
        type = input("Is it Hollow, Open or Closed")
        if type == "Hollow":
           cyl_area_hollow()
          
        elif type == "Open":
           cyl_area_open()
          
        elif type == "Closed":
           cyl_area_closed()
           
        else:
           print("Invalid input. Please try again :)")


           
           

        

   

    



