# ctx.py

with open("ctx.py") as f:
    pass

# with ctx() as x:
#   pass

# x=ctx().__enter__()
# try:
#   pass
# finally:
#   x.__exit__()

from sqlite3 import connect
with connect("test.db") as conn:
    cur = conn.cursor()
    try:
        cur.execute("drop table points")
    except:
        pass
    cur.execute("create table points (x int, y int)")
    cur.execute("insert into points (x,y) values(1,1)")
    cur.execute("insert into points (x,y) values({},{})".format(3, 4))
    cur.execute("insert into points (x,y) values(4,5)")
    for row in cur.execute("select x, y from points"):
        print(row)
    cur.execute("drop table points")


# we can create a class to drop the tables for us:

class temtable:
    def __init__(self, cur):
        self.cur = cur
        print("__init__")

    def __enter__(self):
        self.cur.execute("create table points (x int, y varchar(100))")
        print("__enter__")

    def __exit__(self, *args):
        self.cur.execute("drop table points")
        print("__exit__")


with connect("test.db") as conn:
    cur = conn.cursor()
    with temtable(cur):
        # initiate , then enter, then exit
        cur.execute("insert into points (x,y) values(1,1)")
        cur.execute("insert into points (x,y) values({},'{}')".format(3, "test"))
        cur.execute("insert into points (x,y) values(4,5)")
        for row in cur.execute("select x, y from points"):
            print(row)
