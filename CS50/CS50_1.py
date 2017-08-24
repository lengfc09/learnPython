#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 23:37:18 2017
TODO:
@author: BenMac
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import *

import CS50_2

# s = test2.get_string()
# ss2 = input("name: ")
# print("hello, {}".format(s))
# print("hello, {}".format(ss2))
print("{:.55f}".format(1 / 10))
import sys
for i in range(len(sys.argv)):
    print(sys.argv[i])

# print("sd f ")
# print("sd f ".strip())
# print("sdf\n", end="")
# print("sdf\n".rstrip("\n"), end="")
# print()
print("dsfsdf".find("f", 4))

import random
# random.choice: return an element
# random.choices: return a subset
x, y = random.choice([(0, 1), (3, 4)])
# x = random.choice((-1, 1))
print(x)

# an experiment
S = 0
PP = list()
for j in range(1000):
    P = 0
    N = 0
    for i in range(1000):
        x = random.choice([1, -1])
        if x == 1:
            P += 1
        else:
            N += 1
    PP.append(P)

plt.hist(PP, bins=30, edgecolor="#000000")
plt.show()
