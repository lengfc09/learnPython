import time
import random
names = ["peter", "david", "slong", "yue"]
cities = ["shanghai", "london", "newyork"]
print(random.choices(names))
# people_num = [1, 2, 3, 4]

# random.choice: return an element
# random.choices: return a subset


def get_people(people_num):
    result = []
    for i in range(people_num):
        people = {
            'ind': i,
            "name": random.choices(names),
            "city": random.choices(cities)
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
            "name": random.choices(names),
            "city": random.choices(cities)
        }
        yield people

peopls2 = gen_people(100)
print(next(peopls2))
print(next(peopls2))
print(next(peopls2))
t1 = time.clock()
peopls = gen_people(100)
t2 = time.clock()
print(t2 - t1)
