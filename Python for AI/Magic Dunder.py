print('__init')
class company:
    name = 'Ali'
    def __len__(self):
        n = 0
        for char in self.name:
            n +=1
        return(n)
c = company()
print(len(c))
from Loop import Magic
m = Magic('Ali Raza')
print(str(m))
print(repr(m))
m()