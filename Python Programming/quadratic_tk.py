#!/usr/bin/ env python3

#This is a python code to create a dialog box for calculating quadratic expressions
#Date : 25th April 2024
#Author : Emmanuel Odongo
#Email address : itsmeemmanuel74@gmail.com



from tkinter import *
import math
def calculate():
    a = int(entrya.get())
    b = int(entryb.get())
    c = int(entryc.get())
   
    x1 = -b + math.sqrt((b*b)- (4 * a * c))/2 * a
    x2 = -b - math.sqrt((b*b)-(4 * a * c))/2 * a
    label_result.config(text = "Your result is {} and {}".format(x1,x2))


window =  Tk()
window.geometry = ("1000x1000")
window.title = ("Quadratic Calculator")

labela = Label(window,
               font=("Raleway",20),
               text= "Enter the coefficient of x²",
)
labelb = Label(window,
               text = "Enter the coefficient of x",
               font = ("Raleway",20),
               )
labelc = Label(window,
               text = "Enter the constant term",
               font = ("Raleway",20),
)
label_result = Label(window,
                     text = "Result",
                     font = ("Raleway",20),
                     )
labela.place(x = 10,y = 10)
labelb.place(x = 10, y = 40)
labelc.place(x = 10, y = 80)
label_result.place(x = 10, y = 120)

entrya = Entry(window,
               font = ("Raleway",10),
)
entryb = Entry(window,
               font = ("Raleway",10),
               )
entryc = Entry(window,
               font = ("Raleway",10),
               )

entrya.place(x = 320, y = 25 )
entryb.place(x = 320, y = 55 )
entryc.place(x = 320, y = 95)

button = Button(window,
                text = "Get Result",
                font = ("Raleway",10),
                command = calculate,
                )
button.place(x = 120,y = 200)

window.mainloop()
























