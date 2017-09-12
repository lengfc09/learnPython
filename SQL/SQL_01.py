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
#             print(row)


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
        print(row)
    print("-----------------")
    # for row in cur.execute("select distinct prod_name from products"):
    #     print(row)
    # print("-----------------")
    for row in cur.execute("select prod_name from products limit 5"):
        print(row)
    print("-----------------")
    for row in cur.execute("select prod_name from products limit 5 offset 5"):
        print(row)
    print("-----------------")

    # sorting Data
    for row in cur.execute("select prod_name from products "):
        print(row)
    print("-----------------")

    for row in cur.execute("select * from products order by prod_name and prod_price"):
        print(row)
    print("-----------------")

    for row in cur.execute("select * from products order by  prod_price DESC"):
        print(row)
    print("-----------------")

    # filtering Data
    for row in cur.execute("select * from products where  prod_price>3"):
        print(row)
    print("-----------------")
    # oder by must be after where
    for row in cur.execute("select * from products where  prod_price>3 order by prod_price"):
        print(row)
    print("-----------------")

    # is Null, <>, !=,>

    # Advanced Data Filtering
    # in （list of options）
    for row in cur.execute("select * from products where  prod_name in  ('yue','david') order by prod_price"):
        print(row)
    print("-----------------")
    # not
    for row in cur.execute("select * from products where  not prod_name in  ('yue','david') order by prod_price"):
        print(row)
    print("-----------------")

    # Wildcards filtering
    # % wildcard: any number of any characters
    for row in cur.execute("select * from products where  prod_name like 'y%' order by prod_price"):
        print(row)
    print("-----------------")
# _ wildcard: one single characters
    for row in cur.execute("select * from products where  prod_name like 'y__' order by prod_price"):
        print(row)
    print("-----------------")
