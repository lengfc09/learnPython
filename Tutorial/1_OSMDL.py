def myfun(x):
    return x * 3


from numpy import *
import time
letters = ["a", "b", "c"]
target = "c"
dd = False
for letter in letters:
    if target == letter:
        print("found")
        dd = True
        break

if not dd:
    print("not found")

# x = input()
# print(x)

f = open("smt.txt")
for line in f:
    print(line)

f.close()
try:
    print(int("3"))
except:
    print("wrong")
else:
    print("right")
finally:
    print("alwasy show")


import os
print(os.getcwd())
# print(os.stat("test.py"))
print(os.path.basename('/temp/test.txt'))
print(os.path.dirname('temp/test.txt'))
print(os.path.split('/temp/test.txt'))
print(os.path.splitext('/temp/test.txt'))

print(os.listdir())

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    print(file_name, "and ", file_ext)
print("and ")
# remove the white space outside
print(" amd ".strip(), end="tsdf")
