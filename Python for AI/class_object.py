class Person():
    name = 'Ali Raza'
    age = '20'
    job = 'Software Developer'
    def res(self):
        print(f'My name is {self.name}, my age is {self.age} and I am {self.job}.')

xyz = Person()
xyz1 = Person()
xyz.name = 'M Mahdi'
xyz.age = 20
xyz.job = 'Qari'
xyz.res()
xyz1.res()