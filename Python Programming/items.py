#!/usr/bin/ env python3

#This is a python code to combiee two modules together
#Date : 25th April 2024
#Author : Emmanuel Odongo
#Email address : itsmeemmanuel74@gmail.com

import cars
import smartphone
import numpy
car = input("Enter your car model: ")

if car == "Toyota":
    cars.Toyota()
elif car == "Nissan":
    cars.Nissan()
elif car == "Subaru":
    cars.Subaru()
elif car == "LandCruiser":
    cars.LandCruiser()
elif car == "Kia":
    cars.Kia()
elif car == "Mercedes":
    cars.Mercedes()
elif car == "Hyundai":
    cars.Hyundai()
else:
    print("Car is not in our database")

phone = input("Enter your phone brand: ")
if phone == "Vivo":
    smartphone.Vivo()
elif phone == "Huawei":
    smartphone.Huawei()
elif phone == "Nothing":
    smartphone.Nothing()
elif phone == "Cubot":
    smartphone.Cubot()
elif phone == "Tecno":
    smartphone.Tecno()
elif phone == "Samsung":
    smartphone.Samsung()
elif phone == "Redmi":
    smartphone.Redmi()
else:
    print("Phone is not in database")











