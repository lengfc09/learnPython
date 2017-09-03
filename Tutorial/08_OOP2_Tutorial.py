# Inheritance---creating subclasses
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


class Developer(Employee):
    # reset the class variables!
    raise_amount = 1.05
    # creat new init function!

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
       # or we can use: Employee.__init(self,first,last,pay)
        self.prog_lang = prog_lang


dev_1 = Developer("Corey", "Schafer", 50000, "Python")
print(dev_1.email)
print(dev_1.pay)
# print(help(Developer))

dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.prog_lang)
# it use the developer: raise_amount


class Manager(Employee):
    # default args can be omitted
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("--->", emp.fullname())

man1 = Manager("Yangyifan", "Chen", 50000)
print(man1.employees)
print(man1.email)
man1.add_emp(dev_1)
man1.print_emps()

# check whether something is a class,

print(isinstance(man1, Developer))
print(isinstance(man1, Manager))

# check whether a class is a subclass of another
print(issubclass(Manager, Developer))
print(issubclass(Manager, Employee))
