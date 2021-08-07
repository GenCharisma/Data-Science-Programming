# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 11:35:45 2021

"""

# HW05:   Problem Solving

# Assume you open your ice cream shop, there are only two types of ice cream, vanilla and strawberry.
# When a box of ice cream is sold, you will get the benefit for $2 for vanilla ice cream
# and $3 for strawberry ice cream. To make the ice cream, the fresh milk is required.
# To make a box of vanilla ice cream requires 0.5 liter and strawberry ice cream requires 0.2 liter.
# You daily order 10 liters of fresh milk.
# To promote your ice cream shop, you give a doll for each ice cream box. The number of dolls,
# that you can give to customers, is 30 dolls per day.
# So, how many boxes of vanilla ice cream and strawberry ice cream
# that you would like to produce to get maximum profit ?
# Use Python to find the answer ; provide solving explanation in PDF file

# xi = the number of ice cream type (1 : vanilla, 2 : strawberry)
#    x1, x2

# Objective
    # max : 2(x1) + 3(x2)
# Contraints
    # Ice Creams Limit : 0.5(x1) + 0.2(x2) <= 10
    # Order Limit      : 1(x1)   + 1(x2)   <= 30
    #                    x1,x2             >= 0

import numpy as np
from scipy.linalg import solve
A = np.array([[0.5,0.2],[1.,1.]])
b = np.array([10.,30.])
x = solve (A,b)
print(x)
xrounded = np.around(x)

print("all vanilla", (2*0) + (3*30))
print("all strawberry",(2*30) + (3*0))
print("Crosspoint", (2*xrounded[0]) + (3*xrounded[1]))

import matplotlib.pyplot as plt
f, ax = plt.subplots()
plt.plot([x[0]],[x[1]],'ro')
plt.plot([20,0],[0,50])
plt.plot([30,0],[0,30])
plt.grid()
ax.set_ylim(bottom=0)
ax.set_xlim(left=0)
#plt.fill_between([20,0], [x[1]], [0,30])
plt.fill_between([0,x[0],20],[30,x[1],0],0, alpha = 0.5)
plt.ylabel('Strawberry')
plt.xlabel('Vanilla')
plt.show()
