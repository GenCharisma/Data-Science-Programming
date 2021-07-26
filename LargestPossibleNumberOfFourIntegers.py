# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 21:36:34 2021

"""

numbers = list(map(str, input("Enter Four Numbers : ").split()))

for a in numbers:
    for b in numbers:
        for c in numbers:
            for d in numbers:
                if (a != b and a != c and a != d and b != c and b != d and c != d):
                    a+b+c+d
                    print(a+b+c+d)

