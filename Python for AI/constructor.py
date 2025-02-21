class Person():
    def __init__(self,n,o):
        self.name = n
        self.occ = o
    def res(self):
        print(f'I am {self.name} and my name is {self.occ}')

a = Person('dev','ali')
a.res()