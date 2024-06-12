#!/usr/bin/ env python3

#This is a python code to  create a dialog box to calculate the sum of numbers
#Date : 25th April 2024
#Author : Emmanuel Odongo
#Email address : itsmeemmanuel74@gmail.com


from tkinter import *
def add():
    a = int(entry1.get())
    b = int(entry2.get())
    sum = a + b
    label3.config(text="Your result is {}".format(sum))

window = Tk()
window.geometry = ("650x650")
window.title = ("Sum Calculator")

label1 = Label(window,
                text="Enter first number:",
                font= ("Raleway",20),
                )
label2 = Label(window,
               text= "Enter second number:",
               font =("Raleway",20)
               )
label3 = Label(window,
               text = "Your result is",
               font = ("Raleway",20)

)
label1.place(x = 10, y = 15)
label2.place(x = 10, y = 80) 
label3.place(x = 120, y = 120)

button = Button(text= "Get Result",
                command= add,
                font= ("Raleway",10),


)
button.place(x = 160, y = 160)
 
entry1 = Entry(window,
              font= ("Raleway",10),
              )
entry2 = Entry(window,
               font = ("Raleway",10),
               )
entry1.place(x = 280, y = 25)
entry2.place(x = 280, y = 92)


window.mainloop()
