# -*- coding: utf-8 -*-
"""
SIF2007 Assignment 1
Pan Eu Jin 23052342
2.(d) Bisection Method
"""

#Note:If the table does not display correctly, please resize the console so that it fits the table
import numpy as np
import matplotlib.pyplot as mpl

#Bisection method for f(x)=e^x - 2 in interval [0,1]
def f(x):
    return np.exp(x)-2          #Change with Q
def calc_err(a,b):
    return abs(a-b)
def calc_root(a,b):
    return (a+b)/2
    
#Prepare table header
print('\033[4m|  i  |       a       |       b       |      err      |\033[0m')

#Starting variables
i=0
a=0                             #Change with Q
b=1                             #Change with Q
root=calc_root(a,b)
err=calc_err(a,b)

#Range of graph
x = np.linspace(a, b, 100)
mpl.plot(a,f(a),'bo',markersize=9)
mpl.plot(b,f(b),'rd',markersize=9)

#Print initial variables
print('| ',i,' | ',f"{a:.5e}",' | ',f"{b:.5e}",' | ',f"{err:.5e}",' |')

#Loop until error is below threshold
while err>10E-6:                 #Change with Q
    c=(a+b)/2
    test=f(a)*f(c)
    if test<0:
        b=c
    elif test>0:
        a=c
    else:
        print('Real root found!')
        break
    root=calc_root(a,b)
    err=calc_err(a,b)
    i=i+1
    print('| ',i,' | ',f"{a:.5e}",' | ',f"{b:.5e}",' | ',f"{err:.5e}",' |')
    mpl.plot(a,f(a),'bo',markersize=9)
    mpl.plot(b,f(b),'rd',markersize=9)
mpl.plot(root,f(root),'m*',markersize=9)
print('Approx. root =',f"{root:.5e}")   

#Plotting of graph
mpl.xlabel('x')
mpl.ylabel('f(x)')
mpl.plot(x,f(x),'k--')
mpl.show()
