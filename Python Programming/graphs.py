#!/usr/bin/ env python3

#This is a python code to create a trigonometric graph of sine and cosine of values in a specified range
#Date : 25th April 2024
#Author : Emmanuel Odongo
#Email address : itsmeemmanuel74@gmail.com


import numpy as np
import matplotlib.pyplot as plt
from math import pi
x = np.arange(-2*pi, 2*pi, 1/24*pi)

y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x , y1, color = 'purple')
plt.plot(x , y2, color = 'maroon')
plt.xlabel("radians")
plt.ylabel("f(x)")
plt.legend(['sin(x)','cos(x)'])
plt.xlim(-2*pi,2*pi)
plt.title("Trigonometric graph for the sine and cosine of angle x")
plt.show()
