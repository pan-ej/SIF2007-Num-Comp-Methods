# -*- coding: utf-8 -*-
"""
SIF2007 Examination 1
Pan Eu Jin 23052342
1.(c) Secant Method
"""

#Note:If the table does not display correctly, please resize the console so that it fits the table
import numpy as np
import matplotlib.pyplot as mpl

#Secant method for f(x)=sin(x) - x/2 with x0 = 0, x1 = 2
def f(x):
    return np.sin(x)-x/2
def calc_err(x0, x1):
    return abs(x1 - x0)
def secant(x0, x1):
    return x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    
#Prepare table header
print('\033[4m|  i  |     x_i-1     |      x_i      |     x_i+1     |      err      |\033[0m')

#Starting variables
i = 0
x0 = 0  #Change with Q
x1 = 2              #Change with Q
err = 1

#Range of graph
x = np.linspace(x0, x1, 100)
mpl.plot(x0, f(x0), 'bo', markersize=9)
mpl.plot(x1, f(x1), 'rd', markersize=9)

#Loop until error is below threshold
while err > 1E-6:
    x2 = secant(x0, x1)
    err = calc_err(x2, x1)
    print('| ',i,' | ',f"{x0:.5e}",' | ',f"{x1:.5e}",' | ',f"{x2:.5e}",' | ',f"{err:.5e}",' |')
    i += 1
    mpl.plot(x2,f(x2),'gx', markersize=9)
    x0, x1 = x1, x2
mpl.plot(x2, f(x2), 'm*', markersize=9)
print('Approx. root =', f"{x2:.5e}")

#Plotting of graph
mpl.plot(x, f(x), 'k--')
mpl.xlabel('x')
mpl.ylabel('f(x)')
mpl.show()