class Animal:
    def __init__(self,name,color):
        self.n = name
        self.c = color
    def intro(self):
        print(f'Animal name is {self.n} and its color is {self.c}')

class Domastic_Animal(Animal):
    def Dom(self):
        print('We are taking about the Catles')

class Cow(Domastic_Animal):
    def cow(self):
        # self.__testvariable = "Test_Variable"
        print('This class is represting the cows')

objs = Animal('cat','white')
objs.intro()
obj = Cow('Cow','Brown')
obj.intro()
obj.Dom()
obj.cow()
# print('This is for testing access modifier',obj._Cow__testvariable)
# print('This is for testing access modifier',obj.__testvariable)

print('Multiple Inheritance')
class School:
    def __init__(self,name):
        self.n = name
    def show(self):
        print(f'The name is {self.n}')
class Academy:
    def __init__(self,course):
        self.c = course
    def show(self):
        print(f'The course is {self.c}')
class children(School,Academy):
    def __init__(self,name,course):
        School.__init__(self,name)
        Academy.__init__(self,course)
        self.n = name
        self.c = course
newobj = children('Ali','Python')
print(children.mro())

print('Multilevel Inheritance')
class Ani:
    def __init__(self,name,species):
        self.n= name
        self.s= species
    def Ani_c(self):
        print(f'Animal Name is {self.n}')
        print(f'Species Name is {self.s}')
class Pet(Ani):
    def __init__(self,name,breed):
        Ani.__init__(self,name,species = 'Catle')
        self.b = breed
    def Pet_c(self):
        Ani.Ani_c(self)
        print(f'Breed Name is {self.b}')
class cal(Pet):
    def __init__(self,name,color):
        Pet.__init__(self,name,breed='Sahiwal')
        self.c = color
    def call_c(self):
        Pet.Pet_c(self)
        print(f'Color is {self.c}')

test = cal('Cow','White')
test.call_c()


