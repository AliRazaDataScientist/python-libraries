x = [1,2,3,4,5]
print(dir(x))
print(x.__add__)


class Person:
    def __init__(self,name,age):
        self.n = name
        self.a = age

obj = Person('xyz',20)
print(obj.__dict__)

print(help(Person))