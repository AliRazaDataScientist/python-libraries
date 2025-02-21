class Person:
    company = 'Apple'
    personno = 0
    def __init__(self,n):
        self.name = n
        self.no = '1234567890'
        Person.personno +=1
    def intro(self):
        print(f'{self.personno}.Employee name is {self.name} and the company is {self.company} and it\'s no is {self.no}')
res = Person('Ali Raza')
res.intro()
res1 = Person('M Mahdi')
res1.company = 'Google'
res1.no = '0987654321'
res1.intro()