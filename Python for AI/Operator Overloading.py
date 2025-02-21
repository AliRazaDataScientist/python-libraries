class vector:
    def __init__(self,x,y,z):
        self.x = x 
        self.y = y
        self.z = z
    def __str__(self):
        return f'{self.x}x+{self.y}y+{self.z}z'
    def __add__(self,i):
        return vector(self.x+i.x,self.y+i.y,self.z+i.z)
obj = vector(4,6,7)
print(obj)
obj1 = vector(5,6,8)
print(obj1)
print(obj+obj1)
print(type(obj+obj1))