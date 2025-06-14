# -*- coding: utf-8 -*-
"""
SIF2007 Assignment 2
Pan Eu Jin 23052342
1.(b) Piecewise Linear Approximation
"""

import numpy as np
import matplotlib.pyplot as plt

# Define actual function
def f(x):
    return np.exp(x)

# Nodes
x0, x1, x2 = 0, 0.5, 1
c0, c1, c2 = f(x0), f(x1), f(x2)

# Define piecewise functions including gradient calculations
def q1(x):
    return (c1-c0)/(x1-x0)*(x-x1)+c1

def q2(x):
    return (c2-c1)/(x2-x1)*(x-x2)+c2

# Create x-values for the segments
x_vals_1 = np.linspace(x0, x1, 100)
x_vals_2 = np.linspace(x1, x2, 100)

# Plot actual and piecewise functions, and nodes
plt.plot(np.linspace(0, 1, 200), f(np.linspace(0, 1, 200)), label='f(x) = eˣ', color='blue')
plt.plot(x_vals_1, q1(x_vals_1), '--r', label='q(x) in interval [0, 0.5]')
plt.plot(x_vals_2, q2(x_vals_2), '--g', label='q(x) in interval [0.5, 1]')
plt.plot([x0, x1, x2], [c0, c1, c2], 'ko', label='Nodes')

# Plot settings
plt.title("Piecewise Linear Approximation of f(x)=eˣ")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()