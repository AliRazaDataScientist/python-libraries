class Employee:
    company = 'Apple'
    def details(self):
        print(f'My name is {self.name} and i am working in {self.company} company.')
    @classmethod
    def changecompany(cls, newname):
        cls.company = newname


obj = Employee()
obj.name = 'Ali'
obj.details()
print(Employee.company)
obj.name = 'Abbas'
obj.changecompany('Tesla')
obj.details()
print(Employee.company)

print('Now test it second time')

class Student:
    def __init__(self,name,age):
        self.n = name
        self.a = age
    @classmethod
    def call(cls,str):
        return cls(str.split('-')[0],str.split('-')[1])

obj = Student('ali','12')
print(obj.n)
print(obj.a)
# obj.call()

string = 'Qamar-15000'
obj1 = Student.call(string)
print(obj1.n)
print(obj1.a)