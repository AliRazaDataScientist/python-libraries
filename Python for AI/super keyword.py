class parent:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def speak(self):
        print(f'This is parent class and it is using {self.x} and {self.y}')
class child(parent):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z
    def speak(self):
        print(f'This is child class and it is using {self.x} and {self.y}')
    def talk(self):
        print(f'I am talking with you {self.z}')
        super().speak()
obj = child(12,14,15)
obj.speak()
obj.talk()