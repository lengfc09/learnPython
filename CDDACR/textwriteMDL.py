print("地方f")
import matplotlib.pyplot as plt
import pandas as pd
import os
xdsf = 3

xdsf = xdsf + 1
print(os.getcwd())
# os.chdir("C:/Users/0100061925")
# print(os.getcwd())
# for path, dirname, filename in os.walk(os.getcwd()):
#     print("path", path)
#     print("Dirs:", dirname)
#     print("filename:", filename)

with open("mytxt.txt", 'w') as f:
    n = 1
    while n < 10:
        f.write("%d) this is great\n" % n)
        f.write("{}) this is great \n".format(n))
        n = n + 1

with open('mytxt.txt', 'r') as rf:
    f_line = rf.readline()
    print(f_line, end='')
