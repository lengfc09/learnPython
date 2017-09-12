#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 23:37:18 2017
TODO:
@author: BenMac
"""

import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# from scipy import *

mysq = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def findmaxsq(sq):
    maxsum = 0
    for i in range(len(sq)):
        for j in range(len(sq) - i):
            temp = sum(sq[i:i + j])
            if temp > maxsum:
                maxsum = temp
                rst = sq[i:i + j]
    print("found")
    return rst


# print(findmaxsq(mysq))
x = 100.00000000000
# add one sentece here
# add one more
