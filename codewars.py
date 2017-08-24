# codewars.py
# Q1
# def persistence(n):
#     num = len(str(n))
#     count = 0
#     while num > 1:
#         dd = 1
#         count = count + 1
#         for _ in str(n):
#             dd = dd * int(_)
#         n = dd
#         num = len(str(n))
#     return count
# print(persistence(39))

# Q2

# def get_sum(a,b):
#     import numpy as np
#     a,b=min(a,b),max(a,b)
#     return sum(np.arange(a,b+1,1))

# Q3


# def remove_smallest(numbers):
#     if numbers == []:
#         return []
#     else:
#         dd = 0
#         ss = numbers[0]
#         for i, num in enumerate(numbers):
#             if num < ss:
#                 dd = i
#                 ss = num
#         numbers.pop(dd)
#         return numbers

# print(remove_smallest([]))
# None != []


# print(remove_smallest([5, 4, 2, 1, 2]))


# Q4
# def high_and_low(numbers):
#     str1 = numbers.split(" ")
#     numbers = []
#     for _ in str1:
#         numbers.append(int(_))
#     mmin = min(numbers)
#     mmax = max(numbers)
#     return "{} {}".format(mmax, mmin)

# print(high_and_low("34 324 234"))

# Q5
# def toJadenCase(string):
#     str1=string.split(" ")
#     str2=""
#     for _ in str1:
#         str2+=_.capitalize()+" "
#     return str2.rstrip(" ")
# # string does not support item assignment
# str.rstrip()


# Q6
# def unique_in_order(iterable):
#     lls=[]
#     for _ in iterable:
#         if _ not in lls:
#             lls.append(_)
#         elif _ !=lls[-1]:
#             lls.append(_)
#     return lls


# Q7
# def getr(num):
#     num = int(num)
#     # print(num)
#     res = 0
#     for i in range(num + 1):
#         res += i**3
#     return res


# def find_nb(m):
#     n = int(m**(1 / 3)) + 1
#     while getr(n) < m:
#         n = n * 2
#     res = 0
#     num1, num2 = 1, n

#     while (num1 + 1) < num2:
#         res1 = 0
#         res2 = 0
#         mid = int((num1 + num2) / 2)
#         # print("mid-->", mid)
#         if getr(num1) == m:
#             return num1
#         elif getr(num2) == m:
#             return num2

#         if getr(mid) < m:
#             num1, num2 = mid, num2
#             # print(num1, num2)
#         elif getr(mid) > m:
#             num1, num2 = num1, mid
#             # print(num1, num2)
#         else:
#             print("found")
#             return mid
#     if getr(num1) != m and getr(num2) != m:
#         return -1

# print(find_nb(40539911473216))
# print(getr(2022))


# Q8
# recipe = {"flour": 500, "sugar": 200, "eggs": 1}
# available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}


# def cakes(recipe, available):
#     # import math
#     # dd = []
#     # for key in recipe:
#     #     try:
#     #         dd.append(math.floor(available[key] / recipe[key]))
#     #     except:
#     #         dd.append(0)
#     # return min(dd)
#     return int(min(available.get(k, 0) / v for k, v in recipe.items()))

# print(cakes(recipe, available))
# # how to read the key and the value of a dictionary
# for k, v in recipe.items():
#     print(k, v)

# # try to get a value from a key in a dict, with a default given
# print(available.get("plp", 0))

# list.count()
# def delete_nth(order,max_e):
#     ls=[]
#     for item in order:
#         if ls.count(item)<max_e:
#             ls.append(item)
#     return ls


# Q9: " ".join(),  str.isalpha()
# def pig_it(text):
#     lst = text.split()
#     return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])


# print(" ".join(["sdfsd", "sdf"]))
# print("dsaf!".isalpha())

# # Q10
# def find_even_index(arr):
#     dd=-1
#     for i,_ in enumerate(arr):
#         if sum(arr[0:i])==sum(arr[i+1:]):
#             dd=i
#             break
#     return dd

# def move_zeros(array):
#     arr = []
#     while 0 in array:
#         array.remove(0)
#         arr.append(0)
#     array.extend(arr)
#     return array

# # Q11
# def dig_pow(n, p):
#     arr=str(n)
#     msum=0
#     for i,_ in enumerate(arr):
#         msum+=int(_)**(p+i)
#     if msum%p==0:
#         return msum/p
#     else:
#         return -1

# # Q12

# def duplicate_count(text):
#     text2 = []
#     for _ in text:
#         if not _ in text2:
#             text2.append(_)
#     dd = 0
#     for _ in text2:
#         if text.count(_) >= 2:
#             dd = dd + 1
#     return dd


# print(duplicate_count("indivisibilityy"))
# llist = [1, 2, 3]
# print(1 in llist)

# # Q13
# def scramble(s1, s2):
#     for _ in s2:
#         if s1.count(_) < s2.count(_):
#             return False
#     return True


# print(scramble('scriptjava', 'javascript'))
# print(scramble('scriptingjava', 'javascript'))

# # Q14
# def order_weight(strng):
#     strng = strng.split(" ")
#     strng = sorted(strng, key=lambda d: sum([int(i) for i in d])+int(d)*10**(-8))
#     return " ".join(strng)
# def order_weight(strng):
#     strng = strng.split(" ")
#     strng = sorted(strng, key=lambda d: sum([int(i) for i in d]))
#     return " ".join(strng)


# print(order_weight("103 123 4444 99 2000"))
