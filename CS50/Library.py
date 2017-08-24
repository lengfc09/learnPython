# Library.py


class Base:
    def foo(self):
        return self.bar()


x = [1, 2, 3, 4, 5]
y = ["bob", "steve", "sherry", "cai", "yue"]

for xx, yy in zip(x, y):
    print(xx, yy)

dd = zip(x, y)
dd2 = dict(dd)


# Top-lever syntax, function <->underscorred method __call__


def add1(x, y):
    return x + y


class Adder:
    # def __init__(self, x):
    #     print(x)
    def __call__(self, x, y):
        return x + y


add2 = Adder()
print(add2(3, 5))


class mylist:
    def __init__(self, *lls):
        self.lls = list(lls)

    def __call__(self, n):
        return self.lls[n + 1]


print(x[0], x[1])
mlls = mylist(*x)
print(mlls(0))
