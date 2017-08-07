import time
import random
names = ["peter", "david", "slong", "yue"]
cities = ["shanghai", "london", "newyork"]
print(random.choices(names))
# return a subset
# people_num = [1, 2, 3, 4]

# random.choice: return an element
# random.choices: return a subset


def get_people(people_num):
    result = []
    for i in range(people_num):
        people = {
            'ind': i,
            "name": random.choice(names),
            "city": random.choice(cities)
        }
        result.append(people)
    return result


t1 = time.clock()
peopls = get_people(100)
t2 = time.clock()
print(t2 - t1)
print(peopls[55])


# use generator
def gen_people(people_num):
    for i in range(people_num):
        people = {
            'ind': i,
            "name": random.choice(names),
            "city": random.choice(cities)
        }
        yield people

peopls2 = gen_people(100)
print(next(peopls2))
print(next(peopls2))
print(next(peopls2))
print("Transform into list")
ppp = list(peopls2)
print(ppp[0])
# as we can see, next() remove those data which have been read.
print("new Line")
# this will be an error to read the value directly
print(peopls2)
print("New Line")


def getpeoplefromgen(ppls, position):
    for i, people in enumerate(ppls):
        if i == position:
            print("found")
            return people
            break
print(getpeoplefromgen(peopls2, 2))


t1 = time.clock()
peopls = gen_people(100)
t2 = time.clock()
print(t2 - t1)
