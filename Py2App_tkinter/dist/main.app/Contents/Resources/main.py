#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    # for Python2
    from Tkinter import *  # notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *


def get_sum(event):
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())
    sumEntry.insert(0, num1 + num2)


root = Tk()
Label(root, text="这是个测试").pack(side=TOP)
num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

Label(root, text="+").pack(side=LEFT)


num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

equalButton = Button(root, text="=")
equalButton.bind("<Button-1>", get_sum)
equalButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)


root.mainloop()
