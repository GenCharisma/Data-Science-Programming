# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 21:36:34 2021

"""

numbers = list(map(str, input("Enter Four Numbers : ").split()))
newnumbers = 0
ax = 0
for a in numbers:
    bx = 0
    for b in numbers:
        cx = 0
        for c in numbers:
            dx = 0
            for d in numbers:
                if ax != bx and ax != cx and ax != dx and bx != cx and bx != dx and cx != dx:
                    converter = int(a+b+c+d)
                    if converter > newnumbers:
                        newnumbers = converter
                dx = dx + 1
            cx = cx + 1
        bx = bx + 1
    ax = ax + 1
    
print(newnumbers)

