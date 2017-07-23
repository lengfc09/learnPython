# Python Objected-Oriented Programming


class Employee():
    """for turial"""
# Class Variables:
    num_of_emps = 0
    raise_amount = 1.04
# construction or initialization, and set the attributes
# it always takes the instant as the first argument automatically!

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        # record the number of employers added
        Employee.num_of_emps += 1
# regular method! For instant！ it always takes the instant as the first argument automatically!

    def fullname(self):
        return self.first + " " + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
# classmethod, takse the class itself as the first arg
# 1. we can use it to set the class varibles

    @classmethod
    def raise_amt(cls, amount):
        cls.raise_amount = amount
# 2. we can creat a new construction function

    @classmethod
    def fromstr(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

# staticmethod: not for class, not for instant, just for convenience
    @staticmethod
    def quack(strrr):
        print("hahah", strrr)


e1 = Employee("Yang", "Chen", 33)
print(e1.email)
print(e1.fullname())
print(Employee.num_of_emps)


e1 = Employee("Cai", "Yue", 33)
print(Employee.num_of_emps)
print(e1.raise_amount)
e1.raise_amt(1.05)
print(e1.raise_amount)

# classmethod to creat instant
emp_str = "Yangyifan-Chen-35"
e2 = Employee.fromstr(emp_str)
print(e2.email)


# static function, which can take args
e2.quack("nice")
