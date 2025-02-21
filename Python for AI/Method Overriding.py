class calculation:
    def __init__(self,lenght, width):
        self.x = lenght
        self.y = width
    def area(self):
        return self.x*self.y

class Circle(calculation):
    def __init__(self, radius):
        self.rad = radius
        super().__init__(radius, radius)
    def area(self):
        return 3.14* super().area()
cal = calculation(5,5)
print(cal.area())
cal = Circle(5)
print(cal.area())