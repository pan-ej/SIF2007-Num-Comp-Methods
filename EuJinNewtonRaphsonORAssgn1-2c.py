# -*- coding: utf-8 -*- 
"""
SIF2007 Assignment 1
Pan Eu Jin 23052342
2.(c) Newton-Raphson Method
"""

#Note:If the table does not display correctly, please resize the console so that it fits the table
import numpy as np
import matplotlib.pyplot as mpl

#Newton-Raphson method for f(x)=e^x - 2 using x0=0
def f(x):
    return np.exp(x) - 2                        #Change with Q
def df(x):
    return np.exp(x)                            #Change with Q
def NR(x):
    return x-f(x)/df(x)
def calc_err(x1,x0):
    return abs(x1-x0)
    
#Starting variables
x0 = 0                                          #Change with Q
x1 = NR(x0)
err = calc_err(x1, x0)
i = 0

# Prepare table header
print('\033[4m|  i  |      x_i      |     x_i+1     |      err      |\033[0m')

# Loop until error is below threshold
while err > 1E-6:                             #Change with Q
    x1 = NR(x0)
    err = calc_err(x1, x0)
    print('| ', i, ' | ', f"{x0:.5e}", ' | ', f"{x1:.5e}", ' | ', f"{err:.5e}", ' |')
    mpl.plot(x0,f(x0),'bo',markersize=9)
    x0 = x1
    i += 1
print('Approx. root =', f"{x0:.5e}")
mpl.plot(x0, f(x0), 'm*', markersize=9)

#Plotting of graph
x=np.linspace(-0.5, 1.5, 100)                #Might need tweaking
mpl.plot(x, f(x), 'k--')
mpl.xlabel('x')
mpl.ylabel('f(x)')
mpl.show()