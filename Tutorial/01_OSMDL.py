def myfun(x):
    return x * 3


from numpy import *
import time
# x = input()
# print(x)
# try syntax:
# try:
#     print(int("3"))
# except:
#     print("wrong")
# else:
#     print("right")
# finally:
#     print("alwasy show")


import os
print(os.getcwd())
# print(os.stat("test.py"))
print(os.path.basename('/temp/test.txt'))
print(os.path.dirname('temp/test.txt'))
print(os.path.split('/temp/test.txt'))
print(os.path.splitext('/temp/test.txt'))

print(os.listdir())

# Rename the files

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    if file_name[0].isdigit():
        print(file_name, "and ", file_ext)
        num, *others = file_name.split("_")
        new_name = file_name.replace(num, num.zfill(2))
        os.rename(f, new_name + file_ext)
