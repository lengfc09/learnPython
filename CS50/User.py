# user.py

from Library import Base

assert hasattr(Base, 'foo'), "you fool!"


class Derived(Base):
    def bar(self):
        return "bar"

d1 = Derived()
print(d1.foo())
print(d1.bar())

import sys
print(sys.path)
