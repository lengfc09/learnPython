test = {"sadf": 13, "sdfdf": 234, "sdfj": 234}
print(test["sadf"])


def my_logger(original_function):
    import logging
    import time
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info("ran with args: {}, and kwargs: {}".format(args, kwargs))
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        logging.info("{} ran in: {} seconds".format(original_function.__name__, t2))
        return result
    return wrapper

    # x = input("this is part of a exciting expriment")
x = 3


@my_logger
def myfun():
    print(x)

myfun()
colors = ["oringe", "green", "black", "blue"]
names = ["Yang", "CaiYue", "Ding", "Han"]

for color in colors:
    print(color)

for color in reversed(colors):
    print(color)

for i, color in enumerate(colors):
    print(i, "-->", color)
    print(i, "-->", colors[i])

mydict = {}

for name, color in zip(names, colors):
    print(name, "-->", color)
    mydict[name] = color

print(mydict)
for k in mydict:
    print(k)

mydict2 = dict(zip(names, colors))
print(mydict2)
