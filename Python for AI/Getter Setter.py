class get_set:
    def __init__(self,n):
        self.no = n
    def res(self):
        print(f'Value is {self.no}')
    @property
    def res1(self):
        return 10 * self.no
    @res1.setter
    def res1(self,new_value):
        self.no = new_value/10

obj = get_set(5)
obj.res1 = 67
print(obj.res1)
obj.res()

# Another example by my self

class Result:
    def __init__(self,number):
        self.num = number
    def show(self):
        print(f'The number is {self.num}')
    @property
    def gett(self):
        return self.num
    @gett.setter
    def gett(self,newvalue):
        self.num = newvalue * 2


new = Result(10)
new.show()
new.gett = 3
print(new.gett)
new.show()