# f = open("mytxt.txt", 'r')
# print(f.name)
# f.close()
# with open("mytxt.txt", 'r') as f:
#     # f_content = f.read()
#     f_line = f.readline()
# with open("mytxt.txt", 'r') as f:
#     for line in f:
#         print(line, end="")

# with open("mytxt.txt", 'r') as f:
#     ff = f.read(10)
#     print(ff)
#     print(f.tell())
#     if f.tell() != 0:
#         f.seek(0)
#         ff = f.read(10)
#         print(ff)
with open("mytxt_copy.txt", 'w') as wf:
    with open("mytxt.txt", "r") as rf:
        for line in rf:
            wf.write(line)
