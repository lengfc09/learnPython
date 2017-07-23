# special methods
class Employee():
    """for turial"""
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return self.first + " " + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
# Special Functions!

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{}-{}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay
# more:
# __add__(self,other)
# __sub__(self,other)
# __mut__()
# __len__()

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Yue", "Cai", 40000)


print(emp_1.fullname())

# it will be error to: print(emp_1)；repr(emp_1)
print(emp_1)
# <__main__.Employee object at 0x10eebeb70>
print(repr(emp_1))
print(str(emp_1))

print(emp_1 + emp_2)
print(len(emp_1))


# Property Decorators- Getters,Setters,and Deleters
print(emp_1.fullname())
emp_1.first = 'Jim'
print(emp_1.fullname())
print(emp_1.email)
# the email name is not correct.
# a way to solve this is to rewrite the property: Email as an function


class Employee2():
    """for turial"""
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)
# make it a property

    @property
    def fullname(self):
        return self.first + " " + self.last
# setter function for this property methods

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

# deleter function
    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee2("Corey", "Schafer", 50000)
print(emp_1.fullname)
emp_1.first = 'Jim'
print(emp_1.fullname)
print(emp_1.email)
# use setter function
emp_1.fullname = "Yue Cai"
print(emp_1.email)

del emp_1.fullname
print(emp_1.email)
# but we want to access it as an attibute! we use @property
# now we can only take this as an attribute! although it is indeed a function, which can be updated once the parameters are updated

# another question: can we set the propety(function) directly like other attributies?
# eg>   emp_1.email="tetst@cda.com"
# use set functions
