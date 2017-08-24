from sqlite3 import connect


# class temtable:
#     def __init__(self, cur):
#         self.cur = cur
#         print("__init__")

#     def __enter__(self):
#         self.cur.execute("create table points (x int, y varchar(100))")
#         print("__enter__")

#     def __exit__(self, *args):
#         self.cur.execute("drop table points")
#         print("__exit__")


# with connect("test.db") as conn:
#     cur = conn.cursor()
#     with temtable(cur):
#         # initiate , then enter, then exit
#         cur.execute("insert into points (x,y) values(1,1)")
#         cur.execute("insert into points (x,y) values({},'{}')".format(3, "test"))
#         cur.execute("insert into points (x,y) values(4,5)")
#         for row in cur.execute("select x, y from points"):
#             print(*row)


import random
pid = ["BNBG{}".format(i) for i in range(10)]
names = ["peter", "david", "slong", "yue"]
pnm = [random.choice(names) for i in range(10)]
prc = [random.uniform(-4, 10) for i in range(10)]

with connect("sample.db") as conn:
    cur = conn.cursor()
    try:
        cur.execute("create table products (prod_id varchar(100), prod_name varchar(100), prod_price float)")
    except:
        cur.execute("drop table products")
        cur.execute("create table products (prod_id varchar(100), prod_name varchar(100), prod_price float)")
    # cur.execute("insert into products (prod_id,prod_name,prod_price) values('BNBG01','Fish bean bag toy',3.49)")
    for i in range(10):
        cur.execute("insert into products (prod_id,prod_name,prod_price) values('{}','{}',{})".format(pid[i], pnm[i], prc[i]))
    for row in cur.execute("select * from products "):
        print(*row)
    print("-----------------")
    # for row in cur.execute("select distinct prod_name from products"):
    #     print(*row)
    # print("-----------------")
    for row in cur.execute("select prod_name from products limit 5"):
        print(*row)
    print("-----------------")
    for row in cur.execute("select prod_name from products limit 5 offset 5"):
        print(*row)
    print("-----------------")

    # sorting Data
    for row in cur.execute("select prod_name from products "):
        print(*row)
    print("-----------------")

    for row in cur.execute("select * from products order by prod_name and prod_price"):
        print(*row)
    print("-----------------")

    for row in cur.execute("select * from products order by  prod_price DESC"):
        print(*row)
    print("-----------------")

    # filtering Data
    for row in cur.execute("select * from products where  prod_price>3"):
        print(*row)
    print("-----------------")
    # oder by must be after where
    for row in cur.execute("select * from products where  prod_price>3 order by prod_price"):
        print(*row)
    print("-----------------")

    # is Null, <>, !=,>

    # Advanced Data Filtering
    # in （list of options）
    for row in cur.execute("select * from products where  prod_name in  ('yue','david') order by prod_price"):
        print(*row)
    print("-----------------")
    # not
    for row in cur.execute("select * from products where  not prod_name in  ('yue','david') order by prod_price"):
        print(*row)
    print("-----------------")

    # Wildcards filtering
    # % wildcard: any number of any characters
    for row in cur.execute("select * from products where  prod_name like 'y%' order by prod_price"):
        print(*row)
    print("-----------------")
# _ wildcard: one single characters
    for row in cur.execute("select * from products where  prod_name like 'y__' order by prod_price"):
        print(*row)
    print("-----------------")
#[] wildcard: one of the given characters
    # for row in cur.execute("select * from products where  prod_name like '[y]%' order by prod_price"):
    #     print(*row)
    # print("-----------------")

# Creating Calculated fields
# ||  join syntax
    for row in cur.execute("select prod_name || ' ( ' ||prod_id||' )'  from products order by prod_price"):
        print(*row)
    print("-----------------")
# RTRIM: trims all space from the right of a value
# LTRIM()： left trim；trim(): trim all; Like rtrip()
    for row in cur.execute("select RTRIM(prod_name) || '(' ||RTRIM(prod_id)  ||')'  from products order by prod_price"):
        print(*row)
    print("-----------------")

# AS: give a column name to the calculated column
    for row in cur.execute("select RTRIM(prod_name) || '(' ||RTRIM(prod_id)  ||')' as prod_tt from products order by prod_price"):
        print(*row)
    print("-----------------")
# mathematical calculation
    for row in cur.execute("select prod_price*3 as expanded_price from products order by prod_price"):
        print(*row)
    print("-----------------")
# cannot use the calculated field later
    try:
        for row in cur.execute("select expanded_price from products order by prod_price"):
            print(row)
        print("-----------------")
    except:
        print("FOOL!")
# using data manipulation functions
## e.g. Rtrim()
    for row in cur.execute("select date()"):
        print(*row)
    print("-----------------")

# Using Functions
# Most SQL implementations support the following types of functions:
# • Text functions are used to manipulate strings of text (for example, trimming or padding values
# and converting values to upper and lowercase).
# • Numeric functions are used to perform mathematical operations on numeric data (for example,
# returning absolute numbers and performing algebraic calculations).
# • Date and time functions are used to manipulate date and time values and to extract specific
# components from these values (for example, returning differences between dates, and checking
# date validity).
# • System functions return information specific to the DBMS being used (for example, returning
# user login information).
# In the last lesson, you saw a function

# TEXT manipulation functions
# upper(), substr(str,start,number),length()
    for row in cur.execute("select date(),upper('test')"):
        print(row)
    print("-----------------")
    for row in cur.execute("select date(),substr('test',1,2),length('test2')"):
        print(row)
    print("-----------------")
# Date manipulation functions
# TODO
# numeric manipulation functions
## abs(), cos(),exp(),PI(),SIN(),SQRT(),TAN()

# Summarizing Data
# AVG(),COUNT(),MAX(),MIN(),SUM()
    for row in cur.execute("select avg(prod_price),count(prod_price) from products"):
        print(row)
    print("-----------------")
# count(*) counts all the rows, whether it is null
# count(culumn) return the rows of Non-Nulls

# Grouping Data
    for row in cur.execute("select prod_name,count(*) from products GROUP BY prod_name"):
        print(row)
    print("-----------------")
# filtering groups
# where filters specific rows, not groups; what if we want to filter after "Group by"
    for row in cur.execute("select prod_name,count(*) from products GROUP BY prod_name having count(*)>=2"):
        print(row)
    print("-----------------")

# Conclusion:
# select column from table where (row-level filtering) group by (group specification) having (Group-level filtering)  order by ...by

# working with subqueries
#     SELECT cust_name,
# cust_state,
# (SELECT COUNT(*)
# FROM Orders
# WHERE Orders.cust_id = Customers.cust_id) AS orders
# FROM Customers
# ORDER BY cust_name;

